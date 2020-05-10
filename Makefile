SRCDIR=src

.PHONY: setup
setup:
	poetry install --extras "dev doc test"
	poetry run pre-commit install --overwrite --install-hooks

.PHONY: lint
lint:
	poetry run pre-commit run -a

.PHONY: test tests
test tests:
	poetry run nox

.PHONY: docs
docs:
	cd docs \
		&& poetry run make html \
		&& cd -

.PHONY: docs-server
docs-server: ip ?= 127.0.0.1
docs-server: port ?= 60666
docs-server:
	cd docs/_build/html \
		&& python -m http.server --bind "$(ip)" "$(port)" \
		&& cd -

.PHONY: change
change: issue ?= _$(shell < /dev/urandom tr -dc A-Za-z0-9 | head -c9)
change: type ?= feature
change: change_file := changes/$(issue).$(type).md
change:
	touch $(change_file)
	$(EDITOR) $(change_file)

.PHONY: clog
clog:
	poetry run towncrier --draft --version=Unreleased

.PHONY: release
release: part ?= patch
release: version := $(shell \
	poetry run bumpversion --dry-run --allow-dirty --list $(part) \
	| grep '^current_version=' \
	| cut -d= -f2 \
)
release: new := $(shell \
	poetry run bumpversion --dry-run --allow-dirty --list $(part) \
	| grep '^new_version=' \
	| cut -d= -f2 \
)
release:
	@echo "bump $(part) => $(version) -> $(new)"
	poetry run towncrier --yes --version '$(new)'
	git commit -m ':pencil: add CHANGELOG for $(new)' --no-verify
	poetry run bumpversion '$(part)' --commit-args='--no-verify'

.PHONY: publish
publish:
	poetry publish
