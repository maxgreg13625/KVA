from ..util import *
import pytest

@pytest.fixture()
def config():
	config = read_config()
	return config

def test_raes(config):
	aes = KVA_AES()
	assert aes.golden_key is not None and aes.iv is not None