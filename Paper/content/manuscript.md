# Introduction

## Problem setting: topology burden and the missing middle regime

Dyson swarms are often treated as the least structurally extreme stellar-collection concept because they replace a monolithic shell with independent orbiting collectors [Dyson, 1960; Wright, 2020]. The simplification is real, but dense same-shell Keplerian realizations still face a different systems pressure: how a very large collector population can coexist dynamically without turning nodal crossings into a persistent collision-management burden.

In a same-shell Keplerian swarm, every orbital plane passes through the central mass. Any two non-coplanar planes therefore intersect along a pairwise nodal line. For circular or near-circular same-radius shells, that geometry creates path-crossing corridors at the nodes; for eccentric cases, exact path intersection occurs when the nodal radii coincide. For sparse systems this may be tolerable. For dense systems, however, large-constellation collision and debris analyses already show that conjunction risk and debris consequences become system-level management issues rather than isolated operational events (Radtke et al., 2017; Le May et al., 2018). Each added orbital plane then contributes not only collecting area, but also more crossing structure that must be phased, screened, and kept mutually separated.

A minimal scaling makes the burden visible without pretending to compute a Dyson-scale collision probability. If a same-radius swarm uses $P$ distinct orbital planes, the number of pairwise nodal lines scales as

$$
N_{\mathrm{node}}\sim \frac{P(P-1)}{2},
$$

with two antipodal crossing corridors associated with each non-coplanar plane pair. If each plane hosts $M$ collectors, then the bookkeeping for phase separation, exclusion windows, or crossing-pair screening grows with the plane-pair graph rather than merely with the number of planes. This scaling argument is only an architecture-level analogy, not a substitute for a full conjunction-rate model, but it explains why nodal geometry becomes a system design pressure once the swarm is dense.

One may try to mitigate this burden through phase-separated megaconstellation logic, Walker-like symmetry, or radial nesting. Such strategies can delay encounters, redistribute conjunction timing, or move parts of the architecture out of the same-shell case; they simply do not geometrically remove the nodal crossing structure of the dense same-radius multi-plane subset itself. In collector architectures, dense multi-shell nesting may also introduce optical crowding along shared star-centered sightlines, although we do not model that tradeoff here (McInnes, 2026). We therefore use the phrase topology-and-growth pressure in a deliberately limited architectural sense: a dense same-shell Keplerian buildout remains organized around shared nodal corridors, and expanding it generally requires renewed phasing and reconfiguration rather than simple geometric replication.

At the opposite extreme, radiatively supported concepts such as statites or Dyson bubbles eliminate the nodal-intersection problem by abandoning ordinary orbital support altogether. In that regime, radiation pressure must offset gravity directly, driving the system toward the critical areal-density threshold $\sigma^*$ and the corresponding $\beta \geq 1$ access condition for purely radiative-support designs. This endpoint is geometrically attractive but payload-hostile: even modest additions in structure, power, control, or instrumentation rapidly consume the available mass margin. The broader solar-sail literature already provides the immediate dynamical backdrop for this question, from early statite and halo-orbit treatments through families of displaced two-body orbits, displaced non-Keplerian orbit stability studies, and later Earth-/planet-synchronous variants (Forward, 1991; McInnes and Simmons, 1992a,b; McInnes, 1997, 1998; Quarta et al., 2020; Bassetto and Quarta, 2024).

The design region of interest therefore lies between these two limits. The motivating question is whether Dyson architectures should be treated not as discrete shell/swarm/bubble endpoints, but as a continuous support space between a purely orbital swarm and a purely radiative-support bubble/statite configuration.

## Making the continuum explicit through a displaced branch

This paper argues that the continuum sketched above can be made analytically explicit in Dyson-swarm terms. To do so, we develop one concrete displaced branch within it: Micro-Displaced Dyson Swarm (MDDS) configurations in which collectors remain primarily orbital while using a modest solar-radiation-pressure component to sustain small out-of-plane offsets. The objective is not full levitation. It is stratification: replacing one crowded orbital layer with multiple nearby latitude bands that no longer intersect.

Under this interpretation, MDDS is best viewed neither as a conventional Keplerian swarm nor as a near-bubble architecture. Instead, it is a low-$\beta$ intermediate regime inside a broader support continuum. At $\phi = 0$, support is entirely orbital and the configuration reduces to the planar Keplerian limit. As $\phi$ increases, solar-radiation pressure progressively supplements orbital support. At still larger support fractions, one approaches the purely radiatively supported bubble/statite endpoint. The principal conceptual move of the paper is therefore to treat Dyson architectures not as a purely discrete shell/swarm/bubble taxonomy, but as a continuous support-and-stratification spectrum parameterized by quantities such as $\beta$, $\phi$, $\nu$, and $\sigma_{\max}(\phi)$.

The specific branch analyzed here is the low-latitude, low-$\beta$, circular displaced-orbit branch within that broader continuum. In the low-latitude ideal-specular support approximation used as the paper's screening model, the payload-optimized relation is

$$
\beta_{\min}(\phi)=\frac{3\sqrt{3}}{2}\sin\phi,
$$

with the equivalent areal-density limit

$$
\sigma_{\max}(\phi)=\frac{2\sigma^*}{3\sqrt{3}\sin\phi}.
$$

This converts the architecture question into a compact screening problem: whether a candidate system areal density can be supported at a chosen latitude. The contribution is therefore twofold: at the architectural scale, the paper introduces a continuous Dyson support spectrum; at the idealized-physics scale, it develops the low-$\beta$ displaced branch of that spectrum into an explicit intersection between a latitude support curve and a system areal-density budget. The same framework naturally exposes a payload-optimized branch and a synchronization-constrained branch, with the latter treated as a recasting of known synchronous DNKO design space rather than as a new orbit-family claim.

