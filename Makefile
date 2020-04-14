SRCDIR=src

.PHONY: setup
setup:
	pipenv sync --dev
	pipenv clean
	pipenv run flit install --symlink
	pipenv run pre-commit install --overwrite --install-hooks

.PHONY: lint
lint:
	pipenv run pre-commit run -a

.PHONY: tests
tests:
	pipenv run nox

.PHONY: docs
docs:
	cd docs && pipenv run make html && cd -

.PHONY: change
change: issue ?= $(shell < /dev/urandom tr -dc A-Za-z0-9 | head -c12)
change: type ?= feature
change: change_file := changes/$(issue).$(type)
change:
	touch $(change_file)
	$(EDITOR) $(change_file)

.PHONY: clog
clog:
	pipenv run towncrier --draft --version=Unreleased

.PHONY: release
release: part ?= patch
release: version := $(shell \
	pipenv run bumpversion --dry-run --allow-dirty --list $(part) \
	| grep '^current_version=' \
	| cut -d= -f2 \
)
release: new := $(shell \
	pipenv run bumpversion --dry-run --allow-dirty --list $(part) \
	| grep '^new_version=' \
	| cut -d= -f2 \
)
release:
	@echo "bump $(part) => $(version) -> $(new)"
	pipenv run towncrier --yes --version '$(new)'
	git commit -m ':pencil: add CHANGELOG for $(new)' --no-verify
	pipenv run bumpversion '$(part)'

.PHONY: publish
publish:
	pipenv run flit publish
