from pathlib import Path

import nox


PYTHON_VERSIONS = ["3.6", "3.7", "3.8"]
TOOLS_TEST = [
    ".",
    "pytest",
]

SOURCE_DIRECTORY = Path("src")
PYTHON_FILES_SOURCE = list(SOURCE_DIRECTORY.glob("**/*.py"))

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=PYTHON_VERSIONS)
def test(session):
    """ Run doctests and pytest test suit. """
    session.install(*TOOLS_TEST)
    session.run("python", "-m", "doctest", *(str(p) for p in PYTHON_FILES_SOURCE))
    session.run("pytest", *session.posargs)
