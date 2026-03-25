# Introduction

## Dyson swarms and the orbital topology-and-growth problem

Dyson structures remain one of the clearest thought experiments for stellar-scale energy harvesting, dating back to Dyson's original argument that sufficiently advanced civilizations may reprocess an appreciable fraction of stellar luminosity into distributed artificial collectors [Dyson, 1960]. Among the usual taxonomy of shell, swarm, and bubble concepts, the swarm is generally regarded as the least structurally extreme because it replaces a monolithic shell with a distributed population of independent collectors. However, that apparent simplification leaves a different difficulty unresolved: how a very large number of collectors can coexist dynamically at similar heliocentric radii without creating an increasingly pathological collision environment.

In a conventional Keplerian swarm, every orbital plane must pass through the central mass. As a result, non-coplanar orbits at comparable radii generically intersect at nodes. For sparse systems this may be tolerable; for dense systems it becomes a structural limitation rather than an operational detail, as modern large-constellation collision and debris analyses have repeatedly emphasized (Radtke et al., 2017; Le May et al., 2018). Each added orbital plane contributes not only more collecting area, but also more geometric crossing corridors and thus more topology burden. In that sense, the difficulty is not merely that conjunction probability rises locally; it is that the architecture becomes organized around an expanding network of nodal bottlenecks.

One may try to manage this burden through phase-separated megaconstellation logic, Walker-like symmetry, or radial nesting. Such strategies can delay encounters, redistribute conjunction timing, or spread traffic across more than one crossing corridor. But they do not geometrically remove the underlying intersections. More importantly for a civilization-scale buildout, they are naturally described for fixed constellation parameters rather than open-ended growth (Walker, 1971; de Weck et al., 2004; Lee et al., 2018; Lee et al., 2025). Once the number of planes, nodes, or phasing relationships changes, the symmetry on which the configuration relied is generically disturbed. We do not attempt a formal reconfiguration-cost analysis here, but the architectural implication is already clear: the Keplerian difficulty is not only a collision problem, but also a topology-and-growth problem.

This is the Dyson-scale problem that motivates the paper. The aim is not merely to identify another solar-sail operating point. It is to ask whether the usual Dyson taxonomy itself is too coarse. If collector populations can transition continuously from purely orbital support to partially radiative support and eventually to fully radiatively supported configurations, then shell/swarm/bubble categories are not just alternative labels for separate end states; they are regions within a larger support space. On that reading, the right theoretical object is not a single favored architecture, but a continuous design spectrum with identifiable working segments and engineering boundaries.

## The gap between Keplerian swarms and radiative-support concepts

At the opposite extreme, radiatively supported concepts such as statites or Dyson bubbles eliminate the nodal-intersection problem by abandoning ordinary orbital support altogether. In that regime, radiation pressure must offset gravity directly, driving the system toward the critical areal-density threshold $\sigma^*$ and the corresponding $\beta \geq 1$ access condition for purely radiative-support designs. This endpoint is geometrically attractive but payload-hostile: even small additions in structure, power, control, or instrumentation quickly exhaust the available mass margin. The broader solar-sail literature already provides the immediate dynamical backdrop for this discussion, from early statite and halo-orbit treatments through families of displaced two-body orbits, displaced non-Keplerian orbit stability studies, and later Earth-/planet-synchronous variants (Forward, 1991; McInnes and Simmons, 1992a,b; McInnes, 1997, 1998; Quarta et al., 2020; Bassetto and Quarta, 2024).

This suggests that the most interesting design region may lie between these two familiar limits. A useful architecture would not need to fully levitate collectors, but it would need to displace them enough to prevent the topological crowding that characterizes a purely Keplerian swarm, while also avoiding a growth logic that depends on repeatedly rethreading a fixed-parameter intersection network. The key question is whether such an intermediate regime exists in a mathematically clean and physically meaningful form.

## Why a continuum view matters

The importance of that shift is not terminological. If Dyson architectures are treated only as discrete end-state categories, then the design problem becomes artificially polarized: one either accepts the intersection burden of a conventional Keplerian swarm, or jumps to payload-hostile radiative levitation. A continuum view changes the problem. It asks how support, stratification, payload margin, and deployment logic vary as one moves continuously through support space. That makes the relevant object of study not a single named megastructure, but a family of reachable architectures parameterized by how much of the support burden is carried orbitally and how much is carried radiatively.

This is also what makes the framework specifically valuable for Dyson theory rather than merely for sailcraft analysis. A stellar collector population is not judged only by the existence of one admissible orbit, but by whether there exists a scalable region of architecture space in which large numbers of collectors can be organized, expanded, and compared without making the growth path itself pathological. The continuum claim is therefore a way of turning Dyson structures from a taxonomy of end states into a parameterized design landscape, one in which topology burden, synchronization options, and incremental deployment logic become explicit architectural variables rather than background annoyances.

## MDDS as a low-beta intermediate regime

This paper argues that such a regime does exist and can be phrased cleanly in Dyson-swarm terms. We consider Micro-Displaced Dyson Swarm (MDDS) configurations in which collectors remain primarily orbital while using a modest solar-radiation-pressure component to sustain small out-of-plane offsets. The objective is not full levitation. It is stratification: replacing one crowded orbital layer with multiple nearby latitude bands that no longer intersect.

