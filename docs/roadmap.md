# Future plans

Everything below is proposed work, not implemented functionality. This is a multi-event lighting project; game day is one program among holidays, birthdays, and other activities.

## Program selection through Home Assistant

Provide a simple selector such as Off, Christmas Lights, New Years Lights, Game Day, Halloween, and approved additional programs. A named registry should map approved program names to runnable implementations. One supervisor should own the strip, stop/clean up the previous program, and report failures honestly. Refactor legacy loops for graceful switching, common brightness/order settings, and eventually shared-frame preview.

MQTT Select is the proposed integration. No broker credentials, discovery, HA entities/YAML, or supervisor exist here. Report requested selection separately from confirmed running state where appropriate, plus controller availability/heartbeat. Running process state does not prove physical light output.

## Pi monitoring and operation

Add a managed service with restart policy, logs, repeatable deployment and rollback. Report Pi/controller availability and actual current program; choose optional health metrics and alert thresholds later. Validate disconnects, crash/restart recovery, single-writer ownership, and dependency compatibility before relying on unattended operation.

## Dedicated Google Calendar

Use a dedicated calendar, suggested name **House Lights**, separate from the family calendar. Only that lighting calendar should drive programs. No calendar has been created or connected. Proposed HA start/end automations map approved event titles (Christmas Lights, Halloween, Game Day) to programs. Game Day activation must allow the two-hour pregame window; live data drives scoring/final behavior, with an optional explicit calendar cutoff.

Decide overlap priorities, event-end behavior (off/restore), manual override lifetime, an explicit Follow Schedule control, and restart/outage reconciliation. An older event ending must not turn off a newer or manually selected program. Define timezone, daylight-saving, all-day and recurring holiday semantics, plus behavior when calendar or MQTT is unavailable.

## Validation and missing decisions

First validate the updated Pi show after byte decoding, a complete demo, real scoring/finals, daytime visibility and prolonged feed recovery. Record Pi Python/OS/dependencies, physical routing/electrical details and destination repository URL. Add durable scoring history/replay-age rules if needed. Smooth the kickoff speed change only as a later behavior change. Decide which legacy variants are canonical; filenames/comments do not establish the intended palette.

When implementing integrations, recheck official [MQTT Select](https://www.home-assistant.io/integrations/select.mqtt/), [MQTT](https://www.home-assistant.io/integrations/mqtt/), and [Google Calendar](https://www.home-assistant.io/integrations/google/) documentation. These links are planning references; no integration was tested here.
