# Lighting programs

Legacy scripts below are hardware-oriented source, not selectable programs in the new runner. They import the bundled colorschemes/driver, often execute at module scope, and many loop indefinitely. They were inspected statically, never imported or executed during this review. Physical behavior and compatibility with a future supervisor remain unverified.

## New runner effects

`gameday.py` provides wave (blue/green sinusoid), comet (green head/trail on dark blue), sparkle (deterministic green/white pulses), touchdown (outward green pulse on blue), color-test (solid R/G/B, four seconds each), and playlist (first four, 30 seconds each). Demo/live add scene selection and overlays. See [game-day](game-day.md) and [simulation](windows-simulation.md).

## Legacy inventory and interpretation

Most event scripts use 480 LEDs; exceptions and exact settings appear below. Christmas variants gate batches by Pi local wall time; the original uses 15:30?23:45 and 06:25?08:35, extended uses 15:30?23:45 and 04:30?07:15. Halloween cycle uses 16:00?00:30; Thanksgiving uses 15:30?23:30 and 04:30?07:30. Other always-true branches are not schedules even where time helpers/comments remain.

Christmas combines twinkle, star-field fades, red/blue collapse scanners, and pink fades. NewYearsLights retains similar effects; its fireworks comment is a TODO, not the newer game-show overlay. Seahawks.py also retains Christmas-like colors rather than implementing a live score feed. SeahawksDay uses blue/green random collapse scanners without live scoring.

Palettes must be read literally: Frozen lists `FFFFFF, CCFF33, 33FF00`; Minnie Mouse lists `CCCC33, 77FF00`; Independence Day lists `FFFFFF, FF0000, 00FF00` (white/red/green in numeric RGB, not a conventional red/white/blue palette). Halloween cycle lists `220006, 100000, 220006`, Thanksgiving `220006, 000010`, and Valentines `FF5555, FF0000`. Legacy channel order defaults to rbg, so numeric RGB and physical appearance may differ. Preserve these settings pending user review rather than silently correcting them.

`clear.py` targets 1024 LEDs through a black Scanner, not the recorded 480. `sample.py` directly drives 42 LEDs and waits 20 seconds. `runcolorcycle.py` uses 144 LEDs; the Blinkt sample uses 8 with BCM 23/24 bit-banged output. Neither is a roof installation default. `test.py` and the dated backup are hardware experiments, not unittest suites. ChristmasLightsDemo is a legacy 144-LED script, distinct from `gameday.py --demo`.

Template nominal batch time is pause ? steps ? cycles plus rendering/SPI overhead and explicit sleeps. Comments estimating durations can disagree with actual numbers. A time gate is checked between batches, so a program can overrun the end of its window. `global_brightness=100`/255 is clamped to 31 by the driver; do not confuse it with the new runner's software 0?1 brightness. The template only promises cleanup on normal completion/KeyboardInterrupt, not a general supervisor lifecycle.

The source index below records executable AST statements in source order, excluding commented-out calls and triple-quoted examples. A constructor alone does not run an effect: look for the subsequent `.start()`, and read its enclosing branch/loop in the linked source. Loop counts and conditions are included; this is a static index, not a runtime trace. Exact call parameters preserve colors, pauses, steps, cycles, brightness and pin choices without claiming measured durations.

## ChristmasLights.py

[Source](../ChristmasLights.py)

```python
# line 8
NUM_LED =480
# line 15
if begin_time < end_time:
# line 22
while True:
# line 26
if is_time_between(time(15, 30), time(23, 45)) or is_time_between(time(6, 25), time(8, 35)):
# line 30
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 32
MY_CYCLE.start()
# line 36
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 38
MY_CYCLE.start()
# line 41
for i in range(40):
# line 44
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 46
MY_CYCLE.start()
# line 50
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 52
MY_CYCLE.start()
# line 57
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=30000)
# line 61
for i in range(50):
# line 63
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=1000)
# line 65
MY_CYCLE.start()
# line 66
t.sleep(.2)
# line 70
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 72
MY_CYCLE.start()
# line 76
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 78
MY_CYCLE.start()
# line 87
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 89
MY_CYCLE.start()
# line 93
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
# line 95
MY_CYCLE.start()
# line 96
t.sleep(120)
```

