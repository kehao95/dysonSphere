# Introduction

## Nodal-crossing burden in same-shell Keplerian swarms

Dyson swarms are often treated as the least structurally extreme form of artificial stellar energy collection because they replace a monolithic shell with many independent orbiting collectors [@dyson1960infrared; @wright2015gies; @wright2020dysonspheres]. That simplification is real, but dense same-shell Keplerian realizations still face a systems-level organization problem. When many inclined orbital planes are used at comparable heliocentric radii, the planes intersect at nodal lines. A dense collector population then inherits repeated crossing corridors that must be phased, screened, or otherwise managed.

This paper uses the nodal issue as an architecture-level burden rather than as a closed collision-rate calculation. If a same-radius swarm uses $P$ distinct orbital planes, the number of pairwise nodal lines scales as

$$
N_{\mathrm{node}}\sim \frac{P(P-1)}{2},
$$

with two antipodal crossing corridors associated with each non-coplanar plane pair. If each plane hosts many collectors, the bookkeeping for phase separation and exclusion windows grows with the plane-pair graph. Modern large-constellation studies already show that conjunction risk, debris generation, and reconfiguration burden become system-level management issues for dense orbital populations [@radtke2017oneweb; @lemay2018collision; @deweck2004staged; @lee2018staged]. The present argument is more limited: dense same-shell Keplerian collector architectures can develop a growing nodal-crossing management burden when many inclined planes are used.

At the opposite endpoint, statites and Dyson-bubble-like concepts use continuous radiation-pressure support rather than ordinary orbital support [@forward1991statite; @mcinnes1999solarsailing; @mcinnes2026bubbles]. This removes the same-shell nodal geometry, but it pushes the architecture toward the severe areal-density demands associated with $\beta\geq1$ radiative support. The useful intermediate question is therefore whether part of the collector population can remain primarily orbital while using modest radiation pressure to maintain non-intersecting displaced latitude bands.

## Contribution of this paper

The present manuscript develops one low-latitude segment of that intermediate design space. It uses established displaced non-Keplerian orbit (DNKO) and solar-sail force-balance ideas, but reinterprets the low-latitude displaced branch as a screening model for stratified Dyson-swarm architectures [@mcinnes1992haloorbits1; @mcinnes1992haloorbits2; @mcinnes1997displaced; @mcinnes1998dnko; @simo2010displaced; @wawrzyniak2011generating].

The central result is a compact support-density criterion. In the reduced ideal-specular model used here, the minimum lightness number needed to sustain displacement latitude $\phi$ is

$$
\beta_{\min}(\phi)=\frac{3\sqrt3}{2}\sin\phi,
$$

and the corresponding maximum supportable system areal density is

$$
\sigma_{\max}(\phi)=\frac{2\sigma^*}{3\sqrt3\sin\phi}.
$$

The architecture question then becomes whether a candidate supported system satisfies

$$
\sigma_{\mathrm{sys}}<\sigma_{\max}(\phi).
$$

The novelty is architectural and screening-oriented rather than orbital-family discovery. This paper does not claim a new DNKO family, a complete stability proof, a closed optical-power architecture, or a solved Dyson-swarm collision model. Its narrower claim is that a known displaced-orbit toolkit can be developed into a low-latitude screening relation connecting displacement latitude, lightness number, and system areal density for radiation-pressure-assisted swarm stratification.

The rest of the paper is organized as follows. Section 2 maps the prior-art boundary and claim boundary. Section 3 defines the reduced support model and derives the optimized support curve. Section 4 gives representative low-latitude design slices and a synchronization-constrained branch. Section 5 gives a branch-specific local boundedness check. Section 6 discusses architectural implications, limitations, and follow-on work.

# Background and Claim Boundary

The relevant prior art spans solar-sail astrodynamics, displaced non-Keplerian orbits, synchronous displaced branches, Dyson-swarm/bubble concepts, and dense-orbital-population management. The present manuscript deliberately uses that literature as foundation rather than as contrast.

