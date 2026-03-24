# Quantitative Findings: First Pass

## Exact Orbit Model

For a displaced circular orbit at heliocentric radius $r$ and latitude $\phi$, let the sail cone angle be $\alpha$ and let

$$\nu = \frac{\omega}{\sqrt{\mu/r^3}}$$

denote the orbital-rate ratio relative to a Keplerian circular orbit at the same spherical radius. For an ideal specular sail, the SRP balance is

$$\beta \cos^3\alpha = \cos\phi(1-\nu^2)$$
$$\beta \cos^2\alpha \sin\alpha = \sin\phi$$

Minimizing $\beta$ over sail attitude yields the practical low-$\beta$ branch:

$$\alpha_{\text{opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right) \approx 35.264^\circ$$
$$\beta_{\min} = \frac{3\sqrt{3}}{2}\sin\phi$$
$$\nu^2 = 1 - \sqrt{2}\tan\phi$$

This is the first important correction to the early project intuition. The exact 1° requirement is not $\beta \approx 0.0175$ but

$$\beta_{\min}(1^\circ) \approx 0.04534$$

which lowers the allowable total system areal density to

$$\sigma_{\max}(1^\circ) = \frac{\sigma^*}{\beta_{\min}} \approx 33.76\ \text{g/m}^2$$

for $\sigma^* = 1.53\ \text{g/m}^2$.

## Typical 1° Ring Force Analysis

At 1 AU and $\phi = 1^\circ$:

- vertical displacement: $d \approx 2.61 \times 10^6$ km
- orbital period: 369.81 days
- photon pressure projected onto the sail normal: $6.05 \times 10^{-6}$ N/m²
- radial sail force requirement: $4.94 \times 10^{-6}$ N/m²
- axial sail force requirement: $3.49 \times 10^{-6}$ N/m²

The axial force matches the vertical component of solar gravity, while the radial force partially unloads the centripetal demand. The displaced orbit therefore remains orbital rather than fully levitated.

## Material Feasibility

We tested source-backed material pairs:

- reflector: CP1 sail subsystem, 5 g/m²
- reflector: 7.6 um aluminized Kapton, 11 g/m²
- PV: ultralight flexible tandem, 27.4%, 54.8 g/m² upper-bound areal density
- PV: projected space CIGS, 15%, 176.0 g/m²
- PV: commercial flexible CIGS module, 16.7%, 1700 g/m²

Define

$$\lambda = \frac{A_p}{A_r}$$

as the PV fill factor and

$$\eta_{\text{abs}} = \lambda \eta_{\text{pv}}$$

as the electrical utilization per reflector footprint. When compared to an all-collector Dyson Swarm using the same PV technology over the same shell area, the relative utilization is simply

$$U_{\text{rel}} = \lambda$$

At 1° the results are:

| Case | $\lambda_{\max}$ | $\eta_{\text{abs}}$ |
|------|------------------|---------------------|
| CP1 + ultralight tandem | 0.525 | 14.4% |
| CP1 + projected space CIGS | 0.163 | 2.45% |
| CP1 + commercial CIGS module | 0.0169 | 0.283% |
| Kapton + ultralight tandem | 0.415 | 11.4% |

This is the second important result: for the decoupled architecture, the real bottleneck is the PV areal density, not just the sail film.

## Controlled Comparison Against Dyson Swarm and Dyson Ring

To keep the comparison pure, we now hold the following variables fixed across all concepts:

- same stellar luminosity and orbital radius
- same ideal collector physics
- no aging, thermal degradation, maintenance loss, or shielding penalty

Then the ideal upper bounds are:

$$P_{\text{swarm}} = \eta f L_\odot,\qquad f \le 1$$
$$P_{\text{ring}} = \eta \sin\psi \, L_\odot$$

and for MDDS:

$$P_{\text{MDDS}} = \eta_{\text{MDDS}} \lambda f L_\odot$$

Therefore:

$$\frac{P_{\text{MDDS}}}{P_{\text{swarm}}} = \min(1,\lambda)\frac{\eta_{\text{MDDS}}}{\eta_{\text{swarm}}}$$

This clarifies the threshold question:

- if MDDS and Dyson Swarm use the same PV technology, MDDS cannot exceed the ideal energy upper bound of Dyson Swarm on the same shell area; at best it approaches parity as $\lambda \to 1$
- if MDDS can use higher-efficiency PV than the comparison Dyson Swarm, then a true threshold exists at

$$\frac{\eta_{\text{MDDS}}}{\eta_{\text{swarm}}} > \frac{1}{\min(1,\lambda)}$$

For the best current 1° case in this repository, $\lambda_{\max} \approx 0.525$, so parity against an ideal same-efficiency Swarm is impossible, while parity against a lower-efficiency 15% Dyson baseline would require only about a 1.905x efficiency advantage

The same benchmark also gives a useful angular threshold. For `CP1 + ultralight tandem`, parity with an ideal same-efficiency Swarm remains possible only up to about $0.565^\circ$ if no extra non-PV mass is reserved. Adding just $5\ \text{g/m}^2$ of extra structure/control margin lowers that threshold to about $0.521^\circ$.

## Angle Limit Interpretation

There are two different "maximum angle" questions:

1. **Reflector-only upper bound**

   This asks what the sail subsystem can support if the PV contribution tends to zero.

   - CP1 reflector-only limit: 6.77°
   - 7.6 um Kapton reflector-only limit: 3.07°

2. **Functional power-generating limit**

   This asks what angle remains possible once we demand a nontrivial power-harvesting fraction.

   For `CP1 + ultralight tandem`:

   - 10% shell-relative Dyson utilization: 3.22°
   - 25% utilization: 1.81°
   - 50% utilization: 1.04°

So the publishable claim should not be "current materials support several-degree rings with useful payload" in a generic sense. The defensible claim is narrower:

> Current source-backed materials support a credible first-pass MDDS architecture in the sub-degree to ~1° regime with ultralight PV, while multi-degree rings quickly become utilization-limited.

## Immediate Paper-Level Conclusions

1. The concept remains viable after replacing the optimistic heuristic with the exact force-balance model.
2. The exact model is materially stricter, so every feasibility claim must use the corrected $\beta_{\min}$ relation.
3. A 1° ring at 1 AU is still physically compelling because it yields 2.61 million km of separation.
4. Commercial flexible PV modules are too heavy for a competitive 1° MDDS node.
5. Ultralight PV demonstrations make the concept plausible, but structural mass closure and perturbation stability are now the critical next steps.

## Structural Closure: Node Granularity Matters

We then replaced the abstract extra-areal-density term with a geometry-explicit
structural model based on square reflectors, deployable booms, suspended
payload tethers, and a fixed bus mass. Even with exploratory placeholder line
densities, the scaling law exposes an important effect:

> At fixed angle, small-power nodes are punished by fixed structural mass, while
> larger-power nodes amortize that mass and recover much more of the ideal
> energy limit.

For the `cross_light` structural scenario at $1^\circ$:

- 100 W node: reflector area $\approx 61.0\ \text{m}^2$, shell-relative Swarm comparison $\approx 0.44\%$
- 10 kW node: reflector area $\approx 131.9\ \text{m}^2$, shell-relative Swarm comparison $\approx 20.3\%$

The same model implies approximate power thresholds at $1^\circ$:

- to reach $\lambda = 0.01$: about 231 W
- to reach $\lambda = 0.05$: about 1.31 kW
- to reach $\lambda = 0.10$: about 3.13 kW
- to reach $\lambda = 0.25$: about 15.95 kW

For the heavier `cross_nominal` structure model, these thresholds move upward
to about 356 W, 2.00 kW, 4.72 kW, and 23.0 kW respectively.

This is a third key conclusion:

> Even if the material pair is nominally feasible at the areal-density level,
> a 1° MDDS architecture is unlikely to look competitive when discretized into
> many small low-power nodes. Larger integrated nodes recover much more of the
> theoretical MDDS advantage.

## Perturbation Sensitivity: First Control Slice

We then asked whether the exact $1^\circ$ operating point is hypersensitive to
small sail-state errors. Holding the nominal orbital rate fixed and perturbing
the sail state around the minimum-$\beta$ solution gives a first control slice:

- cone-angle error that produces a 1% axial residual: $\approx 3.33^\circ$
- cone-angle error that produces a 5% axial residual: $\approx 7.56^\circ$
- cone-angle error that produces a 10% axial residual: $\approx 10.84^\circ$
- fractional $\beta$ error maps linearly to the same fractional axial residual

Using a representative external pressure disturbance of
$2.6\times 10^{-9}\ \text{N/m}^2$ gives an equivalent $\beta$ perturbation of
only about $5.73\times 10^{-4}$. In this simple constant-acceleration estimate,
that would take about 67 days to accumulate a 1000 km offset if left
uncorrected.

This does **not** replace a full linearized stability treatment. But it does
support a useful intermediate conclusion:

> The $1^\circ$ MDDS operating point is not obviously hypersensitive to small
> pointing or solar-wind-scale disturbances. The remaining stability question is
> a control-and-dynamics closure problem, not an immediate order-of-magnitude
> impossibility.

We can now sharpen that statement with a closed-form local result. Around the
practical low-$\beta$ optimum

$$\alpha_{\text{opt}}=\arctan\left(\frac{1}{\sqrt{2}}\right)$$

let $\delta$ be the cone-angle error in radians and let $\varepsilon_\beta$ be
the fractional beta error. Then:

$$\frac{\Delta a_z}{a_{z,0}} \approx \varepsilon_\beta - 3\delta^2$$
$$\frac{\Delta a_r}{a_{r,0}} \approx \varepsilon_\beta - \frac{3}{\sqrt{2}}\delta$$

This is a mathematically important result:

- the axial response is second-order in cone-angle error
- the radial response is first-order in cone-angle error

So the weak axial sensitivity at the $1^\circ$ operating point is not
accidental; it follows from the fact that the chosen cone angle sits at a
stationary point of the axial SRP factor.

The approximation matches the exact model very closely. At a $1^\circ$ cone
offset:

- exact axial residual fraction: $\approx 9.10\times 10^{-4}$
- approximation: $\approx 9.14\times 10^{-4}$
- exact radial residual fraction: $\approx 3.701\times 10^{-2}$
- approximation: $\approx 3.702\times 10^{-2}$

and even at $2^\circ$ the relative errors remain below about 1%.

## Integrated Design Map: Angle, Node Power, and Benchmark Performance

Finally, we coupled the exact orbit model, the structure scaling law, and the
ideal Swarm/Ring benchmark into one design-map experiment.

For same-efficiency comparisons:

$$\frac{P_{\text{MDDS}}}{P_{\text{swarm}}} = \lambda$$

and the same ratio maps to an equivalent ideal Dyson-Ring half-angle
$\psi_{\text{eq}} = \arcsin(\lambda)$.

At $1^\circ$, under the optimistic `cross_light` structure model:

- 10% of an ideal same-efficiency Swarm ($\psi_{\text{eq}}\approx 5.74^\circ$)
  requires about 3.13 kW per node
- 25% ($\psi_{\text{eq}}\approx 14.48^\circ$) requires about 15.95 kW
- 50% ($\psi_{\text{eq}}=30^\circ$) requires about 2.67 MW

Under the heavier `cross_nominal` structure model at the same angle:

- 10% requires about 4.72 kW
- 25% requires about 23.0 kW

At $2^\circ$, the picture tightens substantially. For `cross_light`:

- 1% requires about 1.03 kW
- 5% requires about 7.52 kW
- 10% requires about 28.45 kW
- 25% is infeasible for the current `CP1 + ultralight tandem` pair

That last point is especially important: by $2^\circ$, a 25% same-efficiency
Swarm comparison is not just structurally difficult; it is ruled out by the
material areal-density ceiling before structure is even added.

The design map also clarifies what fixed node power can buy:

- a 10 kW `cross_light` node reaches about 20.3% of an ideal same-efficiency
  Swarm at $1^\circ$ (equivalent ideal Ring half-angle $\approx 11.73^\circ$)
- the same 10 kW node falls to about 5.98% at $2^\circ$
  ($\psi_{\text{eq}}\approx 3.43^\circ$)
- a 10 kW `cross_light` node can still sustain 10% out to about $1.53^\circ$,
  but 25% only out to about $0.873^\circ$
- even a 100 kW `cross_light` node only extends these limits to about
  $2.46^\circ$ for 10%, $1.41^\circ$ for 25%, and $0.84^\circ$ for 50%

This creates a much sharper, more publishable systems statement:

> With the current best source-backed material pair in this repository,
> sub-degree to roughly $1$–$1.5^\circ$ MDDS rings can retain meaningful
> same-shell energy performance only when nodes are pushed into the kW to
> 100-kW regime. Multi-degree rings remain possible mainly in low-utilization
> regimes.

## Flight-Heritage Gap: The Integrated Spacecraft Is Still the Problem

To separate "materials are too heavy" from "the current full spacecraft stack is
too heavy," we benchmarked two real solar-sail flight systems directly against
the exact MDDS areal-density requirement.

For NASA ACS3:

- total deployed system: $16\ \text{kg}$ over $80\ \text{m}^2$
- deployed areal density: $200\ \text{g/m}^2$
- effective $\beta \approx 0.00765$
- exact maximum MDDS angle at 1 AU: only about $0.169^\circ$
- required mass reduction to reach $1^\circ$: about $5.92\times$

For NASA NEA Scout:

- total spacecraft mass: less than $14\ \text{kg}$ over an $86\ \text{m}^2$ sail
- upper-bound deployed areal density: about $162.8\ \text{g/m}^2$
- exact maximum MDDS angle at 1 AU: about $0.207^\circ$
- required mass reduction to reach $1^\circ$: about $4.82\times$

But the ACS3 decomposition is even more informative. If we strip ACS3 down to
just the membrane and booms:

- sail quadrant mass: $4 \times 0.085\ \text{kg}$
- boom mass: $4 \times 0.164\ \text{kg}$
- combined deployed areal density: $12.45\ \text{g/m}^2$
- exact maximum MDDS angle at 1 AU: about $2.71^\circ$

That subcase is already in the right regime. At $1^\circ$, it would still leave
enough mass margin for about

$$\lambda_{\max} \approx 0.389$$

of the ultralight tandem PV benchmark before any additional bus/control mass is
added.

This is a fourth major conclusion:

> Current flight-demonstrated solar-sail systems are not yet light enough as
> integrated spacecraft for 1°-class MDDS nodes, but their membrane-plus-boom
> hardware is already much closer to the required regime. The dominant gap is
> now the spacecraft bus, deployment, and control stack carried behind the sail.

## Fixed Bus Budget: MDDS Is Also a Spacecraft Miniaturization Problem

We then turned the ACS3 heritage numbers into a stricter systems threshold.
Once angle $\phi$, node power $P$, and target same-shell energy ratio
$\lambda$ are fixed, the reflector area is no longer free:

$$A_p = \frac{P}{S\eta_{\text{pv}}}, \qquad A_r = \frac{A_p}{\lambda}$$

At that point, the remaining mass margin is the maximum allowable fixed bus /
deployment / control mass:

$$m_{\text{fixed,max}} = \frac{\sigma_{\max}(\phi) A_r}{1000}
 - m_r - m_p - m_{\text{boom+tether}}(A_r)$$

Using ACS3-derived boom line density and a 1.25 mm Dyneema tether benchmark:

- at $1^\circ$, $10\ \text{kW}$, and $\lambda = 0.10$:
  - $m_{\text{fixed,max}} \approx 5.11\ \text{kg}$
  - an ACS3-class $8.3\ \text{kg}$ bus is too heavy by a factor of about 1.62
- at $1^\circ$, $10\ \text{kW}$, and $\lambda = 0.25$:
  - $m_{\text{fixed,max}} \approx 0.90\ \text{kg}$
- at $2^\circ$, $10\ \text{kW}$, and $\lambda = 0.10$:
  - $m_{\text{fixed,max}} \approx 0.583\ \text{kg}$
  - an ACS3-class bus is too heavy by about $14.2\times$
- at $2^\circ$, $10\ \text{kW}$, and $\lambda = 0.25$:
  - the design is infeasible even before any fixed bus mass is added

The same threshold can be inverted to ask how much power is needed to carry an
ACS3-class bus:

- $1^\circ$, $\lambda = 0.10$: about $15.56\ \text{kW}$
- $1^\circ$, $\lambda = 0.25$: about $62.47\ \text{kW}$
- $2^\circ$, $\lambda = 0.10$: about $65.2\ \text{kW}$

This sharpens the engineering story again:

> In the current source-backed regime, a 1° MDDS node is not merely a
> lightweight-sail problem. Once meaningful same-shell energy performance is
> demanded, it becomes a fixed-spacecraft-mass problem, and the allowable bus
> mass can collapse into the sub-kilogram range surprisingly quickly.
