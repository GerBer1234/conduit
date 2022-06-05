import pytest
from vmi import cucc


def test_cucc():
    assert cucc() == 'csirkefarhat'
