Publication figures live here as `.svg` sources with generated `.pdf` and `.jpg` companions.

The `Paper/template/Makefile` build converts them to PDF for local paper builds.

The canonical figure generator is:

```bash
python Paper/figures/scripts/gen_paper_figures.py
```

The per-figure scripts in `Paper/figures/scripts/` are thin wrappers around that generator. Keep manuscript figures in the paper style: white background, minimal ornament, readable axes, and captions carrying interpretation rather than in-figure prose.
