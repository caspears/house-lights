# Raspberry Pi deployment

These are operator instructions, not actions performed by this documentation task. Preserve the known working scripts and environment. Confirm the actual user, host, path, interpreter and permissions before using the recorded examples.

## Limited update to the existing installation

Back up the Pi's existing `gameday.py` and `game_show.py` together, if present, before copying. From Windows:

```powershell
scp gameday.py game_show.py pi@10.0.0.124:/home/pi/Development/APA102_Pi/
```

Stop the current lighting writer gracefully and confirm it exited. Copying files does not update a running process. On the Pi, using the known working interpreter and permissions:

```bash
cd /home/pi/Development/APA102_Pi
python3 --version
python3 gameday.py --hardware --effect color-test --brightness 0.15 --duration 12
python3 gameday.py --hardware --demo --brightness 1 --duration 220
```

The color test is red, green, blue, four seconds each. RGB order was physically reported correct; full updated controller operation remains unverified. Confirm the preview's selected game and score before running live hardware:

```bash
python3 gameday.py --hardware --live --game-date 2026-10-11 --brightness 1
```

This date is a dated example, not recurring scheduling. Maintain a synchronized Pi clock. Use Ctrl+C to stop and clear. A Pi desktop terminal accessed through VNC can stay open after VNC disconnects; a foreground SSH process may terminate on disconnect. No systemd service or session manager is supplied.

## New repository and repeatable deployment (proposed workflow)

The accessible new repository URL is not yet supplied. The handoff records `orgin` pointing at medinuity/piLights and `origin` pointing at tinue/APA102_Pi; do not assume either is the intended new destination. No remote edits, push, or deployment are part of this documentation change.

Review local edits/untracked scripts, retain LICENSE and attribution, and exclude credentials, virtual environments, and recursive Python caches before committing. The working tree currently has a deleted `.gitignore`; review that separately rather than assuming caches are ignored.

Once the destination exists, use a separate Pi checkout initially, leaving `/home/pi/Development/APA102_Pi` available as a fallback. Record the reviewed commit and dependency environment; validate preview/tests, then stop the old writer and run the selected version manually. Fresh-install compatibility and automated deployment are pending. Do not copy Windows environments or auto-update during a game.

For rollback, stop the new writer, restore both backed-up game modules as a matched pair (or return to the recorded known-good checkout), then restart the prior command/environment. Record the command, revision, configuration and observed result. No rollback automation currently exists.