Under this interpretation, MDDS is best viewed neither as a conventional Keplerian swarm nor as a near-bubble architecture. Instead, it is a low-$\beta$ intermediate regime inside a broader support continuum. At $\phi = 0$, support is entirely orbital and the configuration reduces to the planar Keplerian limit. As $\phi$ increases, solar-radiation pressure progressively supplements orbital support. At still larger support fractions, one approaches the purely radiatively supported bubble/statite endpoint. In that sense, the principal conceptual move of this paper is to treat Dyson architectures not as a purely discrete shell/swarm/bubble taxonomy, but as a continuous support-and-stratification spectrum parameterized by quantities such as $\beta$, $\phi$, $\nu$, and $\sigma_{\max}(\phi)$. The specific branch analyzed here is the low-latitude, low-$\beta$, circular displaced-orbit branch within that broader continuum. The novelty claim of the present paper is therefore not that these underlying solar-sail dynamics are new, but that they can be reorganized into a compact analytic criterion for layered Dyson-swarm architecture and used to shift the system question from intersection management to support geometry.

## Contribution and scope

The contribution of this paper is primarily theoretical, but it operates at two linked scales. First, at the architectural scale, we propose a continuum view of Dyson architectures, in which collector populations are organized along a continuous support spectrum rather than partitioned into fully disconnected conceptual types. Within that spectrum, MDDS can be understood as an alternative architecture language to the conventional Keplerian Dyson swarm: one that trades some mass and energy margin for a cleaner orbital topology by organizing collectors into radiation-assisted latitude bands and by replacing a fixed-parameter nodal-intersection problem with a layered support geometry that admits a staged-growth interpretation. Second, at the idealized-physics scale, we show that the central design question can be rewritten as the intersection between a latitude support curve and a system areal-density budget. This yields a compact criterion for determining whether a collector architecture can be supported at a chosen off-plane latitude.

The paper also identifies two natural design directions within the same framework. The first is a payload-optimized branch, obtained by minimizing the required $\beta$ at fixed latitude and thus maximizing allowable system areal density. The second is a synchronization-constrained branch, obtained by imposing an external period condition such as Earth-synchronous heliocentric motion. The former maximizes feasibility margin; the latter maximizes operational regularity and makes it possible to discuss layered bands with nearly common angular rates. We emphasize that the second branch should be read as a useful recasting of known synchronous DNKO design space, not as an independent novelty claim in orbit theory.

Our scope is intentionally limited. We do not attempt a full structural, thermal, control, or economic closure for a complete Dyson-scale system. Nor do we attempt a formal megaconstellation-reconfiguration analysis. Instead, we use a small set of low-latitude representative cases to show that the framework is not empty, that it already admits an entry-level regime in the idealized Sun-Earth model, and that the working window narrows rapidly with latitude. The paper should therefore be read as a theory-grounded architectural framework with illustrative low-latitude slices, not as a claim that large-scale Dyson engineering, open-ended deployment economics, or the underlying displaced-orbit dynamics themselves, have been solved anew here.

## What this paper does not claim

For clarity, the present paper does not claim four things. First, it does not propose a fundamentally new orbit family; it repurposes a known low-latitude DNKO branch into a Dyson-architecture language. Second, it does not prove full-lifecycle station-keeping, swarm-wide control closure, or long-horizon operational stability for a Dyson-scale population. Third, it does not establish economic optimality, deployment optimality, or system-level superiority over all Keplerian alternatives. Fourth, it does not provide a complete non-ideal optical model; the main support curve is derived under the ideal-specular approximation and should be read as a reference limit rather than a final engineering closure.

## Related work and novelty posture

The relevant prior-art landscape has two mature branches. The first is the solar-sail and DNKO literature: statites, solar-sail halo orbits, families of displaced two-body orbits, displaced non-Keplerian orbit stability and control, and later synchronous heliocentric variants have all been studied extensively (Forward, 1991; McInnes and Simmons, 1992a,b; McInnes, 1997, 1998; McInnes, 1999; Quarta et al., 2020; Bassetto and Quarta, 2024). The second is the Dyson-swarm / Dyson-bubble literature, which frames stellar collector populations as large-scale engineering or observability problems rather than primarily as orbit-design problems (Dyson, 1960; Wright et al., 2015; McInnes, 2025, 2026).

The present paper sits between those two literatures. Its main novelty is not the introduction of a fundamentally new solar-sail orbit family. Nor does it claim that the burdens of Keplerian swarm management, the limitations of phase-separated megaconstellation logic, Earth-synchronous displaced orbits, period-constrained DNKOs, or statite-like support conditions are first identified here. Instead, the contribution is threefold: to propose a continuous Dyson support spectrum as a more useful architecture language than a purely discrete taxonomy; to identify MDDS as a low-$\beta$ segment of that spectrum; and to reorganize known low-latitude displaced-orbit dynamics into a compact analytic criterion for layered Dyson-swarm design. In that sense, the paper is best read as an analytic architecture/framework paper: it imports mature astrodynamical ingredients, translates them into a Dyson-swarm design language, and shows that the resulting low-angle regime is non-empty in the idealized model and architecturally suggestive.