The scope is intentionally narrow. We do not attempt full structural, thermal, control, or economic closure; a formal megaconstellation-reconfiguration analysis; or a complete non-ideal optical model. Nor do we claim a fundamentally new orbit family, first discovery of the displaced-NKO bridge to swarm stratification, or a first general stability analysis of displaced non-Keplerian orbits. The local dynamics result below should instead be read as a branch-specific linearization of the idealized low-latitude support model used here, not as a replacement for the broader DNKO stability literature. The main support curve should therefore be read as a reduced low-latitude architecture-screening relation, not as a complete high-latitude ideal-sail solution or final engineering closure.

## Prior art and claim boundary

The relevant prior-art landscape has two mature branches. The first is the solar-sail and DNKO literature: statites, solar-sail halo orbits, families of displaced two-body orbits, displaced non-Keplerian orbit stability and control, and later synchronous heliocentric variants have all been studied extensively (Forward, 1991; McInnes and Simmons, 1992a,b; McInnes, 1997, 1998; McInnes, 1999; Quarta et al., 2020; Bassetto and Quarta, 2024). The second is the Dyson-swarm / Dyson-bubble literature, which frames stellar collector populations as large-scale engineering or observability problems rather than primarily as orbit-design problems (Dyson, 1960; Wright, 2020; Wright et al., 2015; McInnes, 2025, 2026).

Recent Dyson-focused work narrows the novelty boundary further. In particular, McInnes (2026) explicitly notes that collisions in an orbiting Dyson swarm could in principle be reduced using displaced non-Keplerian orbits whose planes can be stacked in parallel rather than left mutually inclined. That observation is already close to the central geometric move developed here. The remaining question is therefore not whether such a bridge exists in principle, but whether it can be elevated into a compact architecture language with explicit screening variables, a continuum interpretation, and a bounded low-latitude working regime.

The present paper sits between those two literatures. The novelty is not the displaced orbit family itself, but the use of the low-latitude displaced branch as a Dyson-swarm architecture screening relation linking latitude, lightness number, and system areal density. Within that framework, the dynamics contribution is narrower: a branch-specific radial-latitude linearization for the same idealized low-latitude support model.

Figure 1 should be read as the motivating geometric picture for the paper, while the subsequent figures track the local force balance, the architectural translation into stratified rings, the quantitative support curves, and finally the low-latitude examples and synchronization variant.

![Keplerian deadlock and nodal-intersection geometry for dense same-shell swarm configurations. Any two non-coplanar orbital planes passing through the central mass intersect along a pairwise nodal line; for same-radius circular or near-circular shells, those lines become crossing corridors that accumulate as swarm density increases.](figures/concept/keplerian_deadlock.pdf){#fig:keplerian-deadlock}

# Theoretical Framework

This section establishes the minimal analytic framework used throughout the rest of the paper. The objective is not to reproduce the full DNKO literature, but to isolate the specific quantities that make the Dyson-architecture problem screenable: the displacement latitude $\phi$, the lightness number $\beta$, the residual orbital contribution $\nu$, and the equivalent areal-density ceiling $\sigma_{\max}(\phi)$. Once these are written in one compact language, the later architecture discussion and low-latitude examples reduce to interpretation rather than repeated derivation.

## Geometry, kinematics, and force balance

Consider a collector at fixed heliocentric distance $r$ and latitude $\phi$, moving in a circular path about the chosen symmetry axis normal to the reference plane with angular velocity $\omega$. The exact ideal-specular solar-sail convention defines cone angle as the angle between the sail normal and the local star-spacecraft line. Away from the equatorial, small-displacement limit, that convention couples the force components to the spherical geometry through the relative orientation of the sail normal and the radial direction. The compact model used in this paper is therefore more limited: $\alpha_{\mathrm{eff}}$ denotes the effective meridional support pitch used in a low-latitude cylindrical force-balance reduction, and the resulting relations are treated as reduced screening formulae rather than high-latitude exact sail dynamics. Define the orbital-rate ratio

$$
\nu \equiv \frac{\omega}{\sqrt{\mu/r^3}}.
$$

Writing the geometry in cylindrical coordinates gives

$$
\rho = r\cos\phi,\qquad z = r\sin\phi.
$$

In that reduced support model, the radiation-pressure components are written as

$$
a_\rho = \frac{\mu}{r^2}\beta \cos^3\alpha_{\mathrm{eff}},\qquad
a_z = \frac{\mu}{r^2}\beta \cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}},
$$

so the low-latitude force-balance conditions become

$$
\beta \cos^3\alpha_{\mathrm{eff}} = \cos\phi(1-\nu^2),
$$

$$
\beta \cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}} = \sin\phi.
$$

The first equation represents radial unloading of the effective gravitational demand; the second represents the out-of-plane support needed to maintain the displaced orbit. These equations should not be read as a full high-latitude ideal-sail force law. In the standard Sun-line cone-angle formulation, the exact components include the relative geometry between the sail normal and the local star-spacecraft line. The present paper keeps the reduced cylindrical form because the engineering examples and screening use cases are concentrated at $\phi\lesssim1^\circ$, where Appendix A shows that the corresponding standard cone-angle correction is only a few per cent.

Read mechanically, these equations simply restate the familiar displaced-orbit balance. Read architecturally, however, they do something more useful: they separate the support burden into an orbital contribution and a radiative contribution. That separation is what allows the present paper to talk about mixed-support Dyson architectures as points within a continuum rather than as members of disconnected conceptual categories.

