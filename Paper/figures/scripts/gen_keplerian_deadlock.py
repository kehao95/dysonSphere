#!/usr/bin/env python
"""Generate the publication-style Keplerian nodal-crossing figure."""

from gen_paper_figures import generate_keplerian_deadlock, setup_style


if __name__ == "__main__":
    setup_style()
    generate_keplerian_deadlock()
    print("generated keplerian_deadlock")
