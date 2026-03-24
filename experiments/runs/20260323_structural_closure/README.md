# Experiment: 20260323_structural_closure

## Goal

Replace the abstract structural areal-density margin with an explicit geometry
model and quantify how node size closes the mass budget for a target angle and
power output.

## Method

- Assume a square reflector node.
- Model support structure as either:
  - `cross`: four center-to-corner booms
  - `perimeter`: four edge booms
- Suspend the payload bus below the reflector with four corner tethers.
- Use placeholder line densities already present in the repository:
  - carbon-fiber boom: 50 g/m
  - Dyneema tether: 0.97 g/m
- Add a fixed non-scaling mass term for payload bus / ACS / deployment hardware.

For a given angle and power target, solve for the minimum reflector area such
that:

$$\sigma_r + \lambda \sigma_{pv} + \sigma_{\text{structure}}(A_r) \le \sigma_{\max}(\phi)$$

## Scope

This is a structural closure *scaling* study, not yet a flight-ready structural
design. The boom/tether line densities are exploratory placeholders, but the
area-scaling law is explicit and useful.

## Headline Findings

For the optimistic `cross_light` scenario at $1^\circ$:

- 100 W node:
  - reflector area $\approx 61.0\ \text{m}^2$
  - side length $\approx 7.81\ \text{m}$
  - shell-relative ideal-Swarm comparison $\approx 0.44\%$
- 10 kW node:
  - reflector area $\approx 131.9\ \text{m}^2$
  - side length $\approx 11.48\ \text{m}$
  - shell-relative ideal-Swarm comparison $\approx 20.3\%$

Power thresholds at $1^\circ$ under the same structural model:

- $\lambda = 0.01$: about 231 W
- $\lambda = 0.05$: about 1.31 kW
- $\lambda = 0.10$: about 3.13 kW
- $\lambda = 0.25$: about 15.95 kW

Interpretation:

- the material pair may look feasible in areal-density terms
- but small low-power nodes are strongly penalized by fixed structural mass
- larger integrated nodes recover much more of the theoretical MDDS advantage

## Artifacts

- `results/structural_designs.csv`
- `results/summary.json`
