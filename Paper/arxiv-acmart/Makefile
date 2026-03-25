# Shared build logic for Pandoc -> acmart -> arXiv papers.
# Override variables before include, or copy this directory and edit in place.

OUT_DIR ?= output
SRC_DIR ?= sections
META ?= metadata.yaml
BIB ?= references.bib

SECTIONS ?= $(SRC_DIR)/01-paper.md
FIGURES ?= $(wildcard figures/concept/*.svg) $(wildcard figures/results/*.svg)
FIGURE_PDFS ?= $(FIGURES:.svg=.pdf)

FULL_MD ?= $(OUT_DIR)/full_paper.md
PDF_NAME ?= paper.pdf
PDF ?= $(OUT_DIR)/$(PDF_NAME)
LATEX_FILE ?= $(OUT_DIR)/paper.tex
HTML ?= $(OUT_DIR)/paper.html
DOCX ?= $(OUT_DIR)/paper.docx
TEMPLATE ?= templates/acmart.latex

ARXIV_DIR ?= $(OUT_DIR)/arxiv_submission
ARXIV_TEX ?= $(ARXIV_DIR)/main.tex
ARXIV_ZIP ?= $(OUT_DIR)/arxiv_submission.tar.gz

SUPPORT_DIR ?= support/acmart
SUPPORT_FILES ?= $(SUPPORT_DIR)/acmart.cls \
                 $(SUPPORT_DIR)/acmauthoryear.bbx \
                 $(SUPPORT_DIR)/acmauthoryear.cbx \
                 $(SUPPORT_DIR)/acmdatamodel.dbx \
                 $(SUPPORT_DIR)/acmnumeric.bbx \
                 $(SUPPORT_DIR)/acmnumeric.cbx \
                 $(SUPPORT_DIR)/totpages.sty

RESOURCE_PATH ?= .:$(SRC_DIR):figures:figures/concept:figures/results

PANDOC_PDF_OPTS := --standalone \
                   --from markdown \
                   --pdf-engine=tectonic \
                   --template=$(TEMPLATE) \
                   --resource-path=$(RESOURCE_PATH) \
                   --citeproc \
                   --bibliography=$(BIB)
PANDOC_LATEX_OPTS := --standalone \
                     --from markdown \
                     --to latex \
                     --template=$(TEMPLATE) \
                     --resource-path=$(RESOURCE_PATH) \
                     --citeproc \
                     --bibliography=$(BIB)

.PHONY: all clean pdf tex html docx setup arxiv arxiv-clean check

all: pdf arxiv

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
	@if [ -z "$(strip $(SECTIONS))" ]; then \
		echo "ERROR: No section files found under $(SRC_DIR)/"; \
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
	rsvg-convert -f pdf -o $@ $<

pdf: check setup $(FULL_MD) $(FIGURE_PDFS)
	pandoc $(FULL_MD) -o $(PDF) $(PANDOC_PDF_OPTS)
	@echo "PDF generated at $(PDF)"

tex: check $(FULL_MD) $(FIGURE_PDFS)
	pandoc $(FULL_MD) -o $(LATEX_FILE) $(PANDOC_LATEX_OPTS)
	@echo "TeX generated at $(LATEX_FILE)"

html: check $(FULL_MD)
	pandoc $(FULL_MD) -o $(HTML) --standalone --resource-path=$(RESOURCE_PATH) --citeproc --bibliography=$(BIB)
	@echo "HTML generated at $(HTML)"

docx: check $(FULL_MD)
	pandoc $(FULL_MD) -o $(DOCX) --resource-path=$(RESOURCE_PATH) --citeproc --bibliography=$(BIB)
	@echo "DOCX generated at $(DOCX)"

arxiv: check $(FULL_MD) $(FIGURE_PDFS)
	@echo "=== Building ArXiv submission package ==="
	rm -rf $(ARXIV_DIR) $(ARXIV_ZIP)
	mkdir -p $(ARXIV_DIR)/figures
	@if [ -n "$(strip $(FIGURE_PDFS))" ]; then \
		echo "Copying figure PDFs..."; \
		cp $(FIGURE_PDFS) $(ARXIV_DIR)/figures/; \
	fi
	cp $(BIB) $(ARXIV_DIR)/
	cp $(SUPPORT_FILES) $(ARXIV_DIR)/
	@echo "Generating LaTeX..."
	pandoc $(FULL_MD) -o $(ARXIV_TEX) $(PANDOC_LATEX_OPTS)
	@echo "Post-processing TeX for ArXiv compatibility..."
	sed -i.bak 's/\.svg/.pdf/g' $(ARXIV_TEX)
	sed -i.bak 's/\\includesvg/\\includegraphics/g' $(ARXIV_TEX)
	sed -i.bak '/\\usepackage{svg}/d' $(ARXIV_TEX)
	sed -i.bak '/\\usepackage{lmodern}/d' $(ARXIV_TEX)
	sed -i.bak '/IfFileExists{microtype.sty}/,/^}{}/d' $(ARXIV_TEX)
	rm -f $(ARXIV_TEX).bak
	rm -f $(ARXIV_DIR)/main.pdf $(ARXIV_DIR)/*.aux $(ARXIV_DIR)/*.log $(ARXIV_DIR)/*.out
	@echo "Creating submission tarball..."
	tar -czvf $(ARXIV_ZIP) -C $(ARXIV_DIR) .
	@echo ""
	@echo "=== ArXiv submission package ready ==="
	@echo "Directory: $(ARXIV_DIR)/"
	@echo "Tarball:   $(ARXIV_ZIP)"

arxiv-clean:
	rm -rf $(ARXIV_DIR) $(ARXIV_ZIP)

clean:
	rm -f $(FULL_MD) $(PDF) $(LATEX_FILE) $(HTML) $(DOCX)
	rm -rf $(ARXIV_DIR) $(ARXIV_ZIP)
	rm -rf $(OUT_DIR)
	rm -f $(FIGURE_PDFS)
