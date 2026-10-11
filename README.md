# House Lights

Outdoor LED lighting for holidays, birthdays, sports, and other activities. The installation described in [CODEX_HANDOFF.md](CODEX_HANDOFF.md) uses 480 APA102/DotStar LEDs and a Raspberry Pi 3B. Windows is the development and preview environment.

The repository contains two implementations: existing hardware-only holiday/event scripts, and a newer shared-frame runner with Windows preview, regular effects, a simulated Seahawks game, and an experimental live ESPN controller. Home Assistant selection, Pi monitoring, and dedicated Google Calendar scheduling are planned; none is configured here.

## Start on Windows

From the repository directory with Python 3 and tkinter:

```powershell
python gameday.py --demo
python -B -m unittest test_game_show -v
```

The preview needs no third-party Python packages. Pi hardware output requires the existing Adafruit_GPIO/SPI dependencies. Do not import legacy scripts to explore them: many start hardware work or endless loops at module scope.

## Documentation

- [Setup and prerequisites](docs/setup.md)
- [Windows simulation and CLI](docs/windows-simulation.md)
- [Raspberry Pi deployment, updates, and rollback](docs/deployment.md)
- [Architecture](docs/architecture.md)
- [Lighting programs and source inventory](docs/programs.md)
- [Game-day behavior and feed limits](docs/game-day.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Future plans and open decisions](docs/roadmap.md)
- [Game-day operational quick start](GAMEDAY.md)

## Validation status

On October 10, 2026, all six existing game-show unit tests passed during this documentation review. They cover state boundaries, demo frame limits/loss, celebration durations, scoring filters, baseline/deduplication, and byte decoding with mocked networking. Legacy scripts were read/parsed as source, never imported or run.

The handoff reports earlier Windows GUI, frame, fake-strip, and ESPN request checks; those were not repeated here. User-reported Pi observations include working light output and a successful RGB color-order test. A successful Pi run after the JSON decoding fix, the complete updated hardware show, real live scoring/final transitions, daytime visibility, and prolonged outage recovery remain unverified.

## Attribution and repository portability

Built on Martin Erzberger's [APA102_Pi](https://github.com/tinue/APA102_Pi), including its driver, templates, samples, and images. The bundled [LICENSE](LICENSE) is GNU GPL version 2; inherited packaging identifies GPLv2 and the driver credits Martin Erzberger (2016?2018). Preserve those notices and license when moving this project. The [original upstream README](docs/upstream-README.md) is retained as historical documentation, including contributor credits; its 2018 setup instructions are not current installation guidance.

Git hosting is incidental to running the lights. The new destination repository URL is still unknown. No remotes, hardware behavior, or deployment were changed by this documentation task. See deployment guidance before transferring the repository.
