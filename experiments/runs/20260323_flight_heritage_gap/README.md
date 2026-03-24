# Experiment: 20260323_flight_heritage_gap

## Goal

Benchmark real solar-sail flight systems against the exact MDDS areal-density
limits, so the paper can distinguish clearly between:

- sail-material plausibility
- deployable-boom plausibility
- full integrated spacecraft plausibility

## Method

- Take source-backed deployed area and total mass values from NASA ACS3 and NEA
  Scout publications.
- Convert each case to deployed areal density and lightness number.
- Map each case into the exact MDDS maximum-angle relation.
- For ACS3, also decompose the system into:
  - total spacecraft
  - sail-boom subsystem
  - bus only
  - membrane plus booms only

This lets us see which part of the present-day solar-sail system stack is
actually preventing 1°-class MDDS operation.

## Headline Findings

- ACS3 total system:
  - deployed areal density `200 g/m²`
  - effective `β ≈ 0.00765`
  - exact MDDS maximum angle only about `0.169°`
  - would need about `5.92x` mass reduction to reach `1°`
- NEA Scout total system:
  - deployed areal density `162.8 g/m²`
  - exact MDDS maximum angle about `0.207°`
  - would need about `4.82x` mass reduction to reach `1°`
- ACS3 membrane plus booms only:
  - deployed areal density `12.45 g/m²`
  - exact MDDS maximum angle about `2.71°`
  - if used as a reflector-only heritage benchmark, it still leaves enough
    margin at `1°` for about `λ ≈ 0.389` of ultralight tandem PV

Interpretation:

- current flight-demonstrated sailcraft validate deployable sail technology
- but current integrated spacecraft overhead still dominates the areal-density
  budget
- the strongest system-level gap is no longer the membrane itself, but the
  spacecraft bus / deployment / control stack carried behind it

## Artifacts

- `results/heritage_gap.csv`
- `results/summary.json`