## ChristmasLights_ext.py

[Source](../ChristmasLights_ext.py)

```python
# line 8
NUM_LED =480
# line 15
if begin_time < end_time:
# line 22
while True:
# line 26
if is_time_between(time(15, 30), time(23, 45)) or is_time_between(time(4, 30), time(7, 15)):
# line 30
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 32
MY_CYCLE.start()
# line 36
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 38
MY_CYCLE.start()
# line 41
for i in range(40):
# line 44
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 46
MY_CYCLE.start()
# line 50
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 52
MY_CYCLE.start()
# line 57
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=30000)
# line 61
for i in range(50):
# line 63
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=1000)
# line 65
MY_CYCLE.start()
# line 66
t.sleep(.2)
# line 70
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 72
MY_CYCLE.start()
# line 76
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 78
MY_CYCLE.start()
# line 87
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 89
MY_CYCLE.start()
# line 93
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
# line 95
MY_CYCLE.start()
# line 96
t.sleep(120)
```

## ChristmasLightsDemo.py

[Source](../ChristmasLightsDemo.py)

```python
# line 8
NUM_LED = 144
# line 15
if begin_time < end_time:
# line 21
t.sleep(5)
# line 26
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                  led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=400)
# line 32
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=150)
# line 34
MY_CYCLE.start()
# line 37
for i in range(1):
# line 40
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 42
MY_CYCLE.start()
# line 46
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 48
MY_CYCLE.start()
# line 52
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                   fade_time = 1, num_cycles=1500)
# line 58
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=75)
# line 60
MY_CYCLE.start()
# line 64
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                  led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=500)
# line 75
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=100)
# line 80
for i in range(2):
# line 83
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [0x00FF00], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 85
MY_CYCLE.start()
# line 89
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 91
MY_CYCLE.start()
# line 94
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 96
MY_CYCLE.start()
# line 97
t.sleep(120)
```

## NewYearsLights.py

[Source](../NewYearsLights.py)

```python
# line 8
NUM_LED = 480
# line 18
if begin_time < end_time:
# line 25
while True:
# line 30
if True:
# line 33
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 39
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 41
MY_CYCLE.start()
# line 44
for i in range(40):
# line 47
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.01, num_steps_per_cycle=82, color = [0xFFFFFF], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 56
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=30000)
# line 58
MY_CYCLE.start()
# line 67
for i in range(50):
# line 69
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.0001, num_steps_per_cycle=1, color =0xF08EC0, color_brightness = 100, global_brightness = 100, \
                                       fade_time = .01, num_cycles=100)
# line 72
t.sleep(.4)
# line 75
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 77
MY_CYCLE.start()
# line 81
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 83
MY_CYCLE.start()
# line 92
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 94
MY_CYCLE.start()
# line 98
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
# line 100
MY_CYCLE.start()
# line 101
t.sleep(120)
```

## HalloweenLights.py

[Source](../HalloweenLights.py)

```python
# line 8
NUM_LED = 144
# line 15
if begin_time < end_time:
# line 27
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0x220006, color_brightness = 100, global_brightness = 100, \
                                  led_multiplier = 1, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=400)
# line 29
MY_CYCLE.start()
# line 33
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = 0x101000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 40
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.05, num_steps_per_cycle=1, color = 0x44000A, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 46
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.05, num_steps_per_cycle=1, color = 0x220006, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 52
for i in range(4):
# line 55
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=1, color = [0x153000], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 10, snake_separation = 0, num_cycles=1)
# line 58
MY_CYCLE.start()
# line 62
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=72, color = [0x220006], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 10, snake_separation = 0, num_cycles=1)
# line 64
MY_CYCLE.start()
# line 68
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=72, color = [0x00020], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 10, snake_separation = 0, num_cycles=1)
# line 70
MY_CYCLE.start()
# line 74
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                   fade_time = 1, num_cycles=1500)
# line 80
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=75)
# line 86
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                  led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=500)
# line 97
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                  blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=100)
# line 102
for i in range(2):
# line 105
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [0x00FF00], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 111
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                            length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 116
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 118
MY_CYCLE.start()
# line 119
t.sleep(120)
```

