# Experiment: 20260323_mdds_feasibility

## Hypothesis

The MDDS concept remains feasible under an exact ideal-sail displaced-orbit model, but the true 1° requirement is stricter than the early heuristic $\beta \approx \sin\phi$ estimate. Therefore, feasibility at 1° should depend strongly on the areal density of the PV subsystem.

## Method

1. Use the exact circular displaced-orbit force balance implemented in `models/orbital/displaced_orbit.py`.
2. Derive the minimum-beta branch:

   $$\beta \cos^3\alpha = \cos\phi(1-\nu^2), \qquad \beta \cos^2\alpha \sin\alpha = \sin\phi$$

   which yields

   $$\alpha_{\text{opt}} = 35.264^\circ,\qquad \beta_{\min} = \frac{3\sqrt{3}}{2}\sin\phi$$

3. Convert current material data into areal densities using source-backed reflector and PV cases from `models/mass_budget/materials.py`.
4. Sweep angle and compute the maximum PV fill factor

   $$\lambda_{\max} = \frac{\sigma_{\max}(\phi) - \sigma_r}{\sigma_p}, \qquad \lambda \equiv A_p/A_r$$

5. Define utilization metrics:
   - shell-relative Dyson utilization: $U_{\text{rel}} = \lambda$ when compared against an all-collector Dyson Swarm using the same PV technology over the same shell area
   - absolute electrical utilization over reflector footprint: $\eta_{\text{abs}} = \lambda \eta_{\text{pv}}$

## Controlled Comparison Baselines

For the rest of this project we compare all concepts under the same ideal assumptions:

- same orbital radius
- same ideal optical/electrical conversion model
- no aging, no thermal degradation, no maintenance loss, no shielding penalty

Under these assumptions:

- ideal Dyson Swarm upper bound: $P_{\text{swarm}} = \eta f L_\odot$, with $f \le 1$
- ideal Dyson Ring upper bound for a complete spherical band of half-angle $\psi$: $P_{\text{ring}} = \eta \sin\psi \, L_\odot$
- MDDS relative to an ideal Swarm: $P_{\text{MDDS}}/P_{\text{swarm}} = \lambda (\eta_{\text{MDDS}}/\eta_{\text{swarm}})$

This means that under truly identical PV technology, MDDS cannot beat the pure energy upper bound of an ideal Swarm or ideal Ring on the same occupied shell area; its advantage must come from orbital manageability, packing, or from using better PV technology than the comparison baseline.

## Source-Backed Material Cases

- Reflector, optimistic: CP1 sail subsystem, 5 g/m², NASA Tech Brief
- Reflector, conservative: 7.6 um aluminized Kapton, 11 g/m², NASA report
- PV, optimistic: ultralight flexible tandem, 27.4%, >5000 W/kg, converted to 54.8 g/m² upper-bound areal density
- PV, conservative space-oriented: flexible CIGS projection, 15%, 1153.13 W/kg, converted to 176.0 g/m²
- PV, commercial: MiaSole FLEX-03W, 16.7%, 1.7 kg/m²

## Key Results

### Exact 1° Reference Ring at 1 AU

- $\beta_{\min} = 0.04534$
- $\alpha_{\text{opt}} = 35.264^\circ$
- $\omega/\omega_{\text{Kepler}} = 0.98758$
- orbital period = 369.81 days
- vertical displacement = $2.61 \times 10^6$ km
- allowable total areal density = 33.76 g/m²
- required photon-pressure components:
  - radial sail force = $4.94 \times 10^{-6}$ N/m²
  - axial sail force = $3.49 \times 10^{-6}$ N/m²

### 1° Material Feasibility

| Case | $\lambda_{\max}$ | $U_{\text{rel}}$ | $\eta_{\text{abs}}$ |
|------|------------------|------------------|---------------------|
| CP1 + ultralight tandem | 0.525 | 52.5% | 14.4% |
| CP1 + projected space CIGS | 0.163 | 16.3% | 2.45% |
| CP1 + commercial CIGS module | 0.0169 | 1.69% | 0.283% |
| Kapton + ultralight tandem | 0.415 | 41.5% | 11.4% |

Interpretation:
- A 1° MDDS ring is plausible with very light PV technology.
- The same ring is essentially non-competitive with current commercial flexible CIGS modules.

### Angle Limits

Reflector-only upper bounds:
- CP1 subsystem: 6.77°
- 7.6 um Kapton: 3.07°

For `CP1 + ultralight tandem`, the maximum angle depends on how much of a Dyson-Swarm-like shell utilization we want to retain:
- 5% utilization: 4.37°
- 10% utilization: 3.22°
- 25% utilization: 1.81°
- 50% utilization: 1.04°

## Conclusion

The concept survives the exact force-balance correction, but the correction matters. The early $\beta \approx \sin\phi$ heuristic understated the 1° requirement by a factor of about 2.6. Under the tighter mass budget, the decisive bottleneck is no longer the sail film alone but the PV areal density. In first-pass form, the architecture looks credible for sub-degree to ~1° rings with current ultralight PV demonstrations, but not with heavy commercial flexible modules.

## Artifacts

- `results/angle_tradeoff.csv`
- `results/utilization_tradeoff.csv`
- `results/summary.json`