| Topic | Existing literature | Used here as | New in this paper |
|---|---|---|---|
| Statites and Dyson bubbles | Known radiative-support endpoint [@forward1991statite; @mcinnes1999solarsailing; @mcinnes2026bubbles] | High-support comparison limit | No |
| Displaced non-Keplerian orbits | Known solar-sail orbit family [@mcinnes1997displaced; @mcinnes1998dnko] | Dynamical basis | No |
| Solar-sail lightness number | Standard support parameter [@mcinnes1999solarsailing] | Areal-density bridge | No |
| Synchronous displaced branches | Known operational variants [@heiligers2015earthfollowing; @quarta2020earthsync; @bassetto2024marssync] | Period-constrained slice | No |
| Dyson swarm/bubble framing | Known architecture context [@dyson1960infrared; @wright2020dysonspheres; @mcinnes2026bubbles] | Systems-level motivation | No |
| Low-latitude density screening curve for stratified Dyson architectures | Not usually formulated this way | Main result | Yes |
| Branch-specific radial-latitude boundedness check | Derived for this reduced branch model | Secondary check | Limited yes |

Recent work narrows the novelty boundary further. In particular, McInnes (2026) explicitly discusses using displaced non-Keplerian orbit families and parallel stacking to reduce collisions in orbiting Dyson-swarm concepts [@mcinnes2026bubbles]. The present paper therefore does not claim to be the first to notice that bridge. It develops the bridge into an explicit low-latitude screening model and design-language framework.

# Nomenclature

| Symbol | Definition | Unit |
|---|---|---|
| $r$ | Heliocentric distance | m or AU |
| $\rho$ | Cylindrical radius | m |
| $z$ | Out-of-plane displacement | m |
| $\phi$ | Displacement latitude | rad or deg |
| $\theta$ | Along-track angular coordinate | rad |
| $\omega$ | Angular velocity | s$^{-1}$ |
| $n$ | Keplerian mean motion, $\sqrt{\mu/r^3}$ | s$^{-1}$ |
| $\nu$ | Orbital-rate ratio, $\omega/n$ | dimensionless |
| $\mu$ | Stellar gravitational parameter | m$^3$ s$^{-2}$ |
| $\beta$ | Solar-sail lightness number | dimensionless |
| $\sigma^*$ | Critical ideal-reflector areal density | kg m$^{-2}$ |
| $\sigma_{\mathrm{sys}}$ | Supported system areal density | kg m$^{-2}$ |
| $\sigma_{\max}$ | Maximum supportable system areal density | kg m$^{-2}$ |
| $\alpha_{\mathrm{eff}}$ | Reduced meridional support pitch | rad |
| $\gamma$ | Standard Sun-line sail cone angle | rad |

# Reduced Support Model

## Assumptions and exclusions

The paper uses a deliberately reduced support model because its purpose is architecture-level screening rather than final mission closure.

| Assumption | Meaning | Consequence |
|---|---|---|
| Ideal specular reflector | Radiation pressure follows an ideal mirror limit | Upper-bound support efficiency |
| Low-latitude working regime | Main examples use $\phi\lesssim1^\circ$ | Main formula is not claimed as a high-latitude branch |
| Point-sail / local element model | No finite-size shadowing or mutual attenuation | Collective optical effects are excluded |
| Attitude-commanded support vector | Support pitch is held nominally | Finite attitude dynamics are excluded |
| Effective support area | Radiation-pressure support area defines $\sigma_{\mathrm{sys}}$ | Power-collection area is not automatically the same area |
| System areal density | Total supported mass divided by support area | Payload and power hardware enter as mass unless optically modeled |

The photovoltaic fill-factor estimate used later is therefore not an optical-power architecture. It is only a supported-mass bookkeeping exercise. A real collector would require a coupled optical, thermal, and attitude model because absorbing, converting, shadowing, or reradiating area changes the radiation-pressure vector.