## HalloweenLights_cycle.py

[Source](../HalloweenLights_cycle.py)

```python
# line 9
NUM_LED = 480
# line 11
colorList = [0x220006, 0x100000, 0x220006]
# line 18
if begin_time < end_time:
# line 23
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0x220006, color_brightness = 100, global_brightness = 100, \
                                  led_multiplier = 1, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=400)
# line 29
while True:
# line 31
if is_time_between(time(16, 0), time(0, 30)):
# line 48
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, 2)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=600)
# line 50
MY_CYCLE.start()
# line 54
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.025, num_steps_per_cycle=1, color = colorList[random.randint(0, 2)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 61
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, 2)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 67
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, 2)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 73
for i in range(2):
# line 76
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.00025, num_steps_per_cycle=1, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 83
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.00025, num_steps_per_cycle=1, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 89
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.00025, num_steps_per_cycle=1, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 95
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =colorList[random.randint(0, 2)], color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=15000)
# line 103
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, 2)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 1, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=800)
# line 105
MY_CYCLE.start()
# line 114
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = colorList[random.randint(0, 2)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 119
for i in range(2):
# line 122
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 128
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 133
t.sleep(60)
# line 135
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 137
MY_CYCLE.start()
# line 138
t.sleep(120)
```

## ThanksgivingLights_cycle.py

[Source](../ThanksgivingLights_cycle.py)

```python
# line 9
NUM_LED = 480
# line 11
colorList = [0x220006, 0x000010]
# line 18
if begin_time < end_time:
# line 25
while True:
# line 27
if is_time_between(time(15, 30), time(23, 30)) or is_time_between(time(4, 30), time(7, 30)):
# line 43
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=2000)
# line 49
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 56
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 62
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 68
for i in range(2):
# line 71
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 74
MY_CYCLE.start()
# line 78
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 84
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 90
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=15000)
# line 98
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=10000)
# line 100
MY_CYCLE.start()
# line 109
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 111
MY_CYCLE.start()
# line 114
for i in range(2):
# line 117
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 123
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 128
t.sleep(60)
# line 130
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 132
MY_CYCLE.start()
# line 133
t.sleep(120)
```

## ValentinesLights.py

[Source](../ValentinesLights.py)

```python
# line 9
NUM_LED = 480
# line 12
colorList = [0xFF5555, 0xFF0000]
# line 19
if begin_time < end_time:
# line 26
while True:
# line 29
if True:
# line 34
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=200)
# line 40
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 47
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 53
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 59
for i in range(2):
# line 62
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.01, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 65
MY_CYCLE.start()
# line 72
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.001, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 78
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 81
for i in range(2):
# line 84
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 200, blink_color = colorList[random.randint(0, len(colorList) - 1)], fade_time = 1, num_cycles=1200)
# line 88
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.005, num_steps_per_cycle=1, color =colorList[0], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 2000, blink_color = colorList[1], fade_time = 1, num_cycles=1200)
# line 90
MY_CYCLE.start()
# line 92
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[1], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 2000, blink_color = colorList[0], fade_time = 1, num_cycles=1200)
# line 94
MY_CYCLE.start()
# line 98
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=15000)
# line 106
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=250)
# line 117
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 122
for i in range(2):
# line 125
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 131
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 136
t.sleep(60)
# line 138
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 140
MY_CYCLE.start()
# line 141
t.sleep(120)
```

## IndependenceDayLights.py

[Source](../IndependenceDayLights.py)

