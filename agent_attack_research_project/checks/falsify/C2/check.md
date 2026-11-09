# C2 falsification — 2026-11-07

## Verdict

**REFUTED for the preregistered narrative/adjacency hypothesis.** The local-gateway pilot did not show a
narrative advantage over random order, and the bridge-swap mechanism control was higher than narrative.

## Checks run

- `python3 -I pilots/I1-memory-cascade/analyze_real_probe.py --expected 150` → all 150 records parsed and utility-valid.
- `python3 -I checks/falsify/C2/check.py` → exit 0 with C2 REFUTED.
- clean: 0/30;
- chronological: 5/30;
- narrative: 17/30 = 56.7% [39.2, 72.6];
- random: 14/30 = 46.7% [30.2, 63.9];
- bridge_swap: 23/30 = 76.7% [59.1, 88.2];
- paired narrative versus random: narrative-only=9, random-only=6, exact McNemar p=0.607239;
- parse/utility rate: 30/30 in every arm;
- local-truth oracle: 150/150;
- estimated pilot cost: $0.0757 under the $50 cap.

## Interpretation

The model route reliably produced structured answers and distinguished the clean arm, but the planned causal
mechanism did not survive the bridge-swap control. The high bridge-swap rate indicates sensitivity to the presence
and direction of the AB/BC statements or to surface semantics, rather than the preregistered adjacency mechanism.
The direction observation is post hoc and exploratory; it is not promoted to a new claim without a fresh idea,
pre-registration and a new control matrix.

## Consequence

Do not run memory or downstream aggregation blocks for I1. Keep the raw run and negative result. A future idea may
study order direction or semantic composition, but it must be registered separately and compared against C18 and
other prior work before execution.
