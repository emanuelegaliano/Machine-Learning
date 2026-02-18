MAIN = "Machine Learning"
OUTDIR = out

all:
	mkdir -p $(OUTDIR)
	latexmk -pdf \
		-interaction=nonstopmode \
		-synctex=1 \
		-shell-escape \
		-outdir=$(OUTDIR) \
		$(MAIN).tex
	cp $(OUTDIR)/$(MAIN).pdf .

clean:
	latexmk -C -outdir=$(OUTDIR)
	rm -rf $(OUTDIR)