```python
# line 9
NUM_LED = 480
# line 12
colorList = [0xFFFFFF, 0xFF0000, 0x00FF00]
# line 19
if begin_time < end_time:
# line 26
while True:
# line 29
if True:
# line 34
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=200)
# line 40
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 47
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 53
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 59
for i in range(2):
# line 62
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.01, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 65
MY_CYCLE.start()
# line 72
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.001, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 78
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 81
for i in range(2):
# line 84
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 200, blink_color = colorList[random.randint(0, len(colorList) - 1)], fade_time = 1, num_cycles=1200)
# line 88
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.005, num_steps_per_cycle=1, color =colorList[0], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 2000, blink_color = colorList[1], fade_time = 1, num_cycles=1200)
# line 90
MY_CYCLE.start()
# line 92
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[1], color_brightness = 100, global_brightness = 100, \
                                              led_multiplier = 2, blink_factor = 2000, blink_color = colorList[0], fade_time = 1, num_cycles=1200)
# line 94
MY_CYCLE.start()
# line 98
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=15000)
# line 106
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=250)
# line 117
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 122
for i in range(2):
# line 125
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 131
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 136
t.sleep(60)
# line 138
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 140
MY_CYCLE.start()
# line 141
t.sleep(120)
```

## CaiaBirthday_Frozen_lights.py

[Source](../CaiaBirthday_Frozen_lights.py)

```python
# line 9
NUM_LED = 480
# line 11
colorList = [0xFFFFFF,0xCCFF33, 0x33FF00]
# line 19
if begin_time < end_time:
# line 26
while True:
# line 29
if True:
# line 45
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=200)
# line 51
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 58
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 64
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 70
for i in range(2):
# line 73
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.001, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 76
MY_CYCLE.start()
# line 80
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.001, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 86
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 92
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=15000)
# line 100
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=250)
# line 111
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 113
MY_CYCLE.start()
# line 116
for i in range(2):
# line 119
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 125
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 130
t.sleep(60)
# line 132
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 134
MY_CYCLE.start()
# line 135
t.sleep(120)
```

## CaiaBirthday_MinnieMouse_lights.py

[Source](../CaiaBirthday_MinnieMouse_lights.py)

```python
# line 9
NUM_LED = 480
# line 11
colorList = [0xCCCC33, 0x77FF00]
# line 18
if begin_time < end_time:
# line 25
while True:
# line 28
if True:
# line 44
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFF0000, fade_time = 1, num_cycles=200)
# line 50
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 57
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 63
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=.025, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 69
for i in range(2):
# line 72
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.001, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 75
MY_CYCLE.start()
# line 79
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.001, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 85
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.05, num_steps_per_cycle=1, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 0, num_cycles=1)
# line 91
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=15000)
# line 99
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =colorList[random.randint(0, len(colorList) - 1)], color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=250)
# line 110
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=1, color = colorList[random.randint(0, len(colorList) - 1)], global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=300)
# line 112
MY_CYCLE.start()
# line 115
for i in range(2):
# line 118
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 124
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, len(colorList) - 1)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 129
t.sleep(60)
# line 131
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 133
MY_CYCLE.start()
# line 134
t.sleep(120)
```

## Seahawks.py

[Source](../Seahawks.py)

```python
# line 8
NUM_LED =480
# line 15
if begin_time < end_time:
# line 22
while True:
# line 27
if True:
# line 30
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 32
MY_CYCLE.start()
# line 36
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 38
MY_CYCLE.start()
# line 41
for i in range(40):
# line 44
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 46
MY_CYCLE.start()
# line 50
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.005, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 52
MY_CYCLE.start()
# line 57
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=30000)
# line 61
for i in range(50):
# line 63
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=1000)
# line 65
MY_CYCLE.start()
# line 66
t.sleep(.2)
# line 70
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 72
MY_CYCLE.start()
# line 76
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 3, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=15000)
# line 78
MY_CYCLE.start()
# line 87
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.03, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=1500)
# line 89
MY_CYCLE.start()
# line 93
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
# line 95
MY_CYCLE.start()
# line 96
t.sleep(120)
```

## SeahawksDay.py

[Source](../SeahawksDay.py)

```python
# line 9
NUM_LED = 480
# line 10
colorList = [0x0000FF, 0x00FF00, 0x00FF00, 0x0000FF]
# line 17
if begin_time < end_time:
# line 24
while True:
# line 26
if True:
# line 31
for i in range(2):
# line 34
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 36
MY_CYCLE.start()
# line 40
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.002, num_steps_per_cycle=82, color = [colorList[random.randint(0, 2)]], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 42
MY_CYCLE.start()
# line 45
t.sleep(60)
# line 47
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                            num_cycles=1)
# line 49
MY_CYCLE.start()
# line 50
t.sleep(120)
```

