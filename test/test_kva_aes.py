from ..util import *
import logging
import pytest
import os

logger = logging.getLogger(__name__)

@pytest.fixture()
def config():
	config = read_config()
	return config

def test_kva_raes():
	aes = KVA_AES()
	assert aes.golden_key is not None and aes.iv is not None

def test_export_bins(config):
	bin_path = config['KVA']['BIN_PATH']
	file_list = os.listdir(bin_path)
	assert all(b in file_list for b in ['iv.bin', 'salt.bin', 'gk.bin'])

@pytest.mark.parametrize('test_str', ['TGiF', 'Gundam'])
def test_encrypt_decrypt(test_str: str):
	aes = KVA_AES()
	encrypt_str = aes.encrypt(test_str)
	logger.info(f'Encrypt {test_str} as {encrypt_str}')
	assert test_str == aes.decrypt(encrypt_str)