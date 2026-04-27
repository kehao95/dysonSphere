#!/usr/bin/env python
"""Generate the publication-style low-latitude support-curves figure."""

from gen_paper_figures import generate_support_curves, setup_style


if __name__ == "__main__":
    setup_style()
    generate_support_curves()
    print("generated support_curves")
