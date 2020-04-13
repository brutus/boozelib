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