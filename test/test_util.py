import pytest
from ..util import *

@pytest.mark.parametrize('seed', [32, 64])
def test_get_random_key(seed: int):
	key = get_random_key(seed)
	assert key is not None and type(key) == bytes

@pytest.mark.parametrize('pwd', ['test'])
def test_get_golden_key_dict(pwd: str):
	key_dict = get_golden_key_dict(pwd)

	assert key_dict is not None and type(key_dict) == dict
	assert pwd in key_dict and len(key_dict[pwd]) == 2

def test_config():
	config = read_config()
	assert 'KVA' in config
