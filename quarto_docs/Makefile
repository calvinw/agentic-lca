.PHONY: all regenerate render serve preview clean

all: regenerate render

regenerate:
	python3 generate_quarto_yml.py

render:
	quarto render

serve: render
	cp skills/*.md _site/skills/
	python3 -m http.server 8080 --directory _site
	rm -f _site/skills/*.md

preview: serve

clean:
	rm -rf _site
