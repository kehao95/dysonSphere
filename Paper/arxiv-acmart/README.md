# arXiv acmart Template

This is the default starting point for a new Quine paper that should compile from Markdown through Pandoc and produce an arXiv-ready bundle.

It is designed to be used in two ways:

1. Copy the whole directory into a new manuscript workspace and edit in place.
2. Keep your manuscript local, but include this template's `Makefile` from a thin wrapper `Makefile`.

## What It Includes

- generic build logic for `pdf`, `tex`, `html`, `docx`, and `arxiv`
- a Pandoc `acmart` LaTeX template
- the required `acmart` class/style files for arXiv submission
- starter `metadata.yaml`, `references.bib`, and section skeletons

## Thin Wrapper Pattern

```make
PAPER_TEMPLATE_ROOT := ../../templates/arxiv-acmart
PDF_NAME := my-paper.pdf
SECTIONS := sections/01-introduction.md \
            sections/02-method.md \
            sections/03-results.md \
            sections/04-conclusion.md

include $(PAPER_TEMPLATE_ROOT)/Makefile
```

Your local manuscript directory should then provide:

- `metadata.yaml`
- `references.bib`
- `sections/*.md`
- optional `figures/*.svg`
- optional local `templates/` or `support/` overrides if you do not want the defaults

## Section Source Conventions

- keep the canonical outline in `manuscript-plan.md`
- section draft files may keep a short local outline block at the top while the prose is still moving
- use bare Markdown headings such as `# Introduction` or `## Evidence`; do not manually prefix section numbers in source, because Pandoc/LaTeX will generate numbering automatically when `numbersections` is enabled
