from pathlib import Path

import nox
from nox.sessions import Session


PYTHON_VERSIONS = ["3.6", "3.7", "3.8", "3.9"]
TOOLS_TEST = [
    ".",
    "ward",
]

SOURCE_DIRECTORY = Path("src")
PYTHON_FILES_SOURCE = list(SOURCE_DIRECTORY.glob("**/*.py"))

nox.options.reuse_existing_virtualenvs = True


@nox.session(python=PYTHON_VERSIONS)
def test(session: Session) -> None:
    """ Run doctests and ward test suit. """
    session.install(*TOOLS_TEST)
    session.run("python", "-m", "doctest", *(str(p) for p in PYTHON_FILES_SOURCE))
    session.run("ward", *session.posargs)
