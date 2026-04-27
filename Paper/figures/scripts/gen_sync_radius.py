#!/usr/bin/env python
"""Generate the publication-style Earth-synchronous radius figure."""

from gen_paper_figures import generate_sync_radius, setup_style


if __name__ == "__main__":
    setup_style()
    generate_sync_radius()
    print("generated sync_radius")
