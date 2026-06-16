.PHONY: all regenerate render serve preview clean

all: regenerate render

regenerate:
	python3 generate_quarto_yml.py
	python3 ../skills_sessions/generate_sessions.py
	python3 ../plan/generate_plans.py
	python3 ../lca_analysis/generate_analyses.py

render:
	quarto render

serve: render
	python3 -m http.server 8080 --directory _site

preview: serve

clean:
	rm -rf _site
