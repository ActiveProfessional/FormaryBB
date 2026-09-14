# Examples

`lakeside-roasters/` is a **frozen synthetic example** — a demo business created to show
what a working repo looks like after a first session: profile from intake, P0 gate
passed with user approval recorded, one task in flight with a work order drafted, one
blocking question answered on record. None of its facts are real.

Use it to:

- See "what good looks like" before filling a real profile.
- Onboard a new model: paste `README.md` + `harness/PHASES.md`, then run
  `python3 bin/foundry.py rollup examples/lakeside-roasters` and work from there.

The CLI accepts paths, so every command works against the example directly
(e.g. `python3 bin/foundry.py status examples/lakeside-roasters`). Real businesses live
in `businesses/` and are created with `init`.