## Geometry and force balance

Consider a collector at fixed heliocentric distance $r$ and latitude $\phi$, moving on a circular displaced path with angular velocity $\omega$. In cylindrical variables,

$$
\rho=r\cos\phi,\qquad z=r\sin\phi,
$$

and the orbital-rate ratio is

$$
\nu\equiv\frac{\omega}{\sqrt{\mu/r^3}}.
$$

The compact model used in the main text writes the idealized radiation-pressure acceleration in terms of an effective meridional support pitch $\alpha_{\mathrm{eff}}$:

$$
a_\rho=\frac{\mu}{r^2}\beta\cos^3\alpha_{\mathrm{eff}},
$$

$$
a_z=\frac{\mu}{r^2}\beta\cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}}.
$$

Here $\alpha_{\mathrm{eff}}$ is not the standard Sun-line sail cone angle. It is an effective support pitch in a reduced cylindrical model. Appendix A uses the standard cone angle $\gamma$ and shows that the reduced curve is conservative by only a few percent over the low-latitude examples used in this paper.

The reduced force-balance equations are

$$
\beta\cos^3\alpha_{\mathrm{eff}}=\cos\phi(1-\nu^2),
$$

$$
\beta\cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}}=\sin\phi.
$$

The first equation represents radial unloading of the gravitational demand. The second represents the out-of-plane support required to maintain the displaced latitude.

## Payload-optimized support curve

At fixed $\phi$, minimizing the required lightness number is equivalent to maximizing

$$
f(\alpha_{\mathrm{eff}})=\cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}},
$$

because

$$
\beta=\frac{\sin\phi}
{\cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}}}.
$$

Differentiating gives

$$
\tan^2\alpha_{\mathrm{eff}}=\frac12,
$$

so the reduced support pitch is

$$
\alpha_{\mathrm{eff,opt}}=\arctan(1/\sqrt2).
$$

At that point,

$$
f_{\max}=\frac{2}{3\sqrt3},
$$

which yields

$$
\beta_{\min}(\phi)=\frac{3\sqrt3}{2}\sin\phi.
$$

The equivalent system areal-density ceiling is

$$
\sigma_{\max}(\phi)
=\frac{\sigma^*}{\beta_{\min}(\phi)}
=\frac{2\sigma^*}{3\sqrt3\sin\phi}.
$$

This is the main screening relation. It is not a universal high-latitude ideal-sail solution; it is a low-latitude architecture relation for systems that can be represented by the reduced support model.

## Reproducibility

All numerical values in the representative slices are computed directly from the equations above using $\sigma^*=1.53\,\mathrm{g\,m^{-2}}$ and $a_\oplus=1\,\mathrm{AU}$. The plotting scripts used for the current support-curve and low-latitude figures are in `Paper/figures/scripts/` and `Paper/figures/generate_figures.py`. A frozen repository snapshot or Zenodo archive should be minted before journal submission.

# Low-Latitude Screening Results

## Support curve

The support curve has two immediate small-angle consequences. First, the lightness-number requirement is approximately linear in latitude:

$$
\beta_{\min}(\phi)\approx\frac{3\sqrt3}{2}\phi
\quad(\phi\ll1).
$$

Second, the allowable system areal density contracts approximately as $1/\phi$:

$$
\sigma_{\max}(\phi)\approx
\frac{2\sigma^*}{3\sqrt3\,\phi}.
$$

The existing support-curve figure should be used here as Fig. 1:

