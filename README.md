# Micro-Displaced Dyson Swarm (MDDS)

**Low-Latitude Architecture Screening for Micro-Displaced Dyson Swarm Nodes using Solar-Sail Support**

基于太阳帆支撑的微位移戴森群低纬架构筛选研究

---

## Abstract

Dense same-shell Keplerian Dyson Swarm concepts inherit a geometric constraint: each orbital plane passes through the stellar center of mass. When many same-radius planes are used, pairwise nodal intersections create a persistent crossing network that must be phased, screened, and managed. The result is not a solved collision-rate model, but a topology-and-growth pressure for dense same-shell architectures.

We propose a **Micro-Displaced Dyson Swarm (MDDS)** architecture that leverages solar radiation pressure (SRP) to maintain small out-of-plane displacements. More broadly, we treat Dyson architectures as a **support continuum** rather than a set of disconnected shell / swarm / bubble categories. In that framing, MDDS occupies a low-$\beta$ mixed-support regime between the planar Keplerian limit and the fully radiatively supported bubble/statite endpoint.

The key architectural idea is a **Decoupled Architecture**: separating the reflective support surface from absorptive payload or power hardware. In the current manuscript this is treated only as mass-budget bookkeeping; a closed optical-power architecture still requires explicit modeling of absorption, reflection, reradiation, shadowing, torque, and thermal control.

---

## The Problem: Same-Shell Keplerian Pressure

```
        Dense Same-Shell Keplerian Swarm
        
              ╱ orbit A
         ☀ ──╳── orbit B    ← Nodal intersection!
              ╲ orbit C
              
     All orbits must pass through stellar center
     → Unavoidable crossing points
     → Crossing corridors that require traffic management
```

This is not just a local conjunction issue. In a dense same-radius swarm, it becomes a topology-and-growth pressure: expanding capacity means expanding the nodal graph itself, so the architecture inherits more crossing structure as it scales.

### Why Existing Endpoints Are Unsatisfying

| Approach | Limitation |
|----------|------------|
| Co-orbital phase separation | Redistributes encounter timing but does not remove same-radius multi-plane nodal geometry |
| Nested rings (different radii) | May reduce crossings, but introduces radial packing, shadowing, and thermal-crosstalk tradeoffs |
| Full levitation (Dyson Bubble) | Requires $\sigma < 1.53$ g/m² — no useful payload |

---

## Our Solution: Micro-Displacement via Decoupled Sails

```
        Micro-Displaced Parallel Rings
        
        ════════════════  z = +d (ring at latitude +φ)
              ↑ SRP
         ☀ ──────────────  z = 0  (equatorial plane)
              ↓ SRP  
        ════════════════  z = -d (ring at latitude -φ)
        
     Small angular displacement φ ~ 1°
     → Physical separation d ~ millions of km
     → No same-shell nodal crossings in the idealized stratified geometry
```

The larger reframing is that Dyson structures need not be discussed as fully separate end states. Instead, they can be organized along a support continuum: purely orbital Keplerian swarms at one end, fully radiatively supported bubble/statite concepts at the other, and low-$\beta$ mixed-support MDDS layers in between.

### Core Insight

We do not need full levitation to enter a displaced-support regime. For the reduced low-latitude screening branch used in the current manuscript,

$$\beta_{\min} = \frac{3\sqrt{3}}{2}\sin\phi$$

At 1 AU and $\phi = 1^\circ$, this gives:

$$\beta_{\min} \approx 0.0453,\qquad \sigma_{\max} \approx 33.8\ \text{g/m}^2,\qquad d \approx 2.61 \times 10^6\ \text{km}$$

This is still far easier than full levitation ($\beta \ge 1$), but materially stricter than the naive $\beta \approx \sin\phi$ heuristic. The current paper treats this as a low-latitude architecture-screening relation, not as a full high-latitude ideal-sail branch.

### Progressive Deployment Path

MDDS is appealing not only as a final configuration, but also as a **growth path**:

1. Start near the chosen reference plane, where the required $\beta$ is minimal and the mass budget is most forgiving.
2. Deploy nodes that are already useful individually, rather than waiting for a full shell-equivalent buildout.
3. Expand gradually toward higher latitudes as materials, structures, control, and in-space manufacturing improve.

