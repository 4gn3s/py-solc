import os

import pytest

from solc import (
    compile_files,
)

from solc.exceptions import ContractsNotFound


def test_compile_empty_folder():
    """Execute compile on a folder without contracts."""

    with pytest.raises(ContractsNotFound):
        compile_files([])
