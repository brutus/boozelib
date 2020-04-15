from pathlib import Path

import nox


PYTHON_VERSIONS = ["2.7", "3.6", "3.7", "3.8"]

SOURCE_DIRECTORY = "src"
TEST_DIRECTORY = "tests"

PYTHON_FILES_SOURCE = list(Path(SOURCE_DIRECTORY).glob("**/*.py"))
PYTHON_FILES_TEST = list(Path(TEST_DIRECTORY).glob("**/*.py"))
PYTHON_FILES_EXTRA = [
    Path("noxfile.py"),
]

PYTHON_FILES = [
    str(p) for p in PYTHON_FILES_SOURCE + PYTHON_FILES_TEST + PYTHON_FILES_EXTRA
]

TOOLS_LINT = [
    "black",
    "flakehell",
    "reorder_python_imports",
]

TOOLS_TEST = [
    "pytest",
    ".",
]

nox.options.reuse_existing_virtualenvs = True


@nox.session
def lint(session):
    """ Check Python style. """
    session.install(*TOOLS_LINT)
    # check syntax
    session.run("flakehell", "lint", *PYTHON_FILES)
    # check style
    session.run("black", "--check", "--quiet", *PYTHON_FILES)
    # check imports
    session.run(
        "reorder-python-imports",
        "--application-directories",
        f".:{SOURCE_DIRECTORY}:{TEST_DIRECTORY}",
        "--separate-relative",
        "--diff-only",
        *PYTHON_FILES
    )


@nox.session(python=PYTHON_VERSIONS)
def test(session):
    """ Run doctests and ward test suit. """
    session.install(*TOOLS_TEST)
    session.run("python", "-m", "doctest", *(str(p) for p in PYTHON_FILES_SOURCE))
    session.run("pytest", *session.posargs)