![Local force balance for a displaced MDDS element in meridional section. In the co-rotating view, sail thrust, stellar gravity, and the orbital centrifugal term close as a three-vector balance; equivalently, in the inertial view, sail thrust plus gravity produce the centripetal demand toward the offset-disk center.](figures/concept/force_balance.pdf){#fig:force-balance}

Figure 3 is intended to visualize this displaced geometry at the architectural level, while the later quantitative figures capture the resulting low-latitude support curves and example design slices in compact form.

![MDDS concept: low-latitude stratified rings above and below a reference orbital plane. Collectors use modest radiation pressure to maintain small out-of-plane displacements, creating non-intersecting latitude bands.](figures/concept/mdds_stratified_rings.pdf){#fig:mdds-rings}

## The low-latitude optimized branch

At fixed $\phi$, the most important engineering objective is usually to maximize the mass budget available to the system. Since $\beta = \sigma^*/\sigma$ for an ideal reflector (McInnes, 1999), this is equivalent to minimizing the required $\beta$. Within the reduced low-latitude support model above, optimizing the effective support pitch gives

$$
\alpha_{\mathrm{eff,opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right),
$$

and the reduced low-$\beta$ screening relation

$$
\beta_{\min}(\phi)=\frac{3\sqrt{3}}{2}\sin\phi.
$$

The corresponding residual orbital contribution in the same reduced model is

$$
\nu^2 = 1-\sqrt{2}\tan\phi,
$$

used here only within the low-latitude regime where the approximation is meant to apply.

This is the central analytic screening relation used throughout the paper. Within the broader and well-established DNKO framework, it functions here as the specialization that makes the Dyson-swarm architecture question legible in closed form at low latitude. The underlying maximum transverse-force geometry is not introduced here from scratch; related optimal-angle results are already well established in displaced-orbit and solar-sail trajectory literature (Simo and McInnes, 2010; Wawrzyniak and Howell, 2011). The specific role of the present paper is to recast that known low-latitude support geometry into the explicit support curve $\beta_{\min}(\phi)$ and then into the architecture criterion $\sigma_{\text{sys}} < \sigma_{\max}(\phi)$. The result shows that the displaced-orbit requirement grows linearly with latitude at small angles, but with a nontrivial prefactor that makes the requirement meaningfully stricter than naive heuristic estimates.

The same result can be rewritten as a limit on allowable system areal density:

$$
\sigma_{\max}(\phi)=\frac{\sigma^*}{\beta_{\min}(\phi)}
=\frac{2\sigma^*}{3\sqrt{3}\sin\phi}.
$$

The architecture question therefore reduces to a single criterion:

$$
\sigma_{\text{sys}} < \sigma_{\max}(\phi).
$$

Here $\sigma_{\text{sys}}$ means total supported system mass divided by the effective optical area that actually participates in the radiation-pressure support. It is therefore not only the reflector film loading: structure, payload, attitude hardware, power conversion, communications, deployment margin, and redundancy all belong in the numerator whenever they are carried by the supported element.

Equivalently, within the low-latitude screening model, a system of known areal density $\sigma_{\text{sys}}$ has a corresponding latitude estimate

$$
\phi_{\max}=\arcsin\left(\frac{2\sigma^*}{3\sqrt{3}\,\sigma_{\text{sys}}}\right).
$$

provided the arcsin argument does not exceed unity. Because the expression is a low-latitude model rather than a full high-latitude ideal-sail branch, the practical screening cap should be read as

$$
\phi_{\max}^{\mathrm{screen}}
=
\min\left[
\phi_{\mathrm{LL}},
\arcsin\left(\frac{2\sigma^*}{3\sqrt{3}\,\sigma_{\text{sys}}}\right)
\right],
$$

where $\phi_{\mathrm{LL}}$ is the chosen validity limit for the low-latitude approximation or the limit imposed by a later exact force-law treatment. In the numerical examples below, the main claimed low-latitude working regime is taken to be $\phi\leq1^\circ$, while $\phi=2^\circ$ is retained only as an outer stress comparison. One may therefore begin with a target latitude and ask what areal density is supportable there, or begin with a candidate system areal density and ask how far from the reference plane it can be stratified within the low-latitude regime. In that sense the same relation serves both as a design equation and as a screening equation, but not as a universal maximum-latitude bound for the full support continuum.

## Dyson support continuum

The support curve above is not only a local orbit result. In the present paper it is used to parameterize a broader Dyson support continuum. At one end lies the planar Keplerian swarm limit, where support is entirely orbital. At the other lies the purely radiatively supported bubble/statite endpoint, where orbital support vanishes. Between them lies a continuous family of mixed-support configurations, of which the low-$\beta$ branch analyzed here is a payload-tolerant segment.

This continuum is not meant to erase engineering differences between swarm-like and bubble-like systems. It is meant to supply a common parameterization for them. In the language of the present framework, the key coordinates along that support spectrum are the lightness number $\beta$, the latitude or off-plane angle $\phi$, the residual orbital contribution $\nu$, and the equivalent areal-density ceiling $\sigma_{\max}(\phi)$. Once written this way, the familiar Dyson categories become interpretable as distinct regions of one support space rather than as isolated conceptual islands.

It is useful to distinguish two different threshold notions within that continuum. The familiar $\beta = 1$ threshold remains an important architectural boundary: once a civilization can build collectors with $\beta \geq 1$, purely radiatively supported bubble/statite-like configurations enter the admissible design space. The low-latitude MDDS screening relation, however, is not intended to define where the full ideal-sail displaced branch terminates or how it connects to a statite at high latitude. Extending the model into that regime requires restoring the standard Sun-line cone-angle geometry and re-solving the force balance. In the present paper, the $\beta=1$ crossing of the low-latitude formula is therefore only an extrapolative marker, not a claimed physical endpoint.

The three markers used here are correspondingly modest:

- **Planar Keplerian limit:** $\phi = 0$, with $\beta_{\min} = 0$ and $\nu = 1$. The support demand for off-plane displacement vanishes, even though a real collector may still have nonzero optical lightness. Support is purely orbital and there is no off-plane displacement.
- **Low-latitude MDDS working segment:** $0<\phi\lesssim\phi_{\mathrm{LL}}$, where $\phi_{\mathrm{LL}}$ denotes the chosen low-latitude validity limit. In this region, the support demand is approximated by $\beta_{\min}(\phi)=\frac{3\sqrt{3}}{2}\sin\phi$ and the architecture is mostly orbital with modest radiative assistance.
- **Bubble/statite access threshold:** $\beta\geq1$ remains the conventional gateway to purely radiative-support concepts, but it belongs to the broader continuum rather than to a high-latitude continuation claimed for the low-latitude approximation.

For orientation only, the low-latitude formula would reach

$$
\beta_{\min}(\phi)=1
\quad\Rightarrow\quad
\phi_{\beta=1}=\arcsin\left(\frac{2}{3\sqrt{3}}\right)\approx 22.638^\circ,
$$

but that number lies well outside the low-latitude examples emphasized below and is not used as an endpoint claim. The point of retaining it is simply to show how far the representative MDDS slices are from the traditional full-radiative-support threshold.

![Latitude support curves in the low-latitude regime. Left: $\beta_{\min}(\phi)$ showing the required lightness number. Right: $\sigma_{\max}(\phi)$ showing the maximum allowable system areal density. Reference values at $0.1^\circ$, $0.5^\circ$, and $1^\circ$ illustrate the rapid tightening of the feasibility window with increasing latitude.](figures/results/support_curves.pdf){#fig:support-curves}

## The synchronization-constrained branch

The same reduced force-balance framework also admits a second natural design objective. Instead of minimizing $\beta$ at fixed $\phi$, one may impose an external timing requirement, such as Earth-synchronous heliocentric motion. In that case the angular velocity is fixed by the external period constraint, and the displaced orbit adjusts its radius accordingly. This branch is already recognizable within the DNKO literature and is included here as an operationally meaningful variant of the same architecture framework rather than as a new orbit family in its own right (Heiligers and McInnes, 2015; Quarta et al., 2020; Bassetto and Quarta, 2024).

For an Earth-synchronous condition with reference radius $a_\oplus$,

$$
r_{\text{sync}}(\phi,\alpha_{\mathrm{eff}})=a_\oplus\left(1-\frac{\tan\phi}{\tan\alpha_{\mathrm{eff}}}\right)^{1/3}.
$$

Taking the low-latitude optimized support pitch gives the approximate screening relation

$$
r_{\text{sync}}(\phi)=a_\oplus\left(1-\sqrt{2}\tan\phi\right)^{1/3}.
$$

An important consequence follows in the low-latitude approximation: the synchronization constraint modifies the orbital radius, but does not by itself alter the support curve $\beta_{\min}(\phi)$ or the equivalent density limit $\sigma_{\max}(\phi)$. In other words, synchronization is primarily a geometric and operational constraint rather than an additional support penalty within this idealized slice. Within the continuum view, it should therefore be read as a way of slicing the same support space under an additional temporal-organization requirement, not as a separate dynamical family.

That distinction matters for how the branch is interpreted later in the paper. The low-latitude optimized branch answers the question, "What is the most mass-efficient way to support a chosen latitude within this screening model?" The synchronization-constrained branch answers a different question: "What geometric adjustment is required if regular timing or common angular rate is imposed from outside?" These are different cuts through the same support space, not competing definitions of the architecture itself.

## Local radial-latitude dynamics

The support curve above establishes the low-latitude displaced branch, but not its nearby open-loop dynamical character. To obtain a branch-specific local boundedness check for the same idealized support model, write the heliocentric dynamics in spherical variables $(r,\phi,\theta)$ and decompose the reduced radiation-pressure force into effective cylindrical support coefficients

$$
A \equiv \mu\beta\cos^3\alpha_{\mathrm{eff}},\qquad
B \equiv \mu\beta\cos^2\alpha_{\mathrm{eff}}\sin\alpha_{\mathrm{eff}}.
$$

The effective coefficients $A$ and $B$ are assumed to be held at their nominal commanded values by attitude control and to scale as $1/r^2$ through the prefactors in the equations below. Finite attitude dynamics, actuator bandwidth, and the question of whether the support vector passively follows a perturbed local radial direction are outside this linearization.

The equations of motion for this reduced force model are then

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

For the displaced circular solution $(r_0,\phi_0,\dot\theta=\omega)$, these reduce to

$$
A=\mu\cos\phi_0(1-\nu^2),\qquad
B=\mu\sin\phi_0,\qquad
\nu=\frac{\omega}{\sqrt{\mu/r_0^3}}.
$$

Now set

$$
r=r_0+\xi,\qquad
\phi=\phi_0+\delta\phi,\qquad
\theta=\omega t+\psi,
$$

and define the length-like perturbations

$$
q \equiv r_0\,\delta\phi,\qquad
y \equiv r_0\cos\phi_0\,\psi.
$$

To first order, the local dynamics become

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
\ddot y+2\omega(\cos\phi_0\,\dot\xi-\sin\phi_0\,\dot q)=0,
$$

with $n=\sqrt{\mu/r_0^3}$.

The third equation integrates once to

$$
\dot y+2\omega(\cos\phi_0\,\xi-\sin\phi_0\,q)=C,
$$

where $C$ is the conserved along-track phase/angular-momentum offset. For perturbations with no injected along-track bias, $C=0$, and the radial-latitude subsystem reduces to

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
0={}&\left(\lambda^2+n^2\nu^2\cos^2\phi_0\right)
\left[\lambda^2+n^2(1+3\nu^2\sin^2\phi_0)\right] \\
&-3n^4\nu^4\sin^2\phi_0\cos^2\phi_0.
\end{aligned}
$$

Writing $u\equiv\lambda^2/n^2$ yields the compact quadratic

$$
u^2+\left[1+\nu^2(1+2\sin^2\phi_0)\right]u+\nu^2\cos^2\phi_0=0.
$$

For any low-latitude operating point retained in the model with $\nu^2>0$ and $\cos^2\phi_0>0$, both roots satisfy $u<0$. The two nontrivial radial-latitude modes are therefore oscillatory, with frequencies

$$
\begin{aligned}
\omega_\pm^2
&=
\frac{n^2}{2}
\left[
1+\nu^2(1+2\sin^2\phi_0)
\right. \\
&\qquad \left.
\pm
\sqrt{
\left(1+\nu^2(1+2\sin^2\phi_0)\right)^2
-4\nu^2\cos^2\phi_0
}
\right].
\end{aligned}
$$

This yields a bounded open-loop $r$-$\phi$ response for the idealized low-latitude support model used here. The along-track degree of freedom remains neutral through the conserved constant $C$, so this is not a proof of passive asymptotic self-restoration or swarm-scale stability; it is a local boundedness result for the coupled radial-latitude subsystem within the reduced branch model.

The same framework also clarifies why $\phi$- and $r$-perturbations represent different kinds of design burden. Along the low-latitude screening branch,

$$
\frac{\delta\beta_{\min}}{\beta_{\min}}
=
\cot\phi_0\,\delta\phi,
$$

so latitude errors directly perturb the support demand. By contrast, the equilibrium family remains scale-free in radius, and the neighboring circular solution instead shifts its orbital rate according to

$$
\frac{\delta\omega}{\omega}
=
-\frac{3}{2}\frac{\delta r}{r_0}.
$$

Thus $r$ errors act primarily as orbital-rate mismatch rather than as a first-order change in the underlying support threshold.

## Assumptions

The present analysis adopts an ideal-specular sail as the motivating optical limit, but it uses only the low-latitude support approximation defined above rather than a full high-latitude Sun-line cone-angle force law. Appendix A gives a short standard cone-angle check showing that the reduced screening curve is conservative at the representative low-latitude examples. The reflector is treated as the sole optically active support surface. Payload elements enter through the aggregate system areal density $\sigma_{\mathrm{sys}}$, defined as total supported mass divided by the effective optical area that provides radiation-pressure support. This support area should not be conflated with energy-collecting area: if power hardware absorbs, shadows, reradiates, or redirects light over the support surface, it changes both the energy budget and the radiation-pressure vector. The results should therefore be read as an ideal baseline framework rather than as a complete optical-realism, payload-coupled, or control-closure model. This matters especially for MDDS because non-ideal optical behavior can perturb not only thrust magnitude but also force direction, thereby shifting the practical support curve away from the ideal limit (Dachwald et al., 2005; Wawrzyniak and Howell, 2011).

# Illustrative Slices of the Low-Latitude Branch

The role of this section is deliberately limited. It does not attempt a full engineering closure, and it is not intended to bear the paper's main novelty claim. Its purpose is narrower and more practical: to show that the continuum established in Section 2 contains a real low-$\beta$ operating window, to attach representative scales to that window, and to illustrate how the analytic criterion behaves when confronted with lightweight spacecraft-style areal-density bookkeeping.

## Representative latitudes

To demonstrate the feasibility window opened by the MDDS continuum, we evaluate the support relations at four representative points: the Earth-angular-radius characteristic angle $\phi = \theta_\oplus \approx 0.00244^\circ$, followed by $\phi = 0.1^\circ$, $\phi = 0.5^\circ$, and $\phi = 1^\circ$. The sharper contraction by $\phi = 2^\circ$ is retained only as an outer comparison point.

Using $\sigma^* \approx 1.53\ \mathrm{g\,m^{-2}}$, the support curve gives

$$
\beta_{\min}(\theta_\oplus)\approx 1.11\times 10^{-4},\qquad \sigma_{\max}(\theta_\oplus)\approx 13.83\ \mathrm{kg\,m^{-2}},
$$

$$
\beta_{\min}(0.1^\circ)\approx 0.00453,\qquad \sigma_{\max}(0.1^\circ)\approx 337.4\ \mathrm{g\,m^{-2}},
$$

$$
\beta_{\min}(0.5^\circ)\approx 0.0227,\qquad \sigma_{\max}(0.5^\circ)\approx 67.5\ \mathrm{g\,m^{-2}},
$$

$$
\beta_{\min}(1.0^\circ)\approx 0.0453,\qquad \sigma_{\max}(1.0^\circ)\approx 33.8\ \mathrm{g\,m^{-2}}.
$$

These values are sufficient for the limited purpose of the section: to show that the low-latitude window is real, but tightens rapidly, approximately as $1/\phi$ in the small-angle limit. In particular, the $\theta_\oplus$ point shows that the continuum already has a near-entry regime at the scale of one Earth radius of normal displacement at 1 AU.

Taken together, these points form a deliberately uneven staircase of difficulty. The $\theta_\oplus$ case marks the near-entry edge of the continuum; $0.1^\circ$ shows a regime that is already geometrically large yet still mass-per-area permissive; $0.5^\circ$ and $1^\circ$ then illustrate how quickly the mass budget begins to tighten once one asks for more ambitious stratification. The value of the set is therefore comparative rather than exhaustive.

![Low-latitude feasibility window showing maximum supportable areal density $\sigma_{\max}$ at representative latitudes on a logarithmic axis. Even the entry-level $0.1^\circ$ case already produces substantial geometric separation while remaining far more permissive in areal-density terms than the better-known high-latitude or bubble limits.](figures/results/low_latitude_window.pdf){#fig:low-latitude-window}

## Entry-level interpretation

Even very small latitudes correspond to very large geometric separations at 1 AU. At $\phi = 0.1^\circ$, the out-of-plane displacement is already about $2.61\times 10^5$ km. Comparing to $\theta_\oplus$, a $0.1^\circ$ MDDS displacement corresponds to about $41$ Earth radii of off-plane separation, while $0.5^\circ$ and $1^\circ$ correspond to about $205$ and $410$ Earth radii respectively. The point of MDDS is not to achieve dramatic angular offsets; it is to obtain enormous spatial stratification from modest angular displacements while staying well below the full radiative-support threshold.

This Earth-angle comparison also suggests a natural entry-level characteristic angle for the framework itself. At $\phi = \theta_\oplus$, the support threshold $\sigma_{\max}(\theta_\oplus)\approx 13.83\ \mathrm{kg\,m^{-2}}$ is already well within the broad range of present human spacecraft materials and systems. Geometrically, it corresponds to an out-of-plane separation of approximately one Earth radius, $z \approx 6{,}371\ \mathrm{km}$. If one additionally imposes Earth-synchronous motion on the low-latitude optimized branch, the corresponding inward radius correction is only about $3.0\times 10^3\ \mathrm{km}$. The significance of this point is not that it solves the full MDDS engineering problem, but that it shows the continuum has a genuinely near-entry regime rather than only a distant futuristic one.

This is the sense in which MDDS differs from both comparison endpoints. Relative to a Keplerian swarm, it sacrifices some mass and energy margin in exchange for non-intersecting stratification. Relative to a statite or bubble concept, it remains far from the $\beta \geq 1$ regime and therefore preserves a much larger payload budget.

## Order-of-magnitude engineering slices

The low-latitude framework becomes more concrete when coupled to a minimal areal-density bookkeeping exercise. Consider an illustrative decoupled node composed of an ultralight reflector and a photovoltaic payload with fill factor $\lambda = A_{\mathrm{pv}}/A_{\mathrm{refl}}$. In this bookkeeping convention, $\sigma_{\mathrm{sys}}$ is the total mass carried by the supported node divided by the reflector's effective radiation-pressure support area. To first order,

$$
\sigma_{\mathrm{sys}} = \sigma_{\mathrm{refl}} + \lambda \sigma_{\mathrm{pv}},
$$

with all second-order structural and control terms deliberately left outside the main-text estimate. In keeping with the modeling scope of this paper, the photovoltaic payload is treated here as added mass rather than as a second optically resolved surface. The PV fill-factor estimate is a mass-budget illustration only, not a closed optical-power architecture: real PV area would absorb, reflect, reradiate, shadow, and torque the element in ways that alter the radiation-pressure force magnitude and direction.

Using a light reflector benchmark of $\sigma_{\mathrm{refl}} \approx 5\ \mathrm{g\,m^{-2}}$ and an optimistic ultralight PV benchmark of $\sigma_{\mathrm{pv}} \approx 54.8\ \mathrm{g\,m^{-2}}$, the support curve immediately implies approximate low-latitude fill-factor limits. The PV number is converted from the device-level flexible InGaP/GaAs tandem-cell result of Kim et al. (2021), which reports $27.4\%$ efficiency and specific power exceeding $5000\ \mathrm{W\,kg^{-1}}$ under an AM1.5G spectrum; it should not be read as a space-qualified module loading including wiring, deployment, interconnects, thermal hardware, or radiation margin.

- at $0.1^\circ$, the ideal areal-density budget no longer constrains $\lambda$ below unity
- at $0.5^\circ$, the same is still true to first order
- at $1^\circ$, the bookkeeping gives $\lambda_{\max} \approx 0.53$

These numbers are useful because they convert an abstract support curve into a design-language statement. Instead of asking only whether a latitude is mathematically supportable, one can ask how much mass-budget photovoltaic fill or payload fraction survives once a reflector benchmark is specified. That translation from support relation to payload fraction is one of the simplest ways to make the continuum operationally legible, but it is not an optically validated PV coverage fraction.

These values show how the support curve translates directly into a shrinking payload fraction as latitude rises, even before heavier structural realism is introduced. In particular, the $0.1^\circ$ point is useful because $\sigma_{\max} \approx 337\ \mathrm{g\,m^{-2}}$ is no longer an obviously exotic areal-density threshold. In pure mass-per-area terms, this entry-level low-latitude regime approaches a domain that contemporary lightweight spacecraft can plausibly inhabit. By contrast, $0.5^\circ$ and especially $1^\circ$ already demand materially lighter systems than those demonstrated by current flown sailcraft (Macdonald and McInnes, 2011; Mansell et al., 2023).

That interpretation becomes sharper if one compares directly against flown or near-flight sailcraft. LightSail 2 combined a roughly $5\ \mathrm{kg}$ CubeSat-class spacecraft with a deployed sail area of $32\ \mathrm{m^2}$, corresponding to a mission-level loading of about $156\ \mathrm{g\,m^{-2}}$ (Mansell et al., 2023). NEA Scout, at less than $14\ \mathrm{kg}$ and about $86\ \mathrm{m^2}$ of sail area, falls in a similar range, roughly $160\ \mathrm{g\,m^{-2}}$ (Johnson et al., 2017). These benchmarks sit far below the $\theta_\oplus$ and $0.1^\circ$ support thresholds, but well above $\sigma_{\max}(1^\circ)$. This is precisely why the current paper frames the low-angle window as non-empty yet rapidly narrowing: the extreme entry regime already overlaps current lightweight sailcraft capability in mass-per-area terms, while the more ambitious low-degree regime remains significantly ahead of present integrated system practice.

## Synchronization slice

The synchronization-constrained branch is also easy to interpret numerically in the low-latitude regime. On the low-latitude optimized branch, the Earth-synchronous radius correction is small but non-negligible:

- at $0.1^\circ$, $r_{\mathrm{sync}} \approx 0.99918\ \mathrm{AU}$, corresponding to an inward shift of about $0.12$ million km
- at $0.5^\circ$, $r_{\mathrm{sync}} \approx 0.99587\ \mathrm{AU}$, corresponding to an inward shift of about $0.62$ million km
- at $1^\circ$, $r_{\mathrm{sync}} \approx 0.99170\ \mathrm{AU}$, corresponding to an inward shift of about $1.24$ million km

This is useful for interpretation because it reinforces the distinction between the two design branches. The support requirement is still controlled by $\beta_{\min}(\phi)$ and $\sigma_{\max}(\phi)$; synchronization mainly alters where the ring sits, not whether the latitude is supportable in the first place.

![Earth-synchronous radius correction along the low-latitude optimized branch. The inward shift from 1 AU grows with latitude but does not alter the fundamental support curve in the reduced screening model; synchronization is an operational geometry constraint, not an additional support penalty.](figures/results/sync_radius.pdf){#fig:sync-radius}

For contrast, the same support curve yields only $\sigma_{\max}(2^\circ)\approx 16.9\ \mathrm{g\,m^{-2}}$, showing how quickly the margin contracts once one moves beyond the entry-level low-latitude regime. The low-latitude slices therefore identify a real but rapidly narrowing low-$\beta$ operating window in which large geometric stratification appears before the architecture reaches the fully radiative-support limit.

# Discussion

The main architectural consequence of the framework is that the central question changes. Instead of asking whether a displaced ring is intuitively plausible, one asks whether a system of areal density $\sigma_{\text{sys}}$ lies below the support curve $\sigma_{\max}(\phi)$. Once written this way, the architecture becomes analyzable, comparable, and extensible. The contribution is therefore not a new orbit family, but a change of design language: from static shell/swarm/bubble end states to a support space with explicit intermediate regimes, screening variables, and transition thresholds.

In that language, MDDS exposes one previously under-articulated region of Dyson design space: a low-$\beta$ regime in which collector populations remain mostly orbital yet already acquire a qualitatively different topology from a dense same-shell Keplerian swarm. The framework does not claim that shell-like, swarm-like, and bubble-like constructs are engineeringly equivalent. It claims that they can be parameterized within a common support logic while retaining sharply different payload, control, and deployment consequences in different regions of that space.

## Growth path and deployment logic

MDDS shifts the organizing variable from the management of an expanding intersection network to the design of a layered support geometry. In the low-latitude regime, added capacity is expressed as additional latitude bands and, on the synchronization-constrained branch, as bands whose angular rates can be kept nearly common through modest radius adjustments. The immediate effect is a change in interaction geometry: from repeated line-of-node crossings to separated layers with explicit normal spacing and operationally regular motion.

Since the support curve is most permissive near the reference orbital plane, the framework naturally suggests a staged reading: low-latitude bands first, higher latitudes later as areal density improves. The low-angle examples sharpen the point that even very small angular displacements already produce large geometric separations in the Sun-Earth environment. A natural next-step metric family would therefore include node-intersection count, minimum normal separation, conjunction-corridor density, and reconfiguration burden under staged expansion.

The same staged-growth logic also suggests a limited observational hypothesis: over part of its buildout history, an MDDS-like system may look closer to an organized circumstellar disk than to the canonical shell-like image of a Dyson sphere. That possibility is worth noting, but radiative-transfer modeling and observational discriminants belong to a later layer of analysis.

## Modeling boundaries

The most immediate realism layers are optical non-idealities, stability, and structural closure. For purely radial radiative-support concepts, optical non-idealities primarily act as thrust-efficiency penalties. For MDDS, by contrast, non-ideal optical behavior can also perturb the effective force direction because the displaced configuration relies on a specific vector decomposition of radiation pressure. The closed-form support curve used here is therefore best understood as a low-latitude ideal reference screen that later optical-realism studies should rederive or correct, not as a final high-latitude force-law result.

Long-term maintainability is the next major boundary. The broader DNKO literature has already shown that displaced orbits can include marginally stable or unstable subfamilies under open-loop dynamics, and that linear state feedback can be used to stabilize such configurations in practice (McInnes, 1998; Bookless, 2006). The present manuscript contributes a narrower, branch-specific result for the idealized low-latitude MDDS support model: the coupled $r$-$\phi$ subsystem is oscillatory for operating points in the retained low-latitude domain with $\nu^2>0$, while the along-track phase degree of freedom remains neutral. That result is encouraging but intentionally limited. It is not a first general stability analysis of displaced orbits, and it does not yet include passive-stability offsets, centre-of-pressure/centre-of-mass coupling, finite-sail attitude dynamics, optical non-idealities, mutual shadowing, or swarm-scale feedback design.

A recent complementary result also suggests a useful, if necessarily indirect, consistency check across neighboring idealized models. In the extended-reflector limit $R \gg R_{*}$, McInnes (2026) derives a stability ceiling $\overline{\beta}_{S}(\overline{\xi})$ for circular orbits of large reflective discs and shows that stable orbits exist only for $\overline{\beta}<\overline{\beta}_{S}$ (McInnes, 2026). That is not the same dynamical regime as the present MDDS model, which treats the opposite small-sail displaced-orbit limit $R_{*} \gg R$ familiar from the non-point-source radiation-pressure analysis of McInnes and Brown (1990), so the result cannot be imported as a formal proof or stability bound. Still, the representative low-latitude cases used in this paper have very small lightness numbers, such as $\phi=0.1^\circ$ with $\beta_{\min}\approx4.53\times10^{-3}$ and $\phi=1^\circ$ with $\beta_{\min}\approx4.53\times10^{-2}$, far below order-unity radiative-support thresholds. The correct reading is limited: this comparison is only a consistency check across neighboring idealized models, not a stability proof for MDDS.

## Scope and next steps

After this McInnes-style consistency check, the most natural next step is no longer to make stronger claims from the reduced model, but to extend it toward exact force-law, passive-stability, and closed-loop closure. Beyond the local $r$-$\phi$ result derived here, the unfinished agenda is now fairly clear: restore the standard Sun-line cone-angle ideal-sail geometry; move beyond the point-sail limit; make passive stability explicit through centre-of-pressure/centre-of-mass offsets, sail conicity, and mass distribution; close the structural problem under differential loading and in-plane stress; and add collective effects such as mutual attenuation, self-shadowing, diffuse reradiation, and secular optical drift.

Stated compactly, McInnes (2026) does not collapse the MDDS framework claim so much as sharpen its next obligations: once low-$\beta$ supportability is shown, the decisive follow-on question is how much passive stability, structural closure, and collective robustness survives after the ideal point-sail abstraction is progressively relaxed.

The appropriate claim at this stage is therefore limited but substantive: the framework is mathematically coherent, physically interpretable, and non-empty in the low-latitude regime. If later work adds optical realism, explicit control closure, deployment economics, and traffic-style growth metrics, those additions would extend the present framework rather than replace its central architectural claim.

# Conclusion

This paper has argued that a major systems pressure in dense same-shell Keplerian Dyson swarms is not only collector abundance, but same-shell crossing topology, while fully radiatively supported bubble/statite concepts resolve that geometry only at severe areal-density cost. The main result is to make the middle regime explicit. By treating Dyson architectures as a continuous support spectrum and then developing its low-$\beta$ displaced branch, we obtained the reduced low-latitude screening relation $\beta_{\min}(\phi)=\frac{3\sqrt{3}}{2}\sin\phi$ and the corresponding density ceiling $\sigma_{\max}(\phi)=\frac{2\sigma^*}{3\sqrt{3}\sin\phi}$. In that form, the architecture question becomes a screening problem in latitude and areal density rather than a purely qualitative contrast between swarm and bubble endpoints. The representative Sun-Earth slices at $\theta_\oplus$, $0.1^\circ$, $0.5^\circ$, and $1^\circ$ then show that this continuum is non-empty in a genuinely low-latitude regime, where very small angular displacements already create large normal separations before the architecture approaches the fully radiative-support limit.

The architectural significance is that Dyson growth can be described in terms of layered support geometry, synchronization choices, and staged latitude expansion rather than only as the management of increasingly dense same-shell crossing structure. On that reading, MDDS is best understood as an analytic entry segment of a broader Dyson support continuum: not the whole design space, but the first part of it that can be written compactly and screened quantitatively. A branch-specific local radial-latitude linearization derived here shows bounded open-loop $r$-$\phi$ response for the idealized low-latitude support model while retaining a neutral along-track phase mode. The next step is therefore not to restate the framework, but to test how much of it survives once the idealizations are relaxed, beginning with an exact Sun-line cone-angle force law, passive and closed-loop stability closure, optical realism, structural closure, and collective swarm effects.

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

Vertical support then requires

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

As $\phi\rightarrow0$, $\gamma_{\mathrm{opt}}\rightarrow\arctan(1/\sqrt{2})$ and $F\rightarrow 2/(3\sqrt{3})$, recovering the main-text screening relation

$$
\beta_{\min}(\phi)=\frac{3\sqrt{3}}{2}\sin\phi
$$

as the low-latitude limit. Over the representative examples used in the paper, this reduced relation slightly overestimates the cone-angle value of $\beta_{\min}$ and is therefore conservative as a screening rule. At $0.1^\circ$, $\beta_{\mathrm{cone}}=0.004523$ while the reduced screen gives $0.004535$, an overestimate of $0.25\%$. At $0.5^\circ$, the corresponding values are $0.02240$ and $0.02267$, an overestimate of $1.24\%$. At $1.0^\circ$, they are $0.04425$ and $0.04534$, an overestimate of $2.48\%$.

This appendix does not replace the future full force-law and stability rederivation. Its limited purpose is to show that, for the low-latitude slices carrying the present architecture argument, the reduced cylindrical screening curve differs from the standard ideal-specular cone-angle treatment by only a few per cent and errs on the conservative side.
