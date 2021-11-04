Reproducible-Research-Standard-1.0.pdf:
%.pdf: %.md 
	pandoc $< -o $@
Reproducible-Research-Standard-1.0.md: render.py content.yaml codebook.yaml Reproducible-Research-Standard.md
	python $<