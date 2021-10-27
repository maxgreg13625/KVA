from ..util import *
import pytest
import os

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