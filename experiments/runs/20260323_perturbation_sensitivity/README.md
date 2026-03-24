# Experiment: 20260323_perturbation_sensitivity

## Goal

Quantify how sensitive the exact displaced-orbit solution is to:

- sail cone-angle errors
- lightness-number errors
- a representative small external pressure disturbance

## Method

Hold the nominal orbital-rate ratio fixed at the minimum-beta displaced-orbit
solution and compute the residual axial and radial accelerations when:

- $\alpha \to \alpha + \Delta\alpha$
- $\beta \to \beta (1+\delta)$

These residuals represent the control effort needed to remain on the original
ring.

## External Disturbance Check

For a simple scale comparison, we convert a representative solar-wind dynamic
pressure into an equivalent fractional beta perturbation. This is only an
order-of-magnitude disturbance estimate, not a full plasma interaction model.

## Artifacts

- `results/cone_angle_sensitivity.csv`
- `results/beta_sensitivity.csv`
- `results/summary.json`