Figure 1 should be read as the motivating geometric picture for the paper, while Figures 2-7 then track the local force balance, the architectural translation into stratified rings, the support continuum, the quantitative support curves, and finally the low-latitude examples and synchronization variant.

![Keplerian deadlock and nodal-intersection geometry for conventional swarm configurations. All orbital planes passing through the central mass must intersect at nodal points, creating unavoidable collision corridors as swarm density increases.](figures/concept/keplerian_deadlock.svg){#fig:keplerian-deadlock}

# Theoretical Framework

This section establishes the minimal analytic framework used throughout the rest of the paper. The objective is not to reproduce the full DNKO literature, but to isolate the specific quantities that make the Dyson-architecture problem screenable: the displacement latitude $\phi$, the lightness number $\beta$, the residual orbital contribution $\nu$, and the equivalent areal-density ceiling $\sigma_{\max}(\phi)$. Once these are written in one compact language, the later architecture discussion and low-latitude examples reduce to interpretation rather than repeated derivation.

## Geometry, kinematics, and force balance

Consider a collector at fixed heliocentric distance $r$ and latitude $\phi$, moving in a circular path about the stellar rotation axis with angular velocity $\omega$. Let $\alpha$ denote the sail cone angle and define the orbital-rate ratio

$$
\nu \equiv \frac{\omega}{\sqrt{\mu/r^3}}.
$$

Writing the geometry in cylindrical coordinates gives

$$
\rho = r\cos\phi,\qquad z = r\sin\phi.
$$

For an ideal specular sail, the force-balance conditions become

$$
\beta \cos^3\alpha = \cos\phi(1-\nu^2),
$$

$$
\beta \cos^2\alpha\sin\alpha = \sin\phi.
$$

The first equation represents radial unloading of the effective gravitational demand; the second represents the out-of-plane support needed to maintain the displaced orbit.

Read mechanically, these equations simply restate the familiar displaced-orbit balance. Read architecturally, however, they do something more useful: they separate the support burden into an orbital contribution and a radiative contribution. That separation is what allows the present paper to talk about mixed-support Dyson architectures as points within a continuum rather than as members of disconnected conceptual categories.

![Local force balance for a displaced HoverDisk element in meridional section. In the co-rotating view, sail thrust, stellar gravity, and the orbital centrifugal term close as a three-vector balance; equivalently, in the inertial view, sail thrust plus gravity produce the centripetal demand toward the offset-disk center.](figures/concept/force_balance.svg){#fig:force-balance}

Figure 3 is intended to visualize this displaced geometry at the architectural level, while Figures 4 and 5 capture the resulting support continuum and low-latitude support curves in compact form.

![MDDS concept: low-latitude stratified rings above and below the ecliptic. Collectors use modest radiation pressure to maintain small out-of-plane displacements, creating non-intersecting latitude bands.](figures/concept/mdds_stratified_rings.svg){#fig:mdds-rings}

## The payload-optimized branch

At fixed $\phi$, the most important engineering objective is usually to maximize the mass budget available to the system. Since $\beta = \sigma^*/\sigma$, this is equivalent to minimizing the required $\beta$. Solving that optimization over sail attitude yields

$$
\alpha_{\text{opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right),
$$

and the low-$\beta$ support relation

$$
\beta_{\min}(\phi)=\frac{3\sqrt{3}}{2}\sin\phi.
$$

This is the central analytic result used throughout the paper. Within the broader and well-established DNKO framework, it functions here as the key specialization that makes the Dyson-swarm architecture question screenable in closed form. The underlying optimal-force geometry is not introduced here from scratch: the $35.264^\circ$ maximum out-of-plane-force pitch angle is already well established in the displaced-orbit and solar-sail trajectory literature (Simo and McInnes, 2010; Wawrzyniak and Howell, 2011). The specific role of the present paper is to recast that known optimal-angle result into the explicit support curve $\beta_{\min}(\phi)$ and then into the architecture criterion $\sigma_{\text{sys}} < \sigma_{\max}(\phi)$. The result shows that the displaced-orbit requirement grows linearly with latitude at small angles, but with a nontrivial prefactor that makes the exact requirement meaningfully stricter than naive heuristic estimates.

The same result can be rewritten as a limit on allowable system areal density:

$$
\sigma_{\max}(\phi)=\frac{\sigma^*}{\beta_{\min}(\phi)}
=\frac{2\sigma^*}{3\sqrt{3}\sin\phi}.
$$

The architecture question therefore reduces to a single criterion:

$$
\sigma_{\text{sys}} < \sigma_{\max}(\phi).
$$

Equivalently, a system of known areal density $\sigma_{\text{sys}}$ has a maximum feasible latitude

$$
\phi_{\max}=\arcsin\left(\frac{2\sigma^*}{3\sqrt{3}\,\sigma_{\text{sys}}}\right).
$$

This inversion is important because it makes the framework directly usable in both directions. One may either begin with a target latitude and ask what areal density is supportable there, or begin with a candidate system areal density and ask how far from the ecliptic it can be stratified. In that sense the same closed-form relation serves both as a design equation and as a screening equation.

## Dyson support continuum

The support curve above is not only a local orbit result. In the present paper it is used to parameterize a broader Dyson support continuum. At one end lies the planar Keplerian swarm limit, where support is entirely orbital. At the other lies the purely radiatively supported bubble/statite endpoint, where orbital support vanishes. Between them lies a continuous family of mixed-support configurations, of which the low-$\beta$ MDDS regime is the most payload-tolerant segment.

This continuum is not meant to erase engineering differences between swarm-like and bubble-like systems. It is meant to supply a common parameterization for them. In the language of the present framework, the key coordinates along that support spectrum are the lightness number $\beta$, the latitude or off-plane angle $\phi$, the residual orbital contribution $\nu$, and the equivalent areal-density ceiling $\sigma_{\max}(\phi)$. Once written this way, the familiar Dyson categories become interpretable as distinct regions of one support space rather than as isolated conceptual islands.

It is useful to distinguish two different threshold notions within that continuum. The familiar $\beta = 1$ threshold remains an important architectural boundary: once a civilization can build collectors with $\beta \geq 1$, purely radiatively supported bubble/statite-like configurations enter the admissible design space. However, this is not the same as the internal endpoint of the low-$\beta$ payload-optimized MDDS branch derived here. Along that specific branch,

$$
\beta_{\min}(\phi)=1
\quad\Rightarrow\quad
\phi_{\beta=1}=\arcsin\left(\frac{2}{3\sqrt{3}}\right)\approx 22.638^\circ,
$$

at which point the branch still retains a nonzero orbital contribution,

$$
\nu^2 \approx 0.410,\qquad \nu \approx 0.640.
$$

So $\beta = 1$ does not mark the point where the present branch has become purely radiatively supported; it marks the point at which fully radiative-support architectures become available as an alternative design choice.

$$
\nu^2 = 1 - \sqrt{2}\tan\phi,
$$

so the orbital contribution vanishes only at

$$
\phi_c = \arctan\left(\frac{1}{\sqrt{2}}\right)\approx 35.264^\circ,
$$

for which

$$
\beta_{\min}(\phi_c)=1.5.
$$

Thus $\beta = 1$ should be read as the onset of the broader pure-radiative-support design space, whereas $\phi_c \approx 35.264^\circ$ and $\beta = 1.5$ mark the termination of the specific payload-optimized displaced-orbit branch analyzed in this paper. This distinction is important: $\phi_c$ is the internal endpoint of the present branch, not the terminal latitude of the full Dyson support continuum.

For clarity, these three markers can be summarized as follows:

| Marker | Condition | Angle / state | Physical meaning |
|--------|-----------|---------------|------------------|
| Planar Keplerian limit | $\phi = 0$ | $\beta = 0,\ \nu = 1$ | Pure orbital support; no off-plane displacement |
| Bubble/statite access threshold | $\beta = 1$ along the payload-optimized branch | $\phi \approx 22.638^\circ,\ \nu \approx 0.640$ | Pure radiative-support architectures become available as an alternative design choice, but the present branch still retains orbital support |
| Payload-optimized branch endpoint | $\nu = 0$ | $\phi_c \approx 35.264^\circ,\ \beta = 1.5$ | The present displaced-orbit branch itself reaches a purely radiative-support endpoint; this is not the endpoint of the full Dyson support continuum |

![Support continuum: the full spectrum from pure orbital support ($\phi=0$, $\nu=1$) to the payload-optimized branch terminus ($\phi \approx 35.3^\circ$, $\nu=0$). The $\beta=1$ threshold at $\phi \approx 22.6^\circ$ marks where bubble/statite architectures become viable alternatives, while the $\nu=0$ endpoint at $\phi \approx 35.3^\circ$, $\beta=1.5$ marks where the present low-$\beta$ branch itself transitions to pure radiative support.](figures/results/support_continuum.svg){#fig:support-continuum}

![Latitude support curves in the low-latitude regime. Left: $\beta_{\min}(\phi)$ showing the required lightness number. Right: $\sigma_{\max}(\phi)$ showing the maximum allowable system areal density. Reference values at $0.1^\circ$, $0.5^\circ$, and $1^\circ$ illustrate the rapid tightening of the feasibility window with increasing latitude.](figures/results/support_curves.svg){#fig:support-curves}

## The synchronization-constrained branch

The same force-balance framework also admits a second natural design objective. Instead of minimizing $\beta$ at fixed $\phi$, one may impose an external timing requirement, such as Earth-synchronous heliocentric motion. In that case the angular velocity is fixed by the external period constraint, and the displaced orbit adjusts its radius accordingly. This branch is already recognizable within the DNKO literature and is included here as an operationally meaningful variant of the same architecture framework rather than as a new orbit family in its own right (Heiligers and McInnes, 2015; Quarta et al., 2020; Bassetto and Quarta, 2024).

For an Earth-synchronous condition with reference radius $a_\oplus$,

$$
r_{\text{sync}}(\phi,\alpha)=a_\oplus\left(1-\frac{\tan\phi}{\tan\alpha}\right)^{1/3}.
$$

On the payload-optimized branch this becomes

$$
r_{\text{sync}}(\phi)=a_\oplus\left(1-\sqrt{2}\tan\phi\right)^{1/3}.
$$

An important consequence follows immediately: the synchronization constraint modifies the orbital radius, but does not alter the fundamental support curve $\beta_{\min}(\phi)$ or the equivalent density limit $\sigma_{\max}(\phi)$. In other words, synchronization is primarily a geometric and operational constraint rather than an additional support penalty. Within the continuum view, it should therefore be read as a way of slicing the same support space under an additional temporal-organization requirement, not as a separate dynamical family.

That distinction matters for how the branch is interpreted later in the paper. The payload-optimized branch answers the question, "What is the most mass-efficient way to support a chosen latitude?" The synchronization-constrained branch answers a different question: "What geometric adjustment is required if regular timing or common angular rate is imposed from outside?" These are different cuts through the same support space, not competing definitions of the architecture itself.

## Scope of the main-text analysis

The present analysis adopts the standard ideal-specular sail assumption, consistent with first-pass treatments of statite and Dyson-bubble critical areal density. This choice is deliberate. The aim of this paper is to establish the geometric and dynamical existence of a low-$\beta$ displaced operating regime in closed form. We note, however, that MDDS is more sensitive to non-ideal optical behavior than purely radial radiative-support concepts, because the displaced configuration depends on a specific decomposition of radiation pressure into radial and off-plane components. Non-ideal reflection, absorption, and thermal re-emission would therefore not only reduce the effective thrust magnitude, but also perturb the force direction and shift the practical support curve away from the ideal limit. This caveat is consistent with the higher-fidelity sail literature, which shows that realistic optical behavior and sail imperfections can attenuate characteristic acceleration and offset the effective force from the ideal sail normal (Dachwald et al., 2005; Wawrzyniak and Howell, 2011).

An equally important modeling boundary concerns the payload itself. In the force-balance derivation, the sail is treated as the sole optically active support surface. Payload elements such as photovoltaic panels are not assigned an explicit radiation-pressure contribution, nor are payload-induced attitude or offset-force effects carried into the closed-form balance equations. Their role in the present paper is purely inertial: they enter through the aggregate system areal density $\sigma_{\mathrm{sys}}$ in the later bookkeeping examples. The results derived here should thus be interpreted as an ideal baseline framework rather than a complete optical-realism or payload-coupled closure.

The framework above is the main theoretical contribution. Everything else in the paper is subordinate to it. The role of the later examples is not to complete the full engineering problem, but to show how the framework should be used and to demonstrate that it identifies a non-empty low-latitude operating window. Detailed structural closure, control-system design, long-duration perturbation analysis, and full deployment economics are therefore left outside the main claim of the present manuscript.

# Low-Latitude Illustrative Slices

The role of this section is deliberately limited. It does not attempt a full engineering closure, and it is not intended to bear the paper's main novelty claim. Its purpose is narrower and more practical: to show that the continuum established in Section 2 contains a real low-$\beta$ operating window, to attach representative scales to that window, and to illustrate how the analytic criterion behaves when confronted with lightweight spacecraft-style areal-density bookkeeping.

## Representative latitudes

To keep the paper aligned with its central contribution, the main-text examples are intentionally narrow. They are not the paper's primary novelty claim. Their role is to demonstrate that the continuum identified above contains a non-empty low-$\beta$ segment with physically meaningful separation scales. We therefore use four representative points: the Earth-angular-radius characteristic angle $\phi = \theta_\oplus \approx 0.00244^\circ$, followed by $\phi = 0.1^\circ$, $\phi = 0.5^\circ$, and $\phi = 1^\circ$. The sharper contraction by $\phi = 2^\circ$ is retained only as an outer comparison point.

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

![Low-latitude feasibility window showing maximum supportable areal density $\sigma_{\max}$ at representative latitudes. Even the entry-level $0.1^\circ$ case already produces substantial geometric separation while remaining far more permissive in areal-density terms than the better-known high-latitude or bubble limits.](figures/results/low_latitude_window.svg){#fig:low-latitude-window}

## Entry-level interpretation

Even very small latitudes correspond to very large geometric separations at 1 AU. At $\phi = 0.1^\circ$, the out-of-plane displacement is already about $2.61\times 10^5$ km. Comparing to $\theta_\oplus$, a $0.1^\circ$ MDDS displacement corresponds to about $41$ Earth radii of off-plane separation, while $0.5^\circ$ and $1^\circ$ correspond to about $205$ and $410$ Earth radii respectively. The point of MDDS is not to achieve dramatic angular offsets; it is to obtain enormous spatial stratification from modest angular displacements while staying well below the full radiative-support threshold.

This Earth-angle comparison also suggests a natural entry-level characteristic angle for the framework itself. At $\phi = \theta_\oplus$, the support threshold $\sigma_{\max}(\theta_\oplus)\approx 13.83\ \mathrm{kg\,m^{-2}}$ is already well within the broad range of present human spacecraft materials and systems. Geometrically, it corresponds to an out-of-plane separation of approximately one Earth radius, $z \approx 6{,}371\ \mathrm{km}$. If one additionally imposes Earth-synchronous motion on the payload-optimized branch, the corresponding inward radius correction is only about $3.0\times 10^3\ \mathrm{km}$. The significance of this point is not that it solves the full MDDS engineering problem, but that it shows the continuum has a genuinely near-entry regime rather than only a distant futuristic one.

This is the sense in which MDDS differs from both comparison endpoints. Relative to a Keplerian swarm, it sacrifices some mass and energy margin in exchange for non-intersecting stratification. Relative to a statite or bubble concept, it remains far from the $\beta \geq 1$ regime and therefore preserves a much larger payload budget.

## Order-of-magnitude engineering slices

The low-latitude framework becomes more concrete when coupled to a minimal areal-density bookkeeping exercise. Consider an illustrative decoupled node composed of an ultralight reflector and a photovoltaic payload with fill factor $\lambda = A_{\mathrm{pv}}/A_{\mathrm{refl}}$. To first order,

$$
\sigma_{\mathrm{sys}} = \sigma_{\mathrm{refl}} + \lambda \sigma_{\mathrm{pv}},
$$

with all second-order structural and control terms deliberately left outside the main-text estimate. In keeping with the modeling scope of this paper, the photovoltaic payload is treated here as added areal density rather than as a second optically resolved surface. That is, its own radiation pressure, thermal re-emission, and possible force-vector offsets are ignored in the main-text bookkeeping. Using a light reflector benchmark of $\sigma_{\mathrm{refl}} \approx 5\ \mathrm{g\,m^{-2}}$ and an ultralight PV benchmark of $\sigma_{\mathrm{pv}} \approx 54.8\ \mathrm{g\,m^{-2}}$, the support curve immediately implies approximate low-latitude fill-factor limits:

- at $0.1^\circ$, the ideal areal-density budget no longer constrains $\lambda$ below unity
- at $0.5^\circ$, the same is still true to first order
- at $1^\circ$, the bookkeeping gives $\lambda_{\max} \approx 0.53$

These numbers are useful because they convert an abstract support curve into a design-language statement. Instead of asking only whether a latitude is mathematically supportable, one can ask how much photovoltaic fill or payload fraction survives once a reflector benchmark is specified. That translation from support relation to payload fraction is one of the simplest ways to make the continuum operationally legible.

These values should not be read as a final engineering design. Their purpose is narrower: they show how the support curve translates directly into a shrinking payload fraction as latitude rises, even before one introduces heavier structural realism. In particular, the $0.1^\circ$ point is useful because $\sigma_{\max} \approx 337\ \mathrm{g\,m^{-2}}$ is no longer an obviously exotic areal-density threshold. In pure mass-per-area terms, this entry-level low-latitude regime approaches a domain that contemporary lightweight spacecraft can plausibly inhabit. That observation should not, however, be extrapolated indiscriminately across the full $0.1^\circ$--$1^\circ$ interval: $0.5^\circ$ and especially $1^\circ$ already demand materially lighter systems than those demonstrated by current flown sailcraft, so the present manuscript treats them as screening slices rather than near-term engineering claims (Macdonald and McInnes, 2011; Mansell et al., 2023).

That interpretation becomes sharper if one compares directly against flown or near-flight sailcraft. LightSail 2 combined a roughly $5\ \mathrm{kg}$ CubeSat-class spacecraft with a deployed sail area of $32\ \mathrm{m^2}$, corresponding to a mission-level loading of about $156\ \mathrm{g\,m^{-2}}$ (Mansell et al., 2023). NEA Scout, at less than $14\ \mathrm{kg}$ and about $86\ \mathrm{m^2}$ of sail area, falls in a similar range, roughly $160\ \mathrm{g\,m^{-2}}$ (Johnson et al., 2017). These benchmarks sit far below the $\theta_\oplus$ and $0.1^\circ$ support thresholds, but well above $\sigma_{\max}(1^\circ)$. This is precisely why the current paper frames the low-angle window as non-empty yet rapidly narrowing: the extreme entry regime already overlaps current lightweight sailcraft capability in mass-per-area terms, while the more ambitious low-degree regime remains significantly ahead of present integrated system practice.

## Synchronization slice

The synchronization-constrained branch is also easy to interpret numerically in the low-latitude regime. On the payload-optimized branch, the Earth-synchronous radius correction is small but non-negligible:

- at $0.1^\circ$, $r_{\mathrm{sync}} \approx 0.99918\ \mathrm{AU}$, corresponding to an inward shift of about $0.12$ million km
- at $0.5^\circ$, $r_{\mathrm{sync}} \approx 0.99587\ \mathrm{AU}$, corresponding to an inward shift of about $0.62$ million km
- at $1^\circ$, $r_{\mathrm{sync}} \approx 0.99170\ \mathrm{AU}$, corresponding to an inward shift of about $1.24$ million km

This is useful for interpretation because it reinforces the distinction between the two design branches. The support requirement is still controlled by $\beta_{\min}(\phi)$ and $\sigma_{\max}(\phi)$; synchronization mainly alters where the ring sits, not whether the latitude is supportable in the first place.

![Earth-synchronous radius correction along the payload-optimized branch. The inward shift from 1 AU grows with latitude but does not alter the fundamental support curve; synchronization is an operational geometry constraint, not an additional support penalty.](figures/results/sync_radius.svg){#fig:sync-radius}

## What the low-latitude slices show

The low-latitude slices establish one thing and one thing only: the continuum identified in Section 2 contains a real and potentially useful low-$\beta$ segment. They do not by themselves establish full system competitiveness, lifetime, control closure, or economic superiority. Their purpose is to verify that the architecture framework maps onto a physically meaningful region rather than collapsing immediately into either the Keplerian limit or the full statite limit. For contrast, the same support curve yields only $\sigma_{\max}(2^\circ)\approx 16.9\ \mathrm{g\,m^{-2}}$, showing how quickly the margin contracts once one moves beyond the entry-level low-latitude regime.

That is exactly the level of inference the present paper needs. The examples do not prove that MDDS is already an engineering solution, but they do prove that the continuum is not empty rhetoric. There exists a mathematically coherent, physically interpretable, and quantitatively nontrivial low-angle regime in which large geometric stratification appears before the architecture reaches the fully radiative-support limit.

# Discussion

The main result of this paper is best understood as a reframing at two linked levels. At the architectural level, MDDS is not presented as a completed Dyson-engineering solution, but as an alternative language for organizing stellar collector populations: one that replaces intersecting same-radius swarm geometry with radiation-assisted latitude bands and thereby lowers the native orbital-topology burden. At the idealized-physics level, the framework identifies a usefully screenable low-angle regime in which modest radiation-pressure support can produce large off-plane stratification without crossing into the payload-hostile bubble limit. The discussion below unpacks why that reframing matters, what it changes conceptually, and where its current limits still lie.

## Architecture reframing

This reframing matters because it changes the central question. The relevant question is no longer whether a given displaced ring is intuitively plausible, but whether a system of areal density $\sigma_{\text{sys}}$ lies below the support curve $\sigma_{\max}(\phi)$. Once expressed in this form, the architecture becomes analyzable, comparable, and extensible. The main novelty of the present paper therefore lies not in introducing a fundamentally new family of solar-sail orbits, but in reorganizing known low-latitude DNKO dynamics into an analytic architecture criterion for layered Dyson-swarm design and, beyond that, in using that criterion to define a continuous Dyson support spectrum.

This is also why the Dyson framing should be taken literally rather than decoratively. The continuum claim is not that shell, swarm, and bubble are engineeringly equivalent. It is that they can be parameterized within a common support logic while retaining sharply different cost, control, and payload consequences in different regions of that space. The specific contribution of MDDS is to make one previously under-articulated region of that space explicit: a low-$\beta$ regime in which stellar collector populations remain mostly orbital, yet already acquire a qualitatively different topology from a conventional Keplerian swarm.

## From end-state taxonomy to design space

For Dyson theory, that shift is substantive. It replaces a discourse organized around static end states with one organized around traversable regions of design space. Once shell-like, swarm-like, and bubble-like constructs are interpreted as regions within a common support spectrum, questions of growth path, reachable intermediate regimes, and transition thresholds become first-class theoretical objects rather than afterthoughts. The role of MDDS in this paper is precisely to expose one such intermediate region in analytic form.

The same point can be stated in more explicitly architectural terms. In a same-radius Keplerian swarm, each additional non-coplanar orbit expands the graph of nodal crossings that must be managed. Phase-separated constellation logic can redistribute the timing of those crossings, but it does not remove the crossing graph itself, and it is naturally framed around fixed parameter sets rather than indefinite expansion (Walker, 1971; Chen et al., 2024; de Weck et al., 2004; Lee et al., 2025). For a civilization-scale infrastructure expected to grow in stages, that is a poor native language. It forces the architecture to think in terms of intersection management, symmetry preservation, and rephasing burden.

## Growth path and deployment logic

MDDS instead shifts the organizing variable from the management of an expanding intersection network to the design of a layered support geometry. In the low-latitude regime, added capacity is expressed as additional latitude bands and, on the synchronization-constrained branch, as bands whose angular rates can be kept nearly common through modest radius adjustments. The immediate effect is not merely "more space," but a change in the geometry of interactions: from repeated line-of-node crossings to separated layers with explicit normal spacing and operationally regular motion. That shift is the architectural significance of the low-$\beta$ regime.

The paper also suggests a useful deployment interpretation. Since the support curve is most permissive near the ecliptic, a Dyson-progressive architecture can begin in low-latitude bands and expand outward in latitude as areal density improves. On this view, MDDS is not merely a static configuration concept; it is also a growth logic for stratified stellar infrastructure, closer in spirit to an evolvable architecture than to a fixed end-state megaconstellation (Creech, 2013; Johnson et al., 2023). The low-angle examples sharpen that point: in the Sun-Earth environment, even very small angular displacements already produce wide deployment planes, and the corresponding areal-density thresholds range from permissive to entry-level rather than immediately futuristic. This does not yet amount to a proof of frictionless expansion, and the present paper does not quantify deployment cost, swarm-management benefit, or reconfiguration avoidance using a formal traffic-analysis metric. But it does define a geometry in which those questions can be asked without first accepting the fixed nodal-intersection graph of the Keplerian case.

A natural next-step metric family would therefore include node-intersection count, minimum normal separation, conjunction-corridor density, and reconfiguration burden under staged expansion. The present paper stops one layer short of that formal traffic-and-growth analysis, but it identifies the architectural shift that makes such a program meaningful: from optimizing traffic through unavoidable crossings to designing a support geometry that suppresses those crossings in the first place.

## Observational implications of a growth-first continuum

The same staged-growth logic also suggests an observational implication that is worth stating explicitly, even though the present paper does not attempt to model it in detail. If a Dyson-scale collector population is more likely to emerge by first occupying the low-latitude, low-$\beta$ part of the support continuum and only later expanding toward higher latitudes, then its developing morphology should not generically resemble a nearly isotropic shell. It should instead appear, at least over a substantial interval of its buildout history, as a flattened and stratified circumstellar structure.

In that restricted geometric sense, a developing MDDS-like system may be observationally closer to a circumstellar disk than to the canonical shell-like popular image of a Dyson sphere. The point is not that an artificial collector population would be physically equivalent to a natural protoplanetary or debris disk. The underlying material, thermal, and dynamical signatures could differ sharply. The narrower inference is that a civilization following a growth path through the low-latitude support regime would likely build a star-centered, anisotropic, disk-like reprocessing structure before it ever approached a high-covering-fraction bubble-like endpoint.

That possibility matters because it suggests that the continuum view may have consequences not only for engineering language but also for technosignature expectations. If realistic growth proceeds through layered low-latitude bands, then some developing Dyson systems may present themselves less as sphere-like infrared excesses and more as unusually organized circumstellar disks with artificial stratification or other non-natural regularities. The present paper does not attempt radiative-transfer modeling, spectral prediction, or discriminants against natural disks, so this point should be read as a hypothesis generated by the framework rather than as an observational claim already demonstrated.

## Modeling boundaries

At the same time, the ideal-mirror assumption should be interpreted carefully. For purely radial radiative-support concepts, optical non-idealities primarily act as thrust-efficiency penalties. For MDDS, by contrast, non-ideal optical behavior can also perturb the effective force direction because the displaced configuration relies on a specific vector decomposition of radiation pressure. This does not invalidate the present framework, but it does mean that the closed-form support curve derived here is best understood as an ideal reference limit that later optical-realism studies should correct upward rather than replace wholesale.

An equally important reviewer concern is long-term maintainability. The broader DNKO literature has already shown that displaced orbits can include marginally stable or unstable subfamilies under open-loop dynamics, and that linear state feedback can be used to stabilize such configurations in practice (McInnes, 1998; Bookless, 2006). The present paper does not attempt to re-derive a distributed control law for a Dyson-scale population, but neither does it assume that stability is a solved freebie. The correct reading is narrower: the architecture framework established here addresses geometric existence and screening-level supportability, while long-horizon station-keeping, phase control, and swarm-wide feedback design belong to the next layer of analysis. Existing DNKO control results make that next layer plausible enough that its omission does not undermine the framework claim, but they do not remove the need for future explicit treatment.

## Scope and next steps

The present manuscript also stops short of the heavier engineering questions. Detailed structural closure, fixed bus mass, deployment mechanics, perturbation-control closure, thermal closure, and broader power-system comparisons remain important follow-on problems. That boundary is intentional. The paper is not trying to compress the entire Dyson-engineering stack into a first framework manuscript; it is trying to establish the lowest layer on which the larger engineering stack can be coherently posed.

The appropriate claim at this stage is therefore limited but substantive: the framework is mathematically coherent, physically interpretable, and non-empty in the low-latitude regime. If later work adds optical realism, explicit control closure, deployment economics, and traffic-style growth metrics, those additions would extend the present framework rather than replace its central architectural claim.

# Conclusion

We have introduced a low-$\beta$ framework for Micro-Displaced Dyson Swarm architectures and derived a closed-form support relation linking off-plane latitude to required radiation-pressure support. This yields a simple density-based criterion and exposes two natural design directions: a payload-optimized branch and a synchronization-constrained branch. The contribution is threefold: at the architectural level, the paper advances a continuous Dyson support-spectrum view in which swarm-like and bubble-like configurations occupy different regions of a common support space; within that spectrum, MDDS emerges as a low-$\beta$ alternative to the conventional Keplerian Dyson swarm by recasting known displaced-orbit dynamics into a layered Dyson-swarm design language; and at the idealized-physics level, the Sun-Earth environment already contains a non-empty low-angle operating window in which modest angular displacement produces large spatial separation while entry-level characteristic angles provide useful scale comparisons against present lightweight spacecraft systems.

The architectural significance of that result is not only that a low-$\beta$ displaced-orbit regime can be identified in the idealized model. It is that this regime changes the organizing question. Instead of treating Dyson growth purely as a problem of managing ever-richer intersection networks in fixed-parameter Keplerian megaconstellations, it allows the problem to be restated in terms of layered support geometry, synchronization choices, and staged latitude expansion. The main contribution is therefore not a new solar-sail orbit family or a proof of full engineering viability, but a compact analytic framework for discussing stratified Dyson-swarm architectures and a low-latitude regime that warrants further study under more realistic optical, control, and system assumptions.

The immediate next step is not to abandon this idealized framework, but to stack additional realism on top of it in an orderly way. The most natural extensions are improved optical-force models, explicit station-keeping and feedback analysis for multi-node populations, traffic-style measures of topology reduction under staged growth, heavier system-level bookkeeping for deployment and payload closure, and observational modeling for whether a developing low-latitude Dyson architecture would present more like an artificial circumstellar disk than a shell-like technosignature. Those extensions would test the engineering reach of MDDS, but they would do so on top of the support-spectrum language established here. In that sense, the present paper is best read as a first architectural control surface: a compact framework that makes the next generation of Dyson-swarm questions more sharply poseable.
