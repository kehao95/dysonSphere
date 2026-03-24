# Experiment: 20260323_fixed_bus_budget

## Goal

Turn the source-backed ACS3 boom and bus data into a direct engineering
threshold:

> Once angle, node power, and target shell-relative utilization are fixed, how
> much non-scaling bus / deployment / control mass can the node still carry?

## Method

- Use the exact displaced-orbit areal-density ceiling $\sigma_{\max}(\phi)$.
- Fix:
  - displacement angle $\phi$
  - node electrical power $P$
  - target shell-relative same-efficiency utilization $\lambda$
- This uniquely fixes:
  - PV area $A_p$
  - reflector area $A_r = A_p/\lambda$
- Subtract reflector, PV, and variable boom+tether masses from the total mass
  budget to obtain the maximum allowable fixed bus mass.

We also invert the same problem:

- for an ACS3-class `8.3 kg` bus, what minimum node power is required?

## Headline Findings

Using ACS3 boom line mass and a `1.25 mm` Dyneema tether benchmark:

- at `1°`, `10 kW`, and `10%` same-efficiency Swarm comparison:
  - maximum allowable fixed bus mass is only about `5.11 kg`
  - an ACS3-class `8.3 kg` bus is therefore too heavy by about `1.62x`
- at `1°`, `10 kW`, and `25%`:
  - maximum allowable fixed bus mass collapses to about `0.90 kg`
- at `2°`, `10 kW`, and `10%`:
  - maximum allowable fixed bus mass is only about `0.58 kg`
- at `2°`, `10 kW`, and `25%`:
  - the case is infeasible even before any fixed bus mass is added

Equivalent power thresholds for an ACS3-class `8.3 kg` bus:

- `1°`, `10%`: about `15.56 kW`
- `1°`, `25%`: about `62.47 kW`
- `2°`, `10%`: about `65.2 kW`

Interpretation:

- the bus mass ceiling tightens extremely quickly once both angle and desired
  same-shell performance are fixed
- this makes the systems problem much sharper than a pure materials argument
- `1°` class nodes are not just "lightweight sail" problems; they are also
  aggressive spacecraft-bus miniaturization problems

## Artifacts

- `results/fixed_mass_allowance.csv`
- `results/power_required_for_acs3_bus.csv`
- `results/summary.json`
