"""Game-day state machine, compressed demo, and optional ESPN feed adapter."""
import datetime as dt
import json
import math
import queue
import threading
import time
import urllib.request

BASE = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/'
TOUCHDOWN_SECONDS = 60
FIELD_GOAL_SECONDS = 30
DEMO_TOUCHDOWN = 80
DEMO_FIELD_GOAL = 155
DEMO_FINAL = 200


def get_json(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'HouseLights/1.0'})
    with urllib.request.urlopen(request, timeout=8) as response:
        # Older Pi Python versions require text rather than bytes for JSON input.
        return json.loads(response.read().decode('utf-8'))


def find_game(date):
    data = get_json(BASE + 'scoreboard?dates=' + date.replace('-', ''))
    games = [event for event in data.get('events', [])
             if any(c.get('team', {}).get('abbreviation') == 'SEA'
                    for c in event.get('competitions', [{}])[0].get('competitors', []))]
    if len(games) != 1:
        raise ValueError('Expected one Seahawks game on {}; found {}. Check --game-date.'.format(date, len(games)))
    return str(games[0]['id'])


def parse_summary(data):
    competition = data['header']['competitions'][0]
    competitors = competition['competitors']
    seattle = next(c for c in competitors if c['team']['abbreviation'] == 'SEA')
    opponent = next(c for c in competitors if c['team']['abbreviation'] != 'SEA')
    status = competition['status']['type']
    # ESPN uses UTC Z timestamps. strptime also supports older Pi Python versions.
    raw_date = competition['date']
    pattern = ('%Y-%m-%dT%H:%M:%S.%fZ' if '.' in raw_date else
               '%Y-%m-%dT%H:%M:%SZ' if raw_date.count(':') == 2 else '%Y-%m-%dT%H:%MZ')
    kickoff = dt.datetime.strptime(raw_date, pattern).replace(tzinfo=dt.timezone.utc).timestamp()
    scores = []
    for play in data.get('scoringPlays', []):
        team = play.get('team', {})
        kind = str(play.get('type', {}).get('text', '')).lower()
        # Explicit scoring type only: no inference from aggregate score changes.
        if str(team.get('id')) == str(seattle['team']['id']):
            if 'touchdown' in kind:
                scores.append((str(play['id']), 'touchdown'))
            elif 'field goal' in kind:
                scores.append((str(play['id']), 'field goal'))
    own, other = int(seattle.get('score', 0)), int(opponent.get('score', 0))
    return {'kickoff': kickoff, 'state': status['state'],
            'completed': bool(status.get('completed', False)),
            'detail': status.get('detail', status.get('description', '')),
            'score': 'SEA {} – {} {}'.format(own, opponent['team']['abbreviation'], other),
            'outcome': 'win' if own > other else 'loss' if own < other else 'tie',
            'scoring': scores}


class Feed:
    """Network work stays off the animation thread. First fetch establishes a baseline."""
    def __init__(self, date, event_id=None, poll=15):
        self.date, self.event_id, self.poll = date, event_id, poll
        self.snapshot = None
        self.error = 'Connecting to score feed…'
        self.updated = 0
        self.events = queue.Queue()
        self.stop = threading.Event()
        self.lock = threading.Lock()
        self.seen = None
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def accept(self, snapshot):
        scoring = snapshot['scoring']
        with self.lock:
            if self.seen is None:
                self.seen = {identifier for identifier, kind in scoring}
            else:
                for identifier, kind in scoring:
                    if identifier not in self.seen:
                        self.seen.add(identifier)
                        if snapshot['state'] == 'in' and not snapshot['completed']:
                            self.events.put(kind)
            self.snapshot, self.updated, self.error = snapshot, time.monotonic(), ''

    def run(self):
        while not self.stop.is_set():
            try:
                if not self.event_id:
                    self.event_id = find_game(self.date)
                self.accept(parse_summary(get_json(BASE + 'summary?event=' + self.event_id)))
            except Exception as exc:
                with self.lock:
                    self.error = 'Feed unavailable: ' + str(exc)
            self.stop.wait(self.poll)

    def read(self):
        with self.lock:
            return self.snapshot, self.updated, self.error

    def close(self):
        self.stop.set()


def stage(snapshot, now):
    """Return scene, brightness multiplier, speed multiplier, and description."""
    if snapshot['completed']:
        outcome = snapshot['outcome']
        return (outcome, 1, .8, 'Final: ' + outcome)
    if snapshot['state'] == 'pre':
        remaining = snapshot['kickoff'] - now
        if remaining > 7200:
            return ('off', 0, .15, 'Waiting: buildup starts two hours before kickoff')
        progress = max(0, min(1, 1 - remaining / 7200))
        return ('wave', 1, .15 + .85 * progress,
                'Pregame buildup: {:.0%} | kickoff in {:.0f} min'.format(progress, max(0, remaining)/60))
    if snapshot['state'] == 'in':
        return ('wave', 1, .8, 'Game in progress')
    return ('off', 0, .15, 'Waiting: ' + snapshot.get('detail', 'unknown game status'))


