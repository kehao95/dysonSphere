#!/usr/bin/env python
"""Generate the publication-style support-continuum schematic."""

from gen_paper_figures import generate_support_continuum, setup_style


if __name__ == "__main__":
    setup_style()
    generate_support_continuum()
    print("generated support_continuum")
