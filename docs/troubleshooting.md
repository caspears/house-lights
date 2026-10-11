# Troubleshooting

| Symptom | Check / action |
| --- | --- |
| Preview cannot import tkinter | Check the selected Python installation with `python -m tkinter`; preview requires Tk. |
| Windows asks for Adafruit_GPIO | Use `gameday.py` without `--hardware`; legacy scripts and setup.py load hardware dependencies. |
| Missing colorschemes/effect class | Run from repository root with the bundled modules; do not substitute the PyPI package. |
| Teal/purple rather than intended blue/green | New runner defaults to `rgb`; legacy template defaults to `rbg`. Stop other writers, run the limited RGB test from deployment docs, and confirm physical channel order. |
| Pi reports JSON object must be str, not bytes | Current `get_json` explicitly decodes UTF-8. Copy both new modules and restart; verify the actual interpreter/path. The post-fix Pi outcome is not yet recorded. |
| SPI/dependency error | Confirm same interpreter and permissions as working scripts, Adafruit_GPIO/SPI availability, enabled SPI and device access. Fresh dependency installation is unverified. |
| Flicker or competing patterns | Stop competing controllers; there is no single-writer lock. |
| Live remains off | Check date, exactly one SEA game (or explicit ID), connectivity and status text. Before initial success and before buildup, off is intentional. |
| Feed stale or no celebration | Check network/status; stale clears celebrations. Startup skips history; opponent scores/extra points are ignored. Final can supersede queued scores. |
| Celebration before/after TV score | Add nonnegative `--celebration-delay` for early feed events; it cannot accelerate late data. |
| Loss leaves a process running | Intentional: completed loss renders black until stopped. |
| SSH disconnect ends show | Use a Pi desktop terminal through VNC temporarily and leave it open; managed service remains planned. |
| `--duration` does not close preview | It is hardware-only. Close the Tk window. |
| Legacy schedule stops late | Time windows are checked between blocking effect batches, not continuously; use Pi local clock/timezone. |
| LEDs remain on after forced kill | Forced kill/power loss skips cleanup. Confirm no writer remains before restarting a controller to clear output. |

Do not use broad unittest discovery: legacy `test.py` and `20181212/test.py` are hardware scripts, not safe unit tests. Run only `python -B -m unittest test_game_show -v` for the existing focused suite.

Record unresolved failures with interpreter/OS, command, revision, traceback/status, current program, and physical observation. Do not include credentials. Outstanding installation details are listed in [setup](setup.md) and [roadmap](roadmap.md).