## clear.py

[Source](../clear.py)

```python
# line 1
NUM_LED = 1024
# line 8
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=10)
# line 10
MY_CYCLE.start()
```

## sample.py

[Source](../sample.py)

```python
# line 7
apa102.APA102(num_led=42, global_brightness=20, mosi = 10, sclk = 11,
                                  order='rbg')
# line 22
time.sleep(20)
```

## runcolorcycle.py

[Source](../runcolorcycle.py)

```python
# line 5
NUM_LED = 144
# line 9
colorschemes.Solid(num_led=NUM_LED, pause_value=3,
                             num_steps_per_cycle=1, num_cycles=1)
# line 15
colorschemes.RoundAndRound(num_led=NUM_LED, pause_value=.008,
                                     num_steps_per_cycle=NUM_LED, num_cycles=3)
# line 17
MY_CYCLE.start()
# line 21
colorschemes.StrandTest(num_led=NUM_LED, pause_value=1,
                                  num_steps_per_cycle=NUM_LED, num_cycles=3)
# line 27
colorschemes.Rainbow(num_led=NUM_LED, pause_value=0,
                               num_steps_per_cycle=255, num_cycles=5)
# line 29
MY_CYCLE.start()
# line 33
colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=5)
# line 35
MY_CYCLE.start()
```

## runcolorcycle_blinkt.py

[Source](../runcolorcycle_blinkt.py)

```python
# line 5
NUM_LED = 8
# line 6
MOSI = 23
# line 7
SCLK = 24
# line 11
colorschemes.Solid(num_led=NUM_LED, pause_value=1, order = 'rgb',
                             num_steps_per_cycle=4, num_cycles=1, mosi=MOSI, sclk=SCLK)
# line 13
MY_CYCLE.start()
# line 17
colorschemes.Rainbow(num_led=NUM_LED, pause_value=0, order = 'rgb',
                               num_steps_per_cycle=255, num_cycles=5, mosi=MOSI, sclk=SCLK)
# line 19
MY_CYCLE.start()
```

## test.py

[Source](../test.py)

