#!/usr/bin/env python
"""Generate the publication-style MDDS force-balance figure."""

from gen_paper_figures import generate_force_balance, setup_style


if __name__ == "__main__":
    setup_style()
    generate_force_balance()
    print("generated force_balance")
