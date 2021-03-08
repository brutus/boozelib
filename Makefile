SRCDIR=src

.PHONY: setup
setup:
	poetry install --extras "dev doc test"
	poetry run pre-commit install --overwrite --install-hooks

.PHONY: lint
lint:
	poetry run pre-commit run --all-files $(args)

.PHONY: test tests
test tests:
	poetry run nox $(args)

.PHONY: docs
docs: ip ?= 127.0.0.1
docs: port ?= 60666
docs:
	poetry run sphinx-autobuild docs docs/_build/html -H "$(ip)" -p "$(port)"

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
	poetry publish --build