```python
# line 8
NUM_LED = 120
# line 15
if begin_time < end_time:
# line 22
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1000)
# line 28
colorschemes.Solid(num_led=NUM_LED, pause_value=1,
                             num_steps_per_cycle=1, num_cycles=1)
# line 36
colorschemes.ChristmasTest(num_led=NUM_LED, pause_value=0.01,
                                  num_steps_per_cycle=NUM_LED, num_cycles=10)
# line 43
colorschemes.Solid(num_led=NUM_LED, pause_value=3,
                             num_steps_per_cycle=1, num_cycles=1)
# line 49
colorschemes.RoundAndRound(num_led=NUM_LED, pause_value=0,
                                     num_steps_per_cycle=NUM_LED, num_cycles=2)
# line 55
colorschemes.StrandTest(num_led=NUM_LED, pause_value=0.04,
                                  num_steps_per_cycle=NUM_LED, color=0x000000,num_cycles=3)
# line 61
colorschemes.Rainbow(num_led=NUM_LED, pause_value=0,
                               num_steps_per_cycle=255, num_cycles=10)
# line 68
colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.1,
                                    num_steps_per_cycle=35,  num_cycles=50)
# line 93
for i in range(0, 1):
# line 97
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xFF05AA, global_brightness = 128, num_cycles=1000)
# line 101
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF61288, global_brightness = 20, num_cycles=1000)
# line 105
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF61288, global_brightness = 20, num_cycles=1000)
# line 109
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 80, global_brightness = 20, \
                                      blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 5, num_cycles=5000)
# line 114
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color = 0xFFFFFF, global_brightness = 100, blink_factor = 100, \
                                      blink_color = 0xFFFFFF, fade_time = .05, num_cycles=2500)
# line 119
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=5000)
# line 123
colorschemes.Scanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.1, num_steps_per_cycle=50, color = [0xFF0000, 0x0000FF], global_brightness = 100, blink_factor = 500, blink_color = 0xFFFFAA, \
                                    length = 10, fade_tail = 1, snake_separation = 0, num_cycles=2)
# line 127
for i in range(225):
# line 130
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 136
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 142
colorschemes.PulseRefresh(num_led=NUM_LED, pause_value=0.05, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF], global_brightness = 100, blink_factor = 500, blink_color = 0xFFFFAA, \
                                    length = 5, fade_tail = 1, snake_separation = -1, num_cycles=2)
# line 149
colorschemes.Carnival(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=30, color = [0xFF0000, 0x0000FF, 0xFF0699], global_brightness = 100, \
                                    length = 3, fade_tail = 0, snake_separation = 3, rotate = 0, num_cycles=50)
# line 154
colorschemes.Carnival(num_led=NUM_LED, pause_value=0.08, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF, 0xFF0699], global_brightness = 100, \
                                    length = 3, fade_tail = 1, snake_separation = 3, rotate = 1, num_cycles=1)
# line 159
colorschemes.Carnival(num_led=NUM_LED, pause_value=0.08, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF, 0xFF0699, 0x00FF00], global_brightness = 100, \
                                    length = 3, fade_tail = 1, snake_separation = 3, rotate = 1, num_cycles=3)
# line 166
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                      led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=90000)
# line 177
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                      blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=800)
# line 186
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0x0000FF, global_brightness = 128, num_cycles=1000)
# line 191
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xFF0000, global_brightness = 128, num_cycles=1000)
# line 210
while True:
# line 212
if is_time_between(time(15, 33), time(9, 0)):
# line 214
for i in range(255):
# line 217
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 219
MY_CYCLE.start()
# line 223
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                    length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 225
MY_CYCLE.start()
# line 229
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 2, pause_value=0.005, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 100, global_brightness = 20, \
                                           fade_time = 1, num_cycles=5000)
# line 231
MY_CYCLE.start()
# line 234
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                          led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=90000)
# line 236
MY_CYCLE.start()
# line 245
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                          blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=800)
# line 247
MY_CYCLE.start()
# line 251
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
# line 253
MY_CYCLE.start()
# line 254
t.sleep(60)
# line 268
colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=50)
# line 277
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
# line 279
MY_CYCLE.start()
```

## 20181212/test.py

[Source](../20181212/test.py)

