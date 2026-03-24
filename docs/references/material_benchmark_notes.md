# Material Benchmark Notes

This note records the benchmark sources used in the first-pass MDDS feasibility
and ideal-architecture comparison studies.

## Reflector Benchmark

### CP1 solar sail subsystem

- NASA solar-sail mission studies and tech briefs consistently treat CP1-based
  sails as a lightweight near-term reference point.
- Repository working benchmark for the optimistic reflector case: `5 g/m²`.
- This is a clean benchmark value for comparison, not a claim that a complete
  flight-ready MDDS reflector subsystem has already been demonstrated at exactly
  that mass.

Useful NASA references:
- Solar-sail subsystem study context: https://ntrs.nasa.gov/api/citations/20120016900/downloads/20120016900.pdf
- Solar-sail state-of-the-art overview: https://ntrs.nasa.gov/api/citations/20140000655/downloads/20140000655.pdf?attachment=true

### Conservative Kapton benchmark

- Repository conservative reflector benchmark: `11 g/m²`, representing a much
  heavier but still recognizably solar-sail-like membrane case.

## Photovoltaic Benchmarks

### Ultralight flexible tandem

- Used as the optimistic PV benchmark.
- Efficiency benchmark: `27.4%`
- Specific power benchmark: `>5000 W/kg`
- Converted in this repository to an upper-bound areal density of `54.8 g/m²`
  for ideal 1 AU comparison purposes.

Public abstract / summary page:
- IBM Research publication page: https://research.ibm.com/publications/ultralight-high-efficiency-flexible-ingapingaas-tandem-solar-cells-on-plastic

Important caveat:
- This is closer to a device-level / cell-level frontier result than to a fully
  integrated, flight-qualified space power subsystem.

### Flexible CIGS space projection

- Used as a conservative space-oriented thin-film benchmark.
- Repository benchmark: `15%` efficiency, `1153.13 W/kg`
- Converted areal density: about `176 g/m²`

Reference:
- NASA/FSEC thin-film CIGS projection: https://ntrs.nasa.gov/api/citations/20030000597/downloads/20030000597.pdf

### Commercial flexible CIGS module

- Used as a realistic heavy commercial flexible baseline.
- Repository benchmark: `16.7%`, `1.7 kg/m²`

Reference:
- MiaSole FLEX-03W datasheet: https://miasole.com/wp-content/uploads/2017/11/flex-03w_datasheet.pdf

## Flight-System Reality Check

For context, NASA SmallSat power state-of-the-art surveys show that real
flight-array specific power is usually far below the ultralight device-level
benchmarks used above. This is why the repository currently treats the
ultralight tandem case as an optimistic upper-end feasibility marker rather than
as a directly available system solution.

Reference:
- NASA SmallSat Power Subsystems state of the art: https://www.nasa.gov/wp-content/uploads/2025/02/soa-2024.pdf