![Low-latitude support curves. Left: required lightness number $\beta_{\min}(\phi)$. Right: maximum supportable system areal density $\sigma_{\max}(\phi)$.](../figures/results/support_curves.pdf){#fig:support-curves}

## Representative numerical values

Table 1 gives representative 1 AU cases. The Earth-angular-radius point $\theta_\oplus\approx0.00244^\circ$ is included as an entry-scale offset because it corresponds to approximately one Earth radius of normal separation at 1 AU.

| $\phi$ | $z=r\sin\phi$ at 1 AU | $\beta_{\min}$ | $\sigma_{\max}$ | Interpretation |
|---:|---:|---:|---:|---|
| $\theta_\oplus$ | $6.37\times10^3$ km | $1.11\times10^{-4}$ | $13.83\,\mathrm{kg\,m^{-2}}$ | Entry-scale offset |
| $0.1^\circ$ | $2.61\times10^5$ km | $4.53\times10^{-3}$ | $337.4\,\mathrm{g\,m^{-2}}$ | Permissive low-$\beta$ case |
| $0.5^\circ$ | $1.31\times10^6$ km | $2.27\times10^{-2}$ | $67.5\,\mathrm{g\,m^{-2}}$ | Lightweight-system regime |
| $1.0^\circ$ | $2.61\times10^6$ km | $4.53\times10^{-2}$ | $33.8\,\mathrm{g\,m^{-2}}$ | Demanding integrated system |

The table shows why the low-latitude region is useful as an architecture screen. Very small angular displacements correspond to large normal separations at 1 AU while remaining well below the $\beta\geq1$ radiative-support regime.

The existing low-latitude figure should be used here as Fig. 2:

![Low-latitude feasibility window showing $\sigma_{\max}$ at representative latitudes.](../figures/results/low_latitude_window.pdf){#fig:low-latitude-window}

## Engineering mass-budget slice

A minimal supported-mass bookkeeping exercise can connect the screening curve to payload margin. For an illustrative reflector-supported node,

$$
\sigma_{\mathrm{sys}}=\sigma_{\mathrm{refl}}+\lambda\sigma_{\mathrm{pv}},
$$

where $\lambda=A_{\mathrm{pv}}/A_{\mathrm{refl}}$ is a bookkeeping fill factor, not an optically closed power-system variable. The reflector benchmark $\sigma_{\mathrm{refl}}\approx5\,\mathrm{g\,m^{-2}}$ and device-level ultralight PV benchmark $\sigma_{\mathrm{pv}}\approx54.8\,\mathrm{g\,m^{-2}}$ are used only to illustrate how the support curve maps into mass margin [@kim2021ultralight].

Under those illustrative assumptions, $0.1^\circ$ and $0.5^\circ$ remain permissive to first order, while $1^\circ$ gives a bookkeeping limit near $\lambda_{\max}\approx0.53$. This should not be interpreted as a physical PV coverage solution. It is a mass-budget translation of the support curve. A real collector would need an optical, thermal, electrical, attitude, and structural model.

The comparison with flown and near-flight solar-sail systems is useful only as scale context. LightSail 2 and NEA Scout have mission-level loadings near $156$-$160\,\mathrm{g\,m^{-2}}$ [@johnson2017neascout; @mansell2023lightsail2]. Those values are below the $\theta_\oplus$ and $0.1^\circ$ thresholds but above the $1^\circ$ threshold, consistent with the interpretation that the low-latitude window is non-empty but contracts rapidly.

## Synchronization-constrained branch

The same reduced model can be sliced by an imposed common-period condition. For an Earth-synchronous reference period, the displaced orbit radius satisfies

$$
r_{\mathrm{sync}}(\phi,\alpha_{\mathrm{eff}})
=a_\oplus\left(1-\frac{\tan\phi}{\tan\alpha_{\mathrm{eff}}}\right)^{1/3}.
$$

Using the optimized support pitch gives

$$
r_{\mathrm{sync}}(\phi)
=a_\oplus(1-\sqrt2\tan\phi)^{1/3}.
$$

Synchronization changes the operating radius in this reduced branch but does not introduce an additional support-density penalty. Numerically, the inward shift is approximately $0.12$ million km at $0.1^\circ$, $0.62$ million km at $0.5^\circ$, and $1.24$ million km at $1^\circ$.

The existing synchronization figure should be used here as Fig. 3:

![Earth-synchronous radius correction along the low-latitude optimized branch.](../figures/results/sync_radius.pdf){#fig:sync-radius}

## Cone-angle correction

Because the main model uses $\alpha_{\mathrm{eff}}$ rather than the standard Sun-line cone angle, the cone-angle comparison is included in the main results rather than hidden only in the appendix.

| $\phi$ | Reduced $\beta_{\min}$ | Cone-angle $\beta_{\mathrm{cone}}$ | Difference |
|---:|---:|---:|---:|
| $0.1^\circ$ | 0.004535 | 0.004523 | +0.25% |
| $0.5^\circ$ | 0.02267 | 0.02240 | +1.24% |
| $1.0^\circ$ | 0.04534 | 0.04425 | +2.48% |

The reduced formula slightly overestimates the standard cone-angle support requirement over the representative low-latitude cases. It is therefore conservative for the screening purpose used here.

# Local Boundedness of the Reduced Branch

The support curve defines the low-latitude displaced branch, but it does not prove full passive stability or control closure. A narrower check can be made for the radial-latitude subsystem of the same reduced model.

Let $n=\sqrt{\mu/r_0^3}$ and let $\nu=\omega/n$ at the nominal displaced circular solution. After linearizing the reduced spherical equations about $(r_0,\phi_0,\dot\theta=\omega)$ and removing the conserved along-track phase/angular-momentum offset, the radial-latitude subsystem yields the compact characteristic equation

$$
u^2+
\left[1+\nu^2(1+2\sin^2\phi_0)\right]u
+\nu^2\cos^2\phi_0=0,
$$

where

$$
u\equiv\frac{\lambda^2}{n^2}.
$$

For $\nu^2>0$ and $\cos^2\phi_0>0$, both roots in $u$ are negative. The retained radial-latitude modes are therefore oscillatory in the reduced model. The along-track phase mode remains neutral. This is a local boundedness result for the branch-specific radial-latitude subsystem, not an asymptotic stability proof, a closed-loop control design, or a swarm-level robustness result. The detailed linearization is given in Appendix B.

# Discussion

## Architectural implication

The support relation can be read as one segment of a broader support continuum:

$$
\phi=0 \rightarrow \text{Keplerian limit},
$$

$$
0<\phi\lesssim1^\circ \rightarrow \text{low-}\beta\text{ stratified support},
$$

$$
\beta\geq1 \rightarrow \text{statite/bubble access threshold}.
$$

The $\beta=1$ crossing of the low-latitude formula is only an extrapolative marker, not a claimed endpoint of the present branch. The value of the model is instead that it makes the lower part of the continuum screenable. A designer can choose a target displacement latitude and read off the required lightness number or allowable system areal density.

This reframes the Dyson-swarm architecture question. In a same-shell Keplerian model, growth is organized around an expanding crossing and phasing problem. In the reduced displaced-support model, growth can instead be posed as layered support geometry: additional bands are placed at small positive and negative latitudes, with explicit normal separation and a calculable support-density cost.

## What the model demonstrates

The present model demonstrates three bounded claims. First, the low-latitude support window is non-empty. Second, the support burden scales approximately linearly with $\phi$ in $\beta_{\min}$ and approximately as $1/\phi$ in $\sigma_{\max}$. Third, the synchronization-constrained branch changes radius but not support burden within the reduced model.

These claims are intentionally narrower than a full mission architecture. They establish a screening relation, representative mass margins, and a local radial-latitude boundedness check. They do not establish the complete engineering feasibility of a Dyson swarm.

## What the model does not demonstrate

The analysis does not provide a complete collision-rate or conjunction-rate model. It does not include finite collector size, mutual shadowing, diffuse reradiation, thermal closure, structural closure, or a power-transmission architecture. It does not include a closed-loop swarm-control law, actuator bandwidth, attitude-error propagation, centre-of-pressure / centre-of-mass passive stability, or station-keeping cost.

The photovoltaic fill-factor estimate is not an optical-power architecture. It is only supported-mass bookkeeping. Once absorbing or power-converting area is modeled as an optically active surface, the radiation-pressure force magnitude, direction, torque environment, and thermal balance must all be recomputed.

## Future work

The next technical step is to restore the exact Sun-line cone-angle force law and propagate the correction through the support curve, local dynamics, and synchronization branch. The second step is to include non-ideal optical coefficients so that thrust efficiency and thrust-direction errors can be separated. The third step is passive and closed-loop stability closure, including centre-of-pressure / centre-of-mass offsets, sail conicity, finite attitude dynamics, and realistic control authority.

At the architecture level, the most useful follow-on work is a conjunction-rate comparison between same-shell Keplerian layered swarms and displaced stratified swarms. That study should use node-intersection count, minimum normal separation, conjunction-corridor density, and reconfiguration burden as explicit metrics rather than relying on the qualitative topology argument used here.

# Conclusion

This paper developed a reduced low-latitude displaced non-Keplerian support model for stratified Dyson-swarm architectures. The central result is the screening relation

$$
\beta_{\min}(\phi)=\frac{3\sqrt3}{2}\sin\phi,
\qquad
\sigma_{\max}(\phi)=\frac{2\sigma^*}{3\sqrt3\sin\phi}.
$$

Representative 1 AU slices show that small displacement latitudes can create large normal separations while remaining well below the $\beta\geq1$ statite/bubble support regime. A synchronization-constrained branch shifts the operating radius without changing the support-density curve in the reduced model. A branch-specific local linearization shows bounded radial-latitude oscillatory modes while leaving the along-track phase mode neutral.

The analysis shows that radiation-pressure-assisted stratification can be expressed as a compact low-latitude screening problem in $\phi$, $\beta$, and $\sigma_{\mathrm{sys}}$. The framework does not close the full engineering problem, but it identifies a mathematically coherent and quantitatively screenable intermediate regime between planar Keplerian swarms and fully radiatively supported bubble/statite concepts.

# Data and Code Availability

The current plotting and numerical scripts are stored in the repository under `Paper/figures/` and `Paper/figures/scripts/`. A frozen public archive should be minted before submission. If a public archive is not yet available at submission time, the manuscript should state that the scripts are available from the author upon reasonable request and will be archived upon acceptance.

# Conflict of Interest

The author declares no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

# CRediT Author Statement

Hao Ke: Conceptualization, Methodology, Formal analysis, Software, Investigation, Writing - original draft, Writing - review and editing, Visualization.

# Declaration of Generative AI and AI-Assisted Technologies

During preparation of this work, the author used AI-assisted drafting and editing tools to help organize prose, compare publication strategies, and identify clarity issues. The author reviewed and edited the content and takes full responsibility for the final manuscript.

# Appendix A: Standard Cone-Angle Check {.unnumbered}

The main text uses a reduced low-latitude cylindrical support model because the paper's architectural claim is concentrated at small displacement angles. A useful check is to compare that screening curve with the standard ideal-specular Sun-line cone-angle convention. Let $\gamma$ be the angle between the sail normal and the local star-spacecraft line, with positive $\gamma$ pitching the thrust toward positive $z$. In the meridional plane, the ideal-sail acceleration components can be written as

$$
a_\rho =
\frac{\mu}{r^2}\beta\cos^2\gamma\cos(\gamma+\phi),
$$

$$
a_z =
\frac{\mu}{r^2}\beta\cos^2\gamma\sin(\gamma+\phi).
$$

Vertical support requires

$$
\beta\cos^2\gamma\sin(\gamma+\phi)=\sin\phi.
$$

At fixed $\phi$, minimizing the required $\beta$ is equivalent to maximizing

$$
F(\gamma,\phi)=\cos^2\gamma\sin(\gamma+\phi).
$$

The stationarity condition gives

$$
2\tan^2\gamma+3\tan\phi\,\tan\gamma-1=0,
$$

so the useful branch is

$$
\tan\gamma_{\mathrm{opt}}
=
\frac{-3\tan\phi+\sqrt{9\tan^2\phi+8}}{4}.
$$

The corresponding exact-cone-angle vertical-support value is

$$
\beta_{\mathrm{cone}}(\phi)
=
\frac{\sin\phi}{F(\gamma_{\mathrm{opt}},\phi)}.
$$

As $\phi\rightarrow0$, $\gamma_{\mathrm{opt}}\rightarrow\arctan(1/\sqrt2)$ and $F\rightarrow2/(3\sqrt3)$, recovering the main-text screening relation as the low-latitude limit.

# Appendix B: Reduced-Branch Linearization {.unnumbered}

For the reduced force model, define

$$
A\equiv\mu\beta\cos^3\alpha_{\mathrm{eff}},
\qquad
B\equiv\mu\beta\cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}}.
$$

The reduced spherical equations are

$$
\ddot r-r\dot\phi^2-r\cos^2\phi\,\dot\theta^2
=
-\frac{\mu}{r^2}
+\frac{A\cos\phi+B\sin\phi}{r^2},
$$

$$
r\ddot\phi+2\dot r\dot\phi+r\sin\phi\cos\phi\,\dot\theta^2
=
\frac{-A\sin\phi+B\cos\phi}{r^2},
$$

$$
r\cos\phi\,\ddot\theta
+2\dot r\cos\phi\,\dot\theta
-2r\sin\phi\,\dot\phi\,\dot\theta
=0.
$$

For the displaced circular solution,

$$
A=\mu\cos\phi_0(1-\nu^2),
\qquad
B=\mu\sin\phi_0,
\qquad
\nu=\frac{\omega}{\sqrt{\mu/r_0^3}}.
$$

Set

$$
r=r_0+\xi,\qquad
\phi=\phi_0+\delta\phi,\qquad
\theta=\omega t+\psi,
$$

and define

$$
q\equiv r_0\delta\phi,\qquad
y\equiv r_0\cos\phi_0\,\psi.
$$

To first order,

$$
\ddot\xi-2\omega\cos\phi_0\,\dot y
=
3n^2\nu^2\cos^2\phi_0\,\xi
-n^2\nu^2\sin\phi_0\cos\phi_0\,q,
$$

$$
\ddot q+2\omega\sin\phi_0\,\dot y
=
-3n^2\nu^2\sin\phi_0\cos\phi_0\,\xi
-n^2(1-\nu^2\sin^2\phi_0)\,q,
$$

$$
\ddot y+2\omega(\cos\phi_0\,\dot\xi-\sin\phi_0\,\dot q)=0.
$$

The third equation integrates once to

$$
\dot y+2\omega(\cos\phi_0\,\xi-\sin\phi_0\,q)=C.
$$

For perturbations with no injected along-track bias, $C=0$, giving the reduced radial-latitude subsystem

$$
\ddot\xi+n^2\nu^2\cos^2\phi_0\,\xi
-3n^2\nu^2\sin\phi_0\cos\phi_0\,q=0,
$$

$$
\ddot q-n^2\nu^2\sin\phi_0\cos\phi_0\,\xi
+n^2(1+3\nu^2\sin^2\phi_0)\,q=0.
$$

Seeking solutions proportional to $e^{\lambda t}$ gives

$$
\begin{aligned}
0={}&
\left(\lambda^2+n^2\nu^2\cos^2\phi_0\right)
\left[\lambda^2+n^2(1+3\nu^2\sin^2\phi_0)\right] \\
&-3n^4\nu^4\sin^2\phi_0\cos^2\phi_0.
\end{aligned}
$$

With $u=\lambda^2/n^2$, this reduces to the main-text quadratic.

