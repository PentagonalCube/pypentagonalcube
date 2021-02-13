push:
	python increment_version.py
	git add VERSION.json
	git add VERSION.py
	git commit -m ":bookmark: Adding automatic version increment"
	git push
