import queue
import threading
import unittest
from unittest.mock import patch
from types import SimpleNamespace

import game_show as g


class GameShowTests(unittest.TestCase):
    def test_feed_decodes_bytes_before_json_parsing(self):
        import io
        original_loads = g.json.loads
        def text_only(value):
            self.assertIsInstance(value, str)
            return original_loads(value)
        with patch.object(g.urllib.request, 'urlopen', return_value=io.BytesIO(b'{"ok": true}')):
            with patch.object(g.json, 'loads', side_effect=text_only):
                self.assertEqual(g.get_json('https://example.com'), {'ok': True})

    def test_pregame_and_results(self):
        snapshot = dict(kickoff=10000, state='pre', completed=False, outcome='win')
        self.assertEqual(g.stage(snapshot, 0)[0], 'off')
        self.assertEqual(g.stage(snapshot, 2800)[1:3], (1, .15))
        self.assertEqual(g.stage(snapshot, 6400)[1], 1)
        self.assertEqual(g.demo_stage(0, 'win')[1], 1)
        self.assertEqual(g.demo_stage(30, 'win')[1], 1)
        self.assertEqual(g.stage(snapshot, 10000)[1:3], (1, 1))
        snapshot['state'] = 'in'
        self.assertEqual(g.stage(snapshot, 10001)[0], 'wave')
        snapshot['completed'] = True
        self.assertEqual(g.stage(snapshot, 10002)[0], 'win')
        snapshot['outcome'] = 'loss'
        self.assertEqual(g.stage(snapshot, 10002)[0], 'loss')

    def test_demo_frames_and_loss(self):
        args = SimpleNamespace(live=False, demo=True, demo_outcome='win', leds=480)
        show = g.Show(args)
        for t in (0, 30, 59, 60, 80, 139, 140, 155, 184, 185, 200, 220):
            pixels, label = show.render(t, .25, 1)
            self.assertEqual(len(pixels), 480)
            self.assertTrue(all(0 <= c <= 64 for p in pixels for c in p))
        args.demo_outcome = 'loss'
        self.assertTrue(all(p == (0,0,0) for p in show.render(210,.25,1)[0]))

    def test_celebration_durations(self):
        self.assertEqual(g.TOUCHDOWN_SECONDS, 60)
        self.assertEqual(g.FIELD_GOAL_SECONDS, 30)
        for start, duration in ((g.DEMO_TOUCHDOWN, 60), (g.DEMO_FIELD_GOAL, 30)):
            self.assertEqual(g.demo_stage(start, 'win')[0], 'celebration')
            self.assertEqual(g.demo_stage(start+duration-.01, 'win')[0], 'celebration')
            self.assertEqual(g.demo_stage(start+duration, 'win')[0], 'wave')

    def test_no_startup_replay_or_duplicate_scores(self):
        feed = g.Feed.__new__(g.Feed)
        feed.lock, feed.events, feed.seen = threading.Lock(), queue.Queue(), None
        snapshot = dict(state='in', completed=False, scoring=[('old','touchdown')])
        feed.accept(snapshot)
        self.assertTrue(feed.events.empty())
        snapshot['scoring'] = [('old','touchdown'), ('new','field goal')]
        feed.accept(snapshot)
        feed.accept(snapshot)
        self.assertEqual(feed.events.get_nowait(), 'field goal')
        self.assertTrue(feed.events.empty())
        snapshot.update(completed=True, scoring=[('final','touchdown')])
        feed.accept(snapshot)
        self.assertTrue(feed.events.empty())

    def test_parse_scores_filters_opponent_and_extra_points(self):
        data = {'header': {'competitions': [{
            'date': '2026-10-11T20:25Z',
            'status': {'type': {'state': 'in', 'completed': False}},
            'competitors': [{'team': {'id':'26','abbreviation':'SEA'},'score':'10'},
                            {'team': {'id':'25','abbreviation':'SF'},'score':'7'}]}]},
            'scoringPlays': [
                {'id':'1','team':{'id':'26'},'type':{'text':'Passing Touchdown'}},
                {'id':'2','team':{'id':'25'},'type':{'text':'Passing Touchdown'}},
                {'id':'3','team':{'id':'26'},'type':{'text':'Extra Point Good'}},
                {'id':'4','team':{'id':'26'},'type':{'text':'Field Goal Good'}}]}
        self.assertEqual(g.parse_summary(data)['scoring'], [('1','touchdown'),('4','field goal')])


if __name__ == '__main__':
    unittest.main()
