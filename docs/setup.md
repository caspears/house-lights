# Setup

Run commands from the repository root so the local `driver` and `colorschemes` packages resolve. Do not install or upgrade a similarly named PyPI `colorschemes` package: these programs use the bundled implementation.

## Windows development

Use Python 3 with tkinter. The handoff records Python 3.12.3 with tkinter; it does not establish a minimum supported version. Check your environment:

```powershell
python --version
python -m tkinter
python gameday.py --help
python gameday.py --demo
```

`python -m tkinter` opens a test window. No pip installation or `setup.py` invocation is needed for preview. Optional virtual environments are local development choices; do not copy a Windows environment onto the Pi.

## Existing Pi installation

The recorded installation is a Raspberry Pi 3B at `10.0.0.124`, username `pi`, project `/home/pi/Development/APA102_Pi`. These are installation examples, not defaults. Record `python3 --version`, OS version, working interpreter/dependencies, and SPI permissions before changing the environment. The Pi Python version and a reproducible dependency lock are missing.

The bundled driver imports `Adafruit_GPIO` and `Adafruit_GPIO.SPI`. Hardware mode uses SPI bus 0/device 0, MOSI BCM 10 and clock BCM 11. SPI must be enabled and available to the chosen user. Reuse the known working environment first; a fresh modern Pi OS installation and dependency installation procedure have not been validated. Historical upstream setup is retained in [upstream-README.md](upstream-README.md), not endorsed as a tested current recipe.

`setup.py` describes the inherited APA102_Pi 2018.1 package, checks Adafruit_GPIO before setup, and declares `python_requires='>3'`. That declaration does not prove current code compatibility with an old Pi interpreter. It is not a Windows preview installer or a program supervisor.

## Hardware information still needed

The LED count is recorded as 480. Exact roof routing, LED 0 location, per-edge counts, voltage/power supply capacity, power injection, wiring and level shifting must be confirmed on the installation. The included upstream wiring/photos are examples, not an as-built record. Software brightness 1.0 is a rendering setting, not an electrical capacity assessment. See [deployment](deployment.md) for a limited color test.
