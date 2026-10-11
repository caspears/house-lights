# Game-day quick start

The new runner provides a Windows demo and experimental live Seahawks feed. Deploy both `gameday.py` and `game_show.py`; Pi output requires the existing Adafruit_GPIO/SPI dependencies. RGB order was physically reported correct. The complete updated Pi controller and real-time game transitions remain unverified.

From the repository directory on Windows:

```powershell
python gameday.py --demo
python gameday.py --live --game-date 2026-10-11
python -B -m unittest test_game_show -v
```

The date is a dated example. Confirm the selected game/score in preview. Before hardware output, stop any other strip writer and follow [deployment and rollback instructions](docs/deployment.md).

On the recorded Pi installation:

```bash
cd /home/pi/Development/APA102_Pi
python3 gameday.py --hardware --effect color-test --brightness 0.15 --duration 12
python3 gameday.py --hardware --demo --brightness 1 --duration 220
python3 gameday.py --hardware --live --game-date 2026-10-11 --brightness 1
```

Ctrl+C requests clear/cleanup. A VNC desktop terminal left open is the current temporary unattended approach; no service is configured. See [game-day behavior](docs/game-day.md) for authoritative state transitions, demo timeline, scoring delays, stale-feed limits and dated schedule evidence, and [simulation/CLI](docs/windows-simulation.md) for controls and defaults.

For holiday and other event programs, start at the [project README](README.md).
