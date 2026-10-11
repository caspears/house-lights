# Architecture

## Shared-frame runner

`gameday.py` owns argument parsing, pure RGB frame generation, Tk preview, and APA102 output. `game_show.py` owns scene selection, demo timing, spark/ring overlays, ESPN parsing, and background polling. `Show.render()` produces the same list of RGB tuples for preview and hardware.

Ordinary mode selects an effect directly or from the playlist. Demo mode selects simulated scenes. Live mode creates a daemon `Feed` thread that retrieves a scoreboard event ID if needed, polls its summary, publishes a locked snapshot, and queues newly identified scoring events. Rendering reads the snapshot without waiting for HTTP. Render motion integrates changing speed; UTC wall time drives live pregame status, while monotonic time measures feed age and animation timing.

Tk is imported only by preview. The hardware driver is imported only by hardware output. The new rendering/feed modules use the standard library; hardware still imports the bundled driver and its Adafruit dependencies. Feed close signals stop but does not join an in-flight request (HTTP timeout is eight seconds).

Hardware creates APA102 with LED multiplier 1, global brightness 31, configured RGB order, and pins 10/11. Each frame sets all pixels then calls `show()`. SIGINT/SIGTERM request loop exit; the output loop's `finally` closes the show, clears the strip, and closes SPI. Forced termination or power loss cannot run cleanup. Initialization failures before the loop's `try` are not covered by that cleanup guarantee.

## Legacy path

Event scripts ? local `colorschemes/colorschemes.py` ? `ColorCycleTemplate.start()` ? APA102 driver. Effects update the strip directly instead of returning shared RGB frames. Template defaults include `order='rbg'`, `num_cycles=-1` (unlimited), and global brightness 255 (driver clamps above 31). `start()` sleeps `pause_value` per step, clears/cleans up on normal completion or KeyboardInterrupt, and has no equivalent common SIGTERM supervisor.

There is currently no common program registry, process ownership lock, persistent event store, configuration file, HA/MQTT integration, calendar adapter, or service definition. Only one writer should access the strip. See [roadmap](roadmap.md) for the proposed migration.
