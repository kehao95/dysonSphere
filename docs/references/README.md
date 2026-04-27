# References and Literature Review

本目录存放参考文献和文献综述材料。

---

## Core References

### Solar Sailing Theory

1. **McInnes, C. R. (1999)**. *Solar Sailing: Technology, Dynamics and Mission Applications*. Springer-Praxis.
   - Chapter 3: Orbital Dynamics — displaced orbit theory
   - Chapter 5: Mission Applications

2. **McInnes, C. R. & Simmons, J. F. L. (1992)**. "Solar sail halo orbits I: Heliocentric case." *Journal of Spacecraft and Rockets*, 29(4), 466-471.

3. **McInnes, C. R. (2002)**. "Non-Keplerian Orbits for Mars and Beyond." *Acta Astronautica*.

### Dyson Structures

4. **Dyson, F. J. (1960)**. "Search for Artificial Stellar Sources of Infrared Radiation." *Science*, 131(3414), 1667-1668.
   - Original Dyson sphere proposal

5. **Wright, J. T. et al. (2014)**. "The Search for Extraterrestrial Civilizations with Large Energy Supplies." *The Astrophysical Journal*.

### Solar Sail Materials

6. **JAXA IKAROS Mission Data**
   - First successful solar sail demonstration (2010)
   - Sail material specifications

7. **NASA In-Space Propulsion Technology Reports**
   - Advanced sail materials (CP1, etc.)
   - Mass budgets for solar sail missions

### Thin-Film Photovoltaics

8. **Alta Devices** — Flexible GaAs solar cell specifications
9. **MiaSolé** — CIGS thin-film specifications

### Repository Benchmark Notes

- `material_benchmark_notes.md` — source notes for the material benchmarks used
  in the first-pass MDDS and ideal-architecture comparison studies
- `structural_benchmark_notes.md` — source notes for boom, tether, and flight-
  heritage structural benchmarks

---

## Literature Review Notes

### Current Literature Review Refresh

- `literature_review_refresh_20260427.md` — curated absorption of the `dr`
  deep-research runs for the MDDS manuscript. Use this as the current prior-art
  boundary map and citation-cluster guide; treat the raw `dr` output as research
  triage, not as citable authority.

### Displaced Orbits (McInnes)

Key equations from McInnes (1999):

For a circular displaced orbit at angle φ above the ecliptic:

1. **Force balance** requires the sail to provide both radial and out-of-plane components
2. **Lightness number** β = σ*/σ determines achievable displacement
3. **Exact ideal-sail minimum-beta branch**: $\beta_{\min} = (3\sqrt{3}/2)\sin\phi$ for practical low-$\beta$ displaced circular orbits

Critical insight: The orbit is not "levitating" (no orbital velocity), but rather following a non-Keplerian trajectory where orbital motion still provides centripetal acceleration.

### Dyson Sphere Variants

| Type | Description | β required | Practical? |
|------|-------------|------------|------------|
| Shell | Solid sphere | N/A (structural) | No |
| Swarm | Keplerian orbits | 0 | Yes, but collision risk |
| Bubble | Full levitation | ≥1 | No (material limits) |
| **MDDS (ours)** | Displaced orbits | ~0.045 at 1° | **Potentially**, if PV areal density stays below the tightened mass budget |

---

## PDF Storage

Place PDF files in this directory with naming convention:
`AuthorYear_ShortTitle.pdf`

Examples:
- `McInnes1999_SolarSailing.pdf`
- `Dyson1960_InfraredSources.pdf`

---

## To Read / Acquire

- [ ] McInnes (1999) full text — Chapter 3 especially
- [ ] IKAROS mission technical reports
- [ ] Recent solar sail material advances (2020+)
- [x] Device-level ultralight PV benchmark source for `54.8 g/m²` conversion: Kim et al. (2021), flexible InGaP/GaAs tandem cell, `27.4%` and `>5000 W/kg` under AM1.5G
- [ ] Thin-film PV space qualification data and module-level packaging margins
