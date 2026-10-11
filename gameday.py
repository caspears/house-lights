"""Shared game-day effects: Windows preview or existing APA102 hardware."""
import argparse
import math
import signal
import time

EFFECTS = ('wave', 'comet', 'sparkle', 'touchdown')
TEST_EFFECT = 'color-test'
BLUE = (0, 35, 120)
GREEN = (70, 255, 0)


def mix(a, b, amount):
    return tuple(round(x + (y - x) * amount) for x, y in zip(a, b))


def frame(effect, seconds, count=480, brightness=0.25, speed=1.0):
    """Return RGB values without importing hardware or GUI dependencies."""
    if effect not in EFFECTS + (TEST_EFFECT,):
        raise ValueError('Unknown effect: ' + effect)
    if count < 1 or not 0 <= brightness <= 1 or speed <= 0:
        raise ValueError('Invalid LED count, brightness, or speed')
    t = seconds * speed
    if effect == TEST_EFFECT:
        color = ((255, 0, 0), (0, 255, 0), (0, 0, 255))[int(seconds // 4) % 3]
        return [tuple(round(c * brightness) for c in color)] * count
    pixels = []
    for i in range(count):
        x = i / max(1, count - 1)
        if effect == 'wave':
            color = mix(BLUE, GREEN, (1 + math.sin(2 * math.pi * (x * 2 - t / 9))) / 2)
        elif effect == 'comet':
            distance = (t / 7 - x) % 1
            color = mix((0, 3, 20), GREEN, max(0, 1 - distance / 0.16) ** 2)
        elif effect == 'sparkle':
            pulse = max(0, math.sin(t * (1.1 + (i * 37 % 19) / 20) + i * 2.399)) ** 40
            color = mix((0, 8, 40), (220, 255, 220) if i % 3 else GREEN, pulse)
        else:
            distance = abs(x - 0.5) * 2
            radius = (t % 5) / 3
            pulse = max(0, 1 - abs(distance - radius) / 0.18)
            color = mix(BLUE, GREEN, pulse)
        pixels.append(tuple(round(c * brightness) for c in color))
    return pixels


def selected(effect, elapsed):
    return EFFECTS[int(elapsed // 30) % len(EFFECTS)] if effect == 'playlist' else effect


def preview(args):
    from game_show import Show, DEMO_TOUCHDOWN, DEMO_FIELD_GOAL, DEMO_FINAL
    import tkinter as tk
    from tkinter import ttk
    root = tk.Tk()
    root.title('House lights | 480 LED game-day preview')
    root.geometry('1160x650')
    root.configure(bg='#081321')
    controls = ttk.Frame(root, padding=12)
    controls.pack(fill='x')
    effect = tk.StringVar(value=args.effect)
    ttk.Label(controls, text='Effect').pack(side='left')
    ttk.Combobox(controls, textvariable=effect, values=('playlist',) + EFFECTS + (TEST_EFFECT,),
                 state='readonly', width=14).pack(side='left', padx=10)
    brightness = tk.DoubleVar(value=args.brightness)
    speed = tk.DoubleVar(value=args.speed)
    for label, variable, low, high in [('Brightness', brightness, 0, 1), ('Speed', speed, .1, 3)]:
        ttk.Label(controls, text=label).pack(side='left', padx=10)
        ttk.Scale(controls, variable=variable, from_=low, to=high, length=160).pack(side='left')
    paused = tk.BooleanVar(value=False)
    ttk.Checkbutton(controls, text='Pause', variable=paused).pack(side='left', padx=12)
    show = Show(args)
    elapsed, previous = 0.0, time.monotonic()
    if args.demo:
        demo_controls = ttk.Frame(root, padding=6)
        demo_controls.pack(fill='x')
        def jump(value):
            nonlocal elapsed
            elapsed = value
            show.motion = 0
            show.previous = None
        for title, value in [('Restart buildup', 0), ('Kickoff', 60), ('Touchdown', DEMO_TOUCHDOWN), ('Field goal', DEMO_FIELD_GOAL), ('Final', DEMO_FINAL)]:
            ttk.Button(demo_controls, text=title, command=lambda v=value: jump(v)).pack(side='left', padx=4)
        outcome = tk.StringVar(value=args.demo_outcome)
        ttk.Label(demo_controls, text='Ending').pack(side='left', padx=8)
        ttk.Combobox(demo_controls, textvariable=outcome, values=('win','loss','tie'), state='readonly', width=7).pack(side='left')
    if args.demo or args.live:
        # The game controller chooses effects; keep speed and brightness available.
        for widget in controls.winfo_children():
            if isinstance(widget, ttk.Combobox):
                widget.configure(state='disabled')
    canvas = tk.Canvas(root, bg='#081321', highlightthickness=0, width=1140, height=540)
    canvas.pack(fill='both', expand=True)
    canvas.create_text(570, 35, text='SEAHAWKS • GAME DAY', fill='#c5edff', font=('Arial', 24, 'bold'))
    canvas.create_polygon(190, 210, 950, 210, 950, 445, 190, 445, fill='#142438', outline='#263d55')
    canvas.create_polygon(80, 150, 1060, 150, 950, 280, 190, 280, fill='#1e3043', outline='#354a60')
    roof, strip = [], []
    # Approximate geometry: 15% left edge, 70% front, 15% right edge.
    for i in range(args.leds):
        u = i / max(1, args.leds - 1)
        if u < .15:
            p = u / .15
            x, y = 190 - 110 * p, 280 - 130 * p
        elif u < .85:
            x, y = 80 + 980 * (u - .15) / .7, 150
        else:
            p = (u - .85) / .15
            x, y = 1060 - 110 * p, 150 + 130 * p
        roof.append(canvas.create_oval(x-2, y-2, x+2, y+2, outline=''))
        x = 60 + 1020 * u
        strip.append(canvas.create_rectangle(x, 490, x + max(1, 1020 / args.leds), 505, outline=''))
    status = canvas.create_text(570, 555, text='', fill='#c5edff', font=('Arial', 11))
    canvas.create_text(570, 465, text='LED 0 → full strip → LED {}'.format(args.leds-1), fill='#a2b6c9')
    def tick():
        nonlocal elapsed, previous
        now = time.monotonic()
        if not paused.get():
            elapsed += now - previous
        previous = now
        args.effect = effect.get()
        if args.demo:
            args.demo_outcome = outcome.get()
        pixels, name = show.render(elapsed, brightness.get(), speed.get())
        for a, b, rgb in zip(roof, strip, pixels):
            color = '#{:02x}{:02x}{:02x}'.format(*rgb)
            canvas.itemconfigure(a, fill=color)
            canvas.itemconfigure(b, fill=color)
        canvas.itemconfigure(status, text='{} | {} LEDs | brightness {:.0%} | approximate roof mapping'.format(name, args.leds, brightness.get()))
        root.after(round(1000 / args.fps), tick)
    try:
        tick()
        root.mainloop()
    finally:
        show.close()


def hardware(args):
    from game_show import Show
    from driver.apa102 import APA102
    strip = APA102(num_led=args.leds, led_multiplier=1, global_brightness=31,
                   order=args.order, mosi=10, sclk=11)
    running = True
    def stop(*_):
        nonlocal running
        running = False
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    start = time.monotonic()
    show = Show(args)
    previous_label = None
    try:
        while running:
            now = time.monotonic()
            elapsed = now - start
            if args.duration and elapsed >= args.duration:
                break
            pixels, label = show.render(elapsed, args.brightness, args.speed)
            if label != previous_label:
                print(label, flush=True)
                previous_label = label
            for i, rgb in enumerate(pixels):
                strip.set_pixel(i, *rgb)
            strip.show()
            time.sleep(max(0, 1 / args.fps - (time.monotonic() - now)))
    finally:
        show.close()
        try:
            strip.clear_strip()
        finally:
            strip.cleanup()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hardware', action='store_true', help='Drive Pi LEDs; default is Windows preview')
    parser.add_argument('--effect', choices=('playlist',) + EFFECTS + (TEST_EFFECT,), default='playlist')
    parser.add_argument('--leds', type=int, default=480)
    parser.add_argument('--brightness', type=float, default=1.0, help='0 to 1; default is full brightness')
    parser.add_argument('--speed', type=float, default=1)
    parser.add_argument('--fps', type=int, default=30)
    parser.add_argument('--order', choices=('rgb','rbg','grb','gbr','brg','bgr'), default='rgb')
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--demo', action='store_true', help='Compressed game-day story with simulated scoring')
    modes.add_argument('--live', action='store_true', help='Experimental ESPN score feed')
    parser.add_argument('--demo-outcome', choices=('win','loss','tie'), default='win')
    parser.add_argument('--game-date', help='Game date YYYY-MM-DD; required for live mode')
    parser.add_argument('--event-id', help='Optional explicit ESPN event ID instead of schedule lookup')
    parser.add_argument('--poll', type=int, default=15, help='Feed polling interval in seconds, minimum 15')
    parser.add_argument('--celebration-delay', type=float, default=0, help='Additional seconds to align celebrations with delayed TV')
    parser.add_argument('--duration', type=float, default=0, help='Hardware runtime in seconds; 0 runs until stopped')
    args = parser.parse_args()
    if args.live:
        import datetime
        if not args.game_date:
            parser.error('--live requires --game-date YYYY-MM-DD')
        try:
            datetime.datetime.strptime(args.game_date, '%Y-%m-%d')
        except ValueError:
            parser.error('--game-date must be YYYY-MM-DD')
    if args.poll < 15 or args.celebration_delay < 0:
        parser.error('Polling must be at least 15 seconds; celebration delay must be nonnegative')
    if args.leds < 1 or not 0 <= args.brightness <= 1 or args.speed <= 0 or not 1 <= args.fps <= 120 or args.duration < 0:
        parser.error('Check LED count, brightness (0–1), speed (>0), FPS (1–120), and duration (>=0)')
    (hardware if args.hardware else preview)(args)


if __name__ == '__main__':
    main()
