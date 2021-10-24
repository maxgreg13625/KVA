import pytest
from ..util import *

@pytest.mark.parametrize('seed', [32, 64])
def test_get_random_key(seed):
	key = get_random_key(seed)
	assert seed is not None and type(key) == bytes
