#!/usr/bin/env python
"""Generate the publication-style MDDS stratified-rings figure."""

from gen_paper_figures import generate_mdds_stratified, setup_style


if __name__ == "__main__":
    setup_style()
    generate_mdds_stratified()
    print("generated mdds_stratified_rings")
