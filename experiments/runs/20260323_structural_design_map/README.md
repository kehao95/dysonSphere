# Experiment: 20260323_structural_design_map

## Goal

Couple the exact displaced-orbit angle limit, explicit node-structure scaling,
and ideal Dyson Swarm / Dyson Ring benchmarks into one reusable design map.

The central question is no longer just "is 1° feasible?" but:

> For a given angle and structure model, what node power is required to retain a
> target fraction of the ideal same-shell Dyson energy limit?

## Method

- Hold the benchmark clean:
  - same stellar luminosity
  - same orbital radius
  - same ideal PV physics
  - no aging, thermal degradation, maintenance, or control losses for any concept
- Use the exact ideal-sail displaced-orbit constraint to obtain
  $\sigma_{\max}(\phi)$.
- Use the geometry-explicit structure model from `models/structural/geometry.py`.
- Solve two complementary problems:
  - given $(\phi, P)$, what fill factor $\lambda$ is achievable?
  - given $(\phi, \lambda)$, what minimum node power is required?

For same-efficiency comparisons:

$$\frac{P_{\text{MDDS}}}{P_{\text{swarm}}} = \lambda$$

and the same ratio maps to an equivalent ideal Dyson-Ring half-angle:

$$\psi_{\text{eq}} = \arcsin(\lambda)$$

## Headline Findings

For the optimistic `cross_light` structure model:

- at $1^\circ$:
  - 10% of an ideal same-efficiency Swarm requires about 3.13 kW per node
  - 25% requires about 15.95 kW
  - 50% requires about 2.67 MW
- at $2^\circ$:
  - 1% requires about 1.03 kW
  - 5% requires about 7.52 kW
  - 10% requires about 28.45 kW
  - 25% is infeasible for the current `CP1 + ultralight tandem` material pair

Fixed node power tells the same story:

- a 10 kW `cross_light` node reaches about 20.3% of an ideal same-efficiency
  Swarm at $1^\circ$ (equivalent ideal Ring half-angle $\approx 11.73^\circ$)
- the same 10 kW node falls to about 5.98% at $2^\circ$
- a 10 kW `cross_light` node can preserve 10% only out to about $1.53^\circ$
  and 25% only out to about $0.873^\circ$
- even 100 kW only pushes those limits to about $2.46^\circ$ and $1.41^\circ$

Interpretation:

- sub-degree to roughly 1°–1.5° is the credible high-value regime for current
  source-backed ultralight materials
- multi-degree rings remain possible mainly when the acceptable energy fraction
  is modest
- node granularity and structural scaling are now central design variables, not
  secondary implementation details

## Artifacts

- `results/design_grid.csv`
- `results/power_thresholds_by_angle.csv`
- `results/angle_thresholds_by_power.csv`
- `results/summary.json`