def demo_stage(elapsed, outcome):
    # Pregame is compressed; scoring celebrations retain their real durations.
    if elapsed < 60:
        p = elapsed / 60
        return ('wave', 1, .15 + .85*p, 'DEMO | pregame: {:.0f} min to kickoff'.format(120*(1-p)))
    if DEMO_TOUCHDOWN <= elapsed < DEMO_TOUCHDOWN + TOUCHDOWN_SECONDS:
        return ('celebration', 1, 1, 'DEMO | Seahawks touchdown + fireworks')
    if DEMO_FIELD_GOAL <= elapsed < DEMO_FIELD_GOAL + FIELD_GOAL_SECONDS:
        return ('celebration', 1, .8, 'DEMO | Seahawks field goal + fireworks')
    if elapsed >= DEMO_FINAL:
        return (outcome, 1, .8, 'DEMO | final: ' + outcome + ' (restart demo to replay)')
    return ('wave', 1, .8, 'DEMO | game in progress')


def decorate(pixels, scene, seconds, brightness):
    """Sparse green/white sparks over a wave or touchdown, within brightness cap."""
    if scene not in ('win', 'celebration'):
        return pixels
    result = []
    t = seconds
    for i, pixel in enumerate(pixels):
        # Deterministic per-pixel phases, with brief bright peaks and gradual fades.
        pulse = max(0, math.sin(t * (3 + (i * 17 % 13)/10) + i * 2.399)) ** 70
        if scene == 'celebration':
            # Expanding spark rings originating at repeatable positions along the strip.
            burst = int(t // 2)
            center = ((burst * 137 + 79) % len(pixels))
            distance = abs(i-center) / max(1, len(pixels))
            radius = (t % 2) * .24
            ring = max(0, 1 - abs(distance-radius)/.025) * max(0, 1-(t % 2)/2)
            pulse = max(pulse, ring)
        target = (220,255,225) if i % 3 else (70,255,0)
        result.append(tuple(round(c + (v*brightness-c)*pulse) for c,v in zip(pixel,target)))
    return result


class Show:
    def __init__(self, args):
        self.args = args
        self.feed = Feed(args.game_date, args.event_id, args.poll) if args.live else None
        self.active = None
        self.pending = []
        self.last_scene = None
        self.motion = 0
        self.previous = None

    def render(self, elapsed, brightness, speed):
        from gameday import frame, selected
        args = self.args
        if args.demo:
            scene, level, rate, label = demo_stage(elapsed, args.demo_outcome)
        elif self.feed:
            snapshot, updated, error = self.feed.read()
            if snapshot is None:
                scene, level, rate, label = 'off', 0, 1, error
            else:
                scene, level, rate, label = stage(snapshot, time.time())
                label += ' | ' + snapshot['score']
                stale = time.monotonic() - updated > max(60, args.poll*3)
                while True:
                    try:
                        kind = self.feed.events.get_nowait()
                        self.pending.append((elapsed + args.celebration_delay, kind))
                    except queue.Empty:
                        break
                if stale:
                    self.pending.clear()
                    self.active = None
                if scene == 'wave' and snapshot['state'] == 'in' and not stale:
                    if self.active is None and self.pending and self.pending[0][0] <= elapsed:
                        _, kind = self.pending.pop(0)
                        self.active = (elapsed, TOUCHDOWN_SECONDS if kind == 'touchdown' else FIELD_GOAL_SECONDS, kind)
                    if self.active:
                        started, duration, kind = self.active
                        if elapsed - started < duration:
                            scene, label = 'celebration', label + ' | Seahawks ' + kind
                        else:
                            self.active = None
                else:
                    self.pending.clear()
                    self.active = None
                if error or stale:
                    label += ' | ' + (error or 'Feed stale; waiting for updates')
        else:
            return frame(selected(args.effect, elapsed), elapsed, args.leds, brightness, speed), args.effect
        # Integrate changing speed: accelerating pregame does not jump animation phase.
        delta = 0 if self.previous is None else max(0, elapsed-self.previous)
        self.previous = elapsed
        self.motion += delta * rate * speed
        if scene in ('off', 'loss'):
            pixels = [(0,0,0)] * args.leds
        else:
            effect = 'touchdown' if scene == 'celebration' else 'wave'
            pixels = frame(effect, self.motion, args.leds, brightness*level, 1)
            pixels = decorate(pixels, scene, elapsed, brightness*level)
        return pixels, label

    def close(self):
        if self.feed:
            self.feed.close()
