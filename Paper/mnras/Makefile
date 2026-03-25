# Pandoc -> MNRAS build for review/submission-style PDFs.

OUT_DIR ?= output
SECTIONS ?= ../content/manuscript.md
META ?= metadata.yaml
BIB ?= ../references/bibliography.bib

FIGURES ?= $(wildcard ../figures/concept/*.svg) $(wildcard ../figures/results/*.svg)
FIGURE_PDFS ?= $(FIGURES:.svg=.pdf)

FULL_MD ?= $(OUT_DIR)/full_paper.md
PDF_NAME ?= paper.pdf
PDF ?= $(OUT_DIR)/$(PDF_NAME)
LATEX_FILE ?= $(OUT_DIR)/paper.tex
HTML ?= $(OUT_DIR)/paper.html
DOCX ?= $(OUT_DIR)/paper.docx
TEMPLATE ?= ../templates/mnras/mnras.latex

SUPPORT_DIR ?= ../templates/mnras/support/mnras
SUPPORT_FILES ?= $(SUPPORT_DIR)/mnras.cls $(SUPPORT_DIR)/mnras.bst

RESOURCE_PATH ?= .:../content:../figures:../figures/concept:../figures/results

PANDOC_LATEX_OPTS := --standalone \
                     --from markdown \
                     --to latex \
                     --template=$(TEMPLATE) \
                     --resource-path=$(RESOURCE_PATH) \
                     --citeproc \
                     --bibliography=$(BIB)

.PHONY: all clean pdf tex html docx setup check

all: pdf

setup:
	mkdir -p $(OUT_DIR)

check:
	@if [ ! -f "$(META)" ]; then \
		echo "ERROR: Missing $(META)"; \
		exit 1; \
	fi
	@if [ ! -f "$(BIB)" ]; then \
		echo "ERROR: Missing $(BIB)"; \
		exit 1; \
	fi
	@if [ ! -f "$(TEMPLATE)" ]; then \
		echo "ERROR: Missing $(TEMPLATE)"; \
		exit 1; \
	fi
	@for f in $(SECTIONS) $(SUPPORT_FILES); do \
		if [ ! -f "$$f" ]; then \
			echo "ERROR: Missing $$f"; \
			exit 1; \
		fi; \
	done
	@numbered_headings=$$(grep -nE '^(#{1,6}) [0-9]+([.][0-9]+)*([.])? ' $(SECTIONS) || true); \
	if [ -n "$$numbered_headings" ]; then \
		echo "WARNING: Section headings appear to include manual numbering."; \
		echo "$$numbered_headings"; \
		echo "WARNING: Use bare headings in manuscript source and let Pandoc/LaTeX generate numbering."; \
	fi

$(FULL_MD): $(META) $(SECTIONS) | setup
	awk 'FNR==1 && NR!=1 {print ""} {print}' $(META) $(SECTIONS) > $(FULL_MD)

$(FIGURE_PDFS): %.pdf: %.svg
	rsvg-convert -f pdf -o $@.tmp $<
	gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -sOutputFile=$@ $@.tmp
	rm -f $@.tmp

$(LATEX_FILE): $(FULL_MD) $(FIGURE_PDFS) $(TEMPLATE) $(META) $(BIB) | setup
	pandoc $(FULL_MD) -o $(LATEX_FILE) $(PANDOC_LATEX_OPTS)
	@echo "TeX generated at $(LATEX_FILE)"

pdf: check $(LATEX_FILE)
	ln -sfn ../figures figures
	ln -sfn ../../figures $(OUT_DIR)/figures
	TEXINPUTS=.:$(SUPPORT_DIR): pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUT_DIR) $(LATEX_FILE)
	TEXINPUTS=.:$(SUPPORT_DIR): pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUT_DIR) $(LATEX_FILE)
	@echo "PDF generated at $(PDF)"

tex: check $(LATEX_FILE)

html: check $(FULL_MD)
	pandoc $(FULL_MD) -o $(HTML) --standalone --resource-path=$(RESOURCE_PATH) --citeproc --bibliography=$(BIB)
	@echo "HTML generated at $(HTML)"

docx: check $(FULL_MD)
	pandoc $(FULL_MD) -o $(DOCX) --resource-path=$(RESOURCE_PATH) --citeproc --bibliography=$(BIB)
	@echo "DOCX generated at $(DOCX)"

clean:
	rm -rf $(OUT_DIR)
	rm -f $(FIGURE_PDFS)
