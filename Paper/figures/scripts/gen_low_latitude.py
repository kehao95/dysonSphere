#!/usr/bin/env python
"""Generate the publication-style low-latitude window figure."""

from gen_paper_figures import generate_low_latitude_window, setup_style


if __name__ == "__main__":
    setup_style()
    generate_low_latitude_window()
    print("generated low_latitude_window")
