# Windows simulation

```powershell
python gameday.py
python gameday.py --demo
python gameday.py --demo --demo-outcome loss
python gameday.py --effect color-test --brightness 0.15
python gameday.py --live --game-date 2026-10-11
```

The ordinary preview offers playlist, wave, comet, sparkle, touchdown, and color-test. Playlist rotates wave ? comet ? sparkle ? touchdown every 30 seconds; the ordinary touchdown effect is not a live scoring event. The roof drawing uses approximate 15% / 70% / 15% sections plus a linear strip. It does not establish real routing or orientation.

Brightness and speed sliders and Pause are available. Demo adds stage jumps and a win/loss/tie ending selector; its effect selector is disabled, as in live mode. Pause freezes elapsed animation/demo time. In live mode network polling and wall-clock game state continue, so Pause is not a feed pause. Close the window to stop. `--duration` applies only to hardware mode and does not close the preview.

## CLI defaults and scope

| Option | Default / behavior |
| --- | --- |
| `--hardware` | Absent: Tk preview; present: Pi output |
| `--effect` | `playlist`; choices above |
| `--leds` | 480; positive integer |
| `--brightness` | 1.0; range 0?1, software RGB scaling |
| `--speed` | 1; greater than zero |
| `--fps` | 30; integer 1?120, target rather than measured rate |
| `--order` | `rgb`; six RGB permutations, hardware only |
| `--demo`, `--live` | Mutually exclusive; neither uses ordinary effects |
| `--demo-outcome` | `win`; also `loss`, `tie` |
| `--game-date` | Required in live mode, YYYY-MM-DD, even with event ID |
| `--event-id` | Optional; bypasses scoreboard discovery |
| `--poll` | 15 seconds; minimum 15 |
| `--celebration-delay` | 0 seconds; nonnegative, scoring only |
| `--duration` | 0: until stopped; nonnegative seconds, hardware only |

Game controllers choose scenes regardless of `--effect`. Color-test changes red/green/blue every four elapsed seconds; speed does not change that cadence. CLI brightness defaults to 1.0 although the internal `frame()` helper's default is 0.25.

The legacy holiday scripts are not wired into this simulator. [Programs](programs.md) distinguishes them from the new effects. No GUI smoke test was performed in this documentation review; earlier GUI checks are reported in the handoff.
