# Structural Benchmark Notes

This note records the source-backed structural and flight-heritage references
used after the first exploratory boom/tether scaling study.

## ACS3 Flight-System Benchmark

Primary source:

- NASA ACS3 mission update (2023): https://ntrs.nasa.gov/api/citations/20230008378/downloads/Wilkie_ACS3_mission_update_ISSS_2023_20230530_rev_a.pdf

Useful appendix values from the ACS3 PDF:

- total spacecraft mass: `16 kg`
- bus mass: `8.3 kg`
- sail-boom subsystem mass: `7.7 kg`
- boom length: `7.0 m`
- boom mass, each: `0.164 kg`
- sail quadrant area, each: `20 m²`
- sail quadrant mass, each: `0.085 kg`
- effective lightness number at 1 AU: `β ≈ 0.0077`

Derived repository benchmarks:

- ACS3 total deployed areal density on `80 m²`: `200 g/m²`
- ACS3 sail-boom subsystem areal density on `80 m²`: `96.25 g/m²`
- ACS3 membrane + boom hardware only:
  - membrane mass = `4 × 0.085 = 0.34 kg`
  - boom mass = `4 × 0.164 = 0.656 kg`
  - combined areal density = `12.45 g/m²`
- ACS3 boom linear density:
  - `0.164 kg / 7.0 m = 23.43 g/m`

Interpretation:

- ACS3 is extremely useful as a system-level reality check because it cleanly
  separates sail membrane / boom hardware from full deployed-spacecraft
  overhead.
- The membrane+boom subset is in the same order of magnitude as the MDDS
  reflector requirements; the full spacecraft is not.

## NEA Scout Flight-System Benchmark

Primary source:

- NASA NEA Scout paper (2017): https://ntrs.nasa.gov/api/citations/20170001499/downloads/20170001499.pdf

Useful values from the paper:

- spacecraft bus weighs less than `14 kg`
- solar sail area: `86 m²`
- sail is a `2.5 micron` CP1-based aluminized membrane
- four `6.8 m` Elgiloy booms deploy the sail

Derived repository benchmark:

- NEA Scout total-system areal density upper bound: `14 kg / 86 m² ≈ 162.8 g/m²`

Interpretation:

- Like ACS3, NEA Scout demonstrates a real deep-space solar-sail system.
- But as an integrated spacecraft benchmark, it still sits several times above
  the areal-density limit required for `1°`-class MDDS operation at 1 AU.

## Tether Line Benchmark

Primary source:

- U.S. Spars Pure Dyneema product page: https://www.usspars.com/ropes/pure-dyneema/

Repository benchmark conversions:

- `1.25 mm` SK78 braid: `0.10 kg / 100 m = 1.0 g/m`
- `2.0 mm` SK78 braid: `0.20 kg / 100 m = 2.0 g/m`

These are product-level rope masses, not space-qualified tether-system masses.
They are still far better grounded than the earlier placeholder-only values and
are suitable for a first source-backed structural scaling pass.
