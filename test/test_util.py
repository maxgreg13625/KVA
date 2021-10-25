from ..util import *
import logging
import pytest

logger = logging.getLogger(__name__)

@pytest.mark.parametrize('seed', [32, 64])
def test_get_random_key(seed: int):
	key = get_random_key(seed)

	logger.info(f'random key: {key}')
	assert key is not None and type(key) == bytes

@pytest.mark.parametrize('pwd', ['test'])
def test_get_golden_key_dict(pwd: str):
	key_dict = get_golden_key_dict(pwd)

	assert key_dict is not None and type(key_dict) == dict
	assert pwd in key_dict and len(key_dict[pwd]) == 2

def test_config():
	config = read_config()
	assert 'KVA' in config
	assert 'PWD' in config['KVA'] and 'BIN_PATH' in config['KVA']

@pytest.fixture()
def config():
	config = read_config()
	return config

def test_salt_bin(config):
	pwd = config['KVA']['PWD']
	# get salt and golden key
	key_dict = get_golden_key_dict(pwd)

	export_bin(key_dict[pwd][0], 'salt_test')
	salt_from_file = import_bin('salt_test')
	# check salt is the same after land to file
	assert key_dict[pwd][0] == salt_from_file
	# check can get same golden key with salt read from file
	assert key_dict[pwd][1] == get_golden_key(pwd, salt_from_file)