This makes MDDS more than a static Dyson concept. It becomes a **Dyson-progressive architecture** in which intermediate stages remain operationally meaningful.

### Decoupled Architecture

| Module | Function | Material | Orientation |
|--------|----------|----------|-------------|
| **Drag Sail** (large area) | Reflect photons → axial thrust | 1 μm Kapton/Al film | Tilted to orbital plane |
| **Payload Core** (small area) | Absorb → power generation | Flex thin-film PV | Face Sun directly |

**Key advantage**: The reflector and absorber can be modeled as distinct functional surfaces. The present paper uses that distinction only for first-pass mass bookkeeping; optical closure and thermal-power architecture remain future work.

---

## Project Structure

```
dysonSphere/
├── README.md           # This file — project overview
├── STATUS.md           # Current state and recent progress
├── ROADMAP.md          # Research milestones and timeline
├── DEVELOPMENT.md      # Development workflow and conventions
├── AGENTS.md           # Repository constitution (self-model)
│
├── Paper/              # Manuscript and related materials
│   ├── README.md       # Paper-specific control plane
│   ├── drafts/         # Working drafts
│   ├── figures/        # Diagrams and plots
│   └── references/     # Bibliography and source materials
│
├── models/             # Mathematical models
│   ├── README.md       # Model documentation
│   ├── orbital/        # Orbital dynamics (displaced orbits)
│   ├── thermal/        # Thermal equilibrium analysis
│   └── mass_budget/    # Engineering mass budget calculations
│
├── experiments/        # Numerical experiments and simulations
│   ├── PROTOCOL.md     # Experiment protocol
│   └── runs/           # Individual experiment runs
│
└── docs/               # Additional documentation
    ├── references/     # Literature review and prior art
    └── visualization/  # Browser-based concept demos
```

---

## Key Parameters

| Symbol | Name | Value | Notes |
|--------|------|-------|-------|
| $\sigma^*$ | Critical areal density | 1.53 g/m² | For Sun; $\beta = 1$ threshold |
| $\beta$ | Lightness number | $\lesssim 0.05$ | Representative low-latitude range through 1° |
| $\phi$ | Displacement angle | $\leq 1^\circ$ main slice | Latitude of displaced ring; 2° retained only as stress comparison |
| $r$ | Orbital radius | 1 AU | Reference distance |

---

## Theoretical Foundation

Based on Colin McInnes' **Displaced Orbit** theory (see `docs/references/`).

The lightness number $\beta$ relates radiation pressure to gravitational force:

$$\beta = \frac{F_{\text{rad}}}{F_{\text{grav}}} = \frac{\sigma^*}{\sigma}$$

For the reduced low-latitude displaced circular-orbit screen, with effective cylindrical support pitch $\alpha_{\mathrm{eff}}$ and orbital-rate ratio $\nu = \omega/\sqrt{\mu/r^3}$:

$$\beta \cos^3\alpha_{\mathrm{eff}} = \cos\phi(1-\nu^2)$$
$$\beta \cos^2\alpha_{\mathrm{eff}} \sin\alpha_{\mathrm{eff}} = \sin\phi$$

Minimizing over this reduced support pitch gives the low-$\beta$ screening branch used in this project:

$$\alpha_{\mathrm{eff,opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right) \approx 35.26^\circ,\qquad
\beta_{\min} = \frac{3\sqrt{3}}{2}\sin\phi$$

This is not a full high-latitude Sun-line cone-angle force law; Appendix A of the manuscript compares it with the standard ideal-specular cone-angle treatment and shows that the low-latitude examples are conservative by only a few per cent.

---

## Current Status

See [STATUS.md](./STATUS.md) for current progress.

See [ROADMAP.md](./ROADMAP.md) for planned milestones.

---

## References

1. Dyson, F. J. (1960). "Search for Artificial Stellar Sources of Infrared Radiation." *Science*, 131(3414), 1667–1668.
2. McInnes, C. R. (1999). *Solar Sailing: Technology, Dynamics and Mission Applications*. Springer-Praxis.
3. McInnes, C. R. (2002). "Non-Keplerian Orbits for Mars and Beyond." *Acta Astronautica*.

---

## License

Research project — licensing TBD.
