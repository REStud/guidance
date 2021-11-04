all: Reproducible-Research-Standard-1.0.pdf restud.pdf
%.pdf: %.md 
	pandoc $< -o $@
Reproducible-Research-Standard-1.0.md: render.py rule.csv item.csv topic.csv 
	python $< > $@
restud.md: render.py rule.csv item.csv topic.csv restud.csv 
	python $< restud > $@