```python
# line 6
NUM_LED = 144
# line 10
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1000)
# line 16
colorschemes.Solid(num_led=NUM_LED, pause_value=1,
                             num_steps_per_cycle=1, num_cycles=1)
# line 24
colorschemes.ChristmasTest(num_led=NUM_LED, pause_value=0.01,
                                  num_steps_per_cycle=NUM_LED, num_cycles=10)
# line 31
colorschemes.Solid(num_led=NUM_LED, pause_value=3,
                             num_steps_per_cycle=1, num_cycles=1)
# line 37
colorschemes.RoundAndRound(num_led=NUM_LED, pause_value=0,
                                     num_steps_per_cycle=NUM_LED, num_cycles=2)
# line 43
colorschemes.StrandTest(num_led=NUM_LED, pause_value=0.04,
                                  num_steps_per_cycle=NUM_LED, color=0x000000,num_cycles=3)
# line 49
colorschemes.Rainbow(num_led=NUM_LED, pause_value=0,
                               num_steps_per_cycle=255, num_cycles=10)
# line 56
colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.1,
                                    num_steps_per_cycle=35,  num_cycles=50)
# line 81
for i in range(0, 1):
# line 85
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xFF05AA, global_brightness = 128, num_cycles=1000)
# line 89
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF61288, global_brightness = 20, num_cycles=1000)
# line 93
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF61288, global_brightness = 20, num_cycles=1000)
# line 97
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xF00E80, color_brightness = 80, global_brightness = 20, \
                                      blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 5, num_cycles=5000)
# line 102
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color = 0xFFFFFF, global_brightness = 100, blink_factor = 100, \
                                      blink_color = 0xFFFFFF, fade_time = .05, num_cycles=2500)
# line 107
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=5000)
# line 111
colorschemes.Scanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.1, num_steps_per_cycle=50, color = [0xFF0000, 0x0000FF], global_brightness = 100, blink_factor = 500, blink_color = 0xFFFFAA, \
                                    length = 10, fade_tail = 1, snake_separation = 0, num_cycles=2)
# line 115
for i in range(225):
# line 118
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 124
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 130
colorschemes.PulseRefresh(num_led=NUM_LED, pause_value=0.05, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF], global_brightness = 100, blink_factor = 500, blink_color = 0xFFFFAA, \
                                    length = 5, fade_tail = 1, snake_separation = -1, num_cycles=2)
# line 137
colorschemes.Carnival(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=30, color = [0xFF0000, 0x0000FF, 0xFF0699], global_brightness = 100, \
                                    length = 3, fade_tail = 0, snake_separation = 3, rotate = 0, num_cycles=50)
# line 142
colorschemes.Carnival(num_led=NUM_LED, pause_value=0.08, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF, 0xFF0699], global_brightness = 100, \
                                    length = 3, fade_tail = 1, snake_separation = 3, rotate = 1, num_cycles=1)
# line 147
colorschemes.Carnival(num_led=NUM_LED, pause_value=0.08, num_steps_per_cycle=100, color = [0xFF0000, 0x0000FF, 0xFF0699, 0x00FF00], global_brightness = 100, \
                                    length = 3, fade_tail = 1, snake_separation = 3, rotate = 1, num_cycles=3)
# line 154
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                      led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=90000)
# line 165
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                      blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=800)
# line 174
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0x0000FF, global_brightness = 128, num_cycles=1000)
# line 179
colorschemes.ColorFade(num_led=NUM_LED, pause_value=0.001, num_steps_per_cycle=1, color =0xFF0000, global_brightness = 128, num_cycles=1000)
# line 198
while True:
# line 200
for i in range(225):
# line 203
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0xFF0000], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 205
MY_CYCLE.start()
# line 209
colorschemes.CollapseScanner(num_led=NUM_LED, led_multiplier = 1, pause_value=0.02, num_steps_per_cycle=82, color = [0x0000FF], global_brightness = 100, \
                                                length = math.floor(NUM_LED / 2), fade_tail = 1, snake_separation = 10, num_cycles=1)
# line 211
MY_CYCLE.start()
# line 216
colorschemes.Twinkle(num_led=NUM_LED, pause_value=0.01, num_steps_per_cycle=1, color =0xFF1699, color_brightness = 100, global_brightness = 100, \
                                      led_multiplier = 2, blink_factor = 200, blink_color = 0xFFFFFF, fade_time = 1, num_cycles=90000)
# line 218
MY_CYCLE.start()
# line 227
colorschemes.ColorFade(num_led=NUM_LED, led_multiplier = 1, pause_value=0.15, num_steps_per_cycle=1, color = 0x000000, global_brightness = 100, \
                                      blink_factor = 1, blink_color = 0xFFFFAA, num_cycles=800)
# line 229
MY_CYCLE.start()
# line 245
colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=50)
# line 254
colorschemes.Scanner(num_led=NUM_LED, pause_value=0.1, num_steps_per_cycle=1, color = [0x000000], global_brightness = 100,  \
                                    num_cycles=1)
# line 256
MY_CYCLE.start()
```

## Local effect framework

`colorschemes/colorschemes.py` defines StrandTest, ChristmasTest, TheaterChase, RoundAndRound, Solid, Rainbow, ColorFade, Scanner, PulseRefresh, Carnival, Twinkle, and CollapseScanner. They subclass the bundled ColorCycleTemplate and update strip buffers directly. ColorFade/Twinkle derive fade behavior from pause/cycle settings; Scanner/CollapseScanner use lengths/tails/separations. These effects have not been ported to hardware-free frames. A TODO remains in the driver's LED multiplier handling; do not infer uniform multiplier support from constructor arguments alone.

[Architecture](architecture.md) explains lifecycle and dependency boundaries. Backups and inherited photos are historical references, not validated deployment assets.
