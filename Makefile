VERSION := $(shell python increment_version.py)

push:	
	git add VERSION.json
	git add VERSION.py
	git commit -m ":bookmark: $(VERSION)"
	git push
