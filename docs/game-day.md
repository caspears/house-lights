# Game-day behavior

Implementation: `gameday.py` and `game_show.py`. [GAMEDAY.md](../GAMEDAY.md) is the operational entry point; [Windows simulation](windows-simulation.md) lists every CLI option.

| Feed state | Scene |
| --- | --- |
| No successful snapshot | Off |
| Pregame, more than 2 hours before kickoff | Off |
| Pregame, within 2 hours | Blue/green wave, selected brightness; motion ramps 0.15 ? 1.0 |
| In game, including halftime | Wave at 0.8 speed multiplier |
| Eligible new SEA touchdown | Outward wave plus sparks/rings, 60 seconds |
| Eligible new SEA field goal | Celebration, 30 seconds |
| Completed win | Wave with green/white glitter until stopped |
| Completed loss | Off; process remains running |
| Completed tie | Wave at 0.8; implementation fallback |
| Other incomplete status | Off with waiting detail |

Brightness and user speed multiply controller settings. Kickoff slightly slows motion from 1.0 to 0.8. A delayed `pre` status stays pregame at maximum speed even after scheduled kickoff; final requires the feed's completed flag. Neither a clock nor a lead establishes a final result.

## Demo timeline

Run `python gameday.py --demo`. Seconds 0?60 compress two hours of buildup; 60 is kickoff; [80,140) is touchdown; [155,185) is field goal; 200 onward is the chosen final. Celebrations retain real durations. The window continues until closed. Hardware may use `--duration 220`. Stage jumps and ending controls are preview-only.

## Live data

`--live` requires a date. Without `--event-id`, scoreboard discovery requires exactly one SEA game on that date; the selected ID is then retained. Each summary refresh supplies kickoff/status/score, including updated kickoff time. There is no automatic next-game discovery.

The code uses publicly reachable, undocumented ESPN endpoints under `https://site.api.espn.com/apis/site/v2/sports/football/nfl/`: `scoreboard?dates=YYYYMMDD` and `summary?event=EVENT_ID`. Polling runs in a daemon thread, defaults to 15 seconds (minimum 15), and waits the poll interval after a request; each request has an eight-second timeout. Availability, schema, and timeliness are not guaranteed.

Detection uses Seattle team ID and explicit play-type text containing touchdown or field goal, not aggregate score deltas. Opponent scores and extra points do not trigger. First success baselines all existing scoring IDs. Later unseen IDs queue only when the snapshot is in-game and incomplete. Deduplication is memory-only; restarting skips history again.

`--celebration-delay` delays scoring only, measured from when rendering consumes the queued event. Celebrations queue and resume the ordinary wave afterward. Final or other non-game scenes clear pending/active celebrations. Corrections cannot undo an already played animation.

After an error, last-known game state continues to drive lighting. Once age exceeds `max(60 seconds, 3 * poll)`, scoring celebrations are cleared; preview/status labels report trouble. Pregame can still advance from the last kickoff timestamp. Recovery can celebrate missed scores during an outage; durable history and replay-age filtering are absent. Pause in live preview does not stop polling or wall-clock state.

## Evidence and limits

The handoff reports October 10 discovery of SF at SEA, event `401872992`, kickoff October 11, 2026 at 20:25 UTC (1:25 p.m. Pacific), implying 11:25 a.m. buildup. This is historical session evidence, not rechecked schedule information. It also reports completed October 4 summary parsing and background polling. No live request was made during this documentation review.

Six local unit tests passed during review. They do not establish actual live scoring latency, prolonged recovery, physical brightness, or successful updated Pi operation. The byte-decoding fix is present and tested with mocked HTTP; a successful Pi run after that fix is still unreported.
