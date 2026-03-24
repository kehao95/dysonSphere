# Experiment: 20260323_ideal_architecture_comparison

## Goal

Establish a clean upper-bound comparison between MDDS, ideal Dyson Swarm, and ideal Dyson Ring by holding the following variables fixed:

- same star
- same orbital radius
- same ideal collector physics
- no aging
- no thermal degradation
- no maintenance or control loss

## Baselines

Ideal Dyson Swarm:

$$P_{\text{swarm}} = \eta f L_\odot$$

Ideal Dyson Ring, modeled as a complete spherical band of half-angle $\psi$:

$$P_{\text{ring}} = \eta \sin\psi \, L_\odot$$

MDDS:

$$P_{\text{MDDS}} = \eta_{\text{MDDS}} \lambda f L_\odot$$

so that

$$\frac{P_{\text{MDDS}}}{P_{\text{swarm}}} = \min(1,\lambda)\frac{\eta_{\text{MDDS}}}{\eta_{\text{swarm}}}$$

## What This Means

Under identical PV efficiency, MDDS cannot exceed the ideal energy upper bound of Dyson Swarm or Dyson Ring on the same occupied shell area. The threshold for parity is therefore:

$$\frac{\eta_{\text{MDDS}}}{\eta_{\text{swarm}}} > \frac{1}{\min(1,\lambda)}$$

or, equivalently for equal efficiencies, the PV areal density must be low enough that $\lambda$ can approach 1.

## Headline 1 Degree Results

At 1 AU and $\phi = 1^\circ$:

- total MDDS areal-density ceiling: 33.76 g/m²
- with CP1 reflector at 5 g/m², the PV subsystem must be at or below 28.76 g/m² to match an ideal same-efficiency Swarm
- if we reserve 5 g/m² for extra structure/control mass, that PV threshold tightens to 23.76 g/m²
- current optimistic ultralight tandem reference in this repo: 54.8 g/m²

Therefore, for the current best material case (`CP1 + ultralight tandem`):

- relative to ideal same-efficiency Swarm: 52.5%
- relative to an ideal 15% Dyson baseline: 95.9%
- equivalent ideal Ring half-angle at same efficiency: 31.7°
- required efficiency multiplier for exact same-shell parity: 1.905x

There is also a useful angular threshold:

- with zero extra structural margin, `CP1 + ultralight tandem` can still match an ideal same-efficiency Swarm up to about `0.565°`
- with `5 g/m²` extra non-PV mass, that parity angle drops to about `0.521°`
- with `10 g/m²` extra non-PV mass, it drops further to about `0.484°`

## Artifacts

- `results/parity_thresholds.csv`
- `results/current_material_comparison.csv`
- `results/summary.json`
