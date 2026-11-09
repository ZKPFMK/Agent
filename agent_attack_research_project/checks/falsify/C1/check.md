# C1 falsification — 2026-11-07

## Verdict

**WEAKENED.** The raw mock harness supports a synthetic order-sensitive effect, but it cannot support a claim
about a real LLM agent because the `MockBackend` policy explicitly assigns a high probability to `A->C` when
`AB` and `BC` are adjacent.

## Checks run

- `python3 -I pilots/I1-memory-cascade/run_probe.py` → 120 records, 4 arms × 10 episodes × 3 seeds.
- `python3 -I pilots/I1-memory-cascade/analyze_probe.py` → recomputed rates from `trials.jsonl`.
- Local truth oracle: 120/120 records pass.
- Utility invariant: 120/120 records pass.
- Narrative vs random: 21 narrative-only and 2 random-only discordant pairs; exact McNemar p=0.000066.
- Bridge-swap control: 4/30 successes versus narrative 25/30; the surface-matched intervention removes the
  adjacent bridge in the synthetic policy.
- Chronological control: 1/30 successes; same fragment set and budget.

## Confounds and limits

- The mock policy is the mechanism under test, so the effect is a harness and evaluator check, not a model result.
- `hash()` is not used for seeding; arm offsets are fixed in `run_probe.py` so reruns are deterministic.
- No memory, downstream Agent, external model, network, real evidence or real secret was used.

## Adopted wording

> In the deterministic synthetic `MockBackend` harness used for R5, an order containing adjacent `AB` and `BC`
> fragments produced more `A->C` false-edge probes than the matched random, chronological and bridge-swap arms
> under the same synthetic facts and task budget. This result validates the probe plumbing only; it does not
> establish the effect in a real LLM or Agent framework.

Next falsifier target: before any real-model run, replace the encoded policy with a local model or an independent
agent implementation and preserve the same paired controls. If that cannot be done within the declared budget,
file C1 as a harness-only boundary result and stop the direction.
