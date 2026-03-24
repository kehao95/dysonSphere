# Experiment: 20260323_linearized_stability

## Goal

Extract a closed-form local stability result around the practical low-`β`
optimal cone angle and verify it against the exact perturbation model.

## Method

Around

$$\alpha_{\text{opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right)$$

define the cone-angle error in radians as $\delta$ and the fractional beta
error as $\varepsilon_\beta$.

Then the local residual fractions are:

$$\frac{\Delta a_z}{a_{z,0}} \approx \varepsilon_\beta - 3\delta^2$$

$$\frac{\Delta a_r}{a_{r,0}} \approx \varepsilon_\beta - \frac{3}{\sqrt{2}}\delta$$

The experiment compares these closed-form approximations against the exact
perturbation model for a `1°` reference ring.

## Headline Findings

- axial response is second-order in cone-angle error
- radial response is first-order in cone-angle error
- the approximation is already very accurate over `0.1°–1°`

Representative comparisons:

- `0.5°` offset:
  - exact axial residual fraction: `2.2798e-4`
  - approximation: `2.2846e-4`
  - exact radial residual fraction: `1.8511e-2`
  - approximation: `1.8512e-2`
- `1.0°` offset:
  - exact axial residual fraction: `9.099e-4`
  - approximation: `9.139e-4`
  - exact radial residual fraction: `3.7013e-2`
  - approximation: `3.7024e-2`

Interpretation:

- the key reason the `1°` MDDS operating point is not hypersensitive in the
  axial direction is mathematical, not accidental
- the chosen cone angle sits at a stationary point of the axial SRP factor
- the first nonzero axial error term is quadratic

## Artifacts

- `results/linearized_vs_exact.csv`
- `results/summary.json`
