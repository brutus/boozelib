from pathlib import Path

import nox


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

nox.options.reuse_existing_virtualenvs = True


def check_syntax(session):
    """ Check Python syntax. """
    session.install("flakehell")
    session.run("flakehell", "lint", *PYTHON_FILES)


@nox.session
def check_style(session):
    """ Check Python style. """
    session.install("black")
    session.run("black", "--check", *PYTHON_FILES)


@nox.session
def check_imports(session):
    """ Check Python imports. """
    session.install("reorder_python_imports")
    session.run(
        "reorder-python-imports",
        "--application-directories",
        ".:src",
        "--diff-only",
        *PYTHON_FILES
    )


@nox.session
def doc_tests(session):
    """ Run all integration tests. """
    session.run("python", "-m", "doctest", *(str(p) for p in PYTHON_FILES_SOURCE))


@nox.session
def integration_tests(session):
    """ Run all integration tests. """
    session.install("ward")
    session.install("flit")
    session.run("flit", "install", "--symlink")
    session.run("ward", "--tags", "integration")
