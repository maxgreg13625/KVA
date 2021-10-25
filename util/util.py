import configparser
import os

def read_config():
	config = configparser.ConfigParser()
	config.read(f'{os.path.dirname(__file__)}/../config.ini')
	return config

def get_random_key(seed: int=32) -> bytes:
	"""
	Return random key generated by Crypto.Random
	"""
	from Crypto.Random import get_random_bytes
	random_key = get_random_bytes(seed)
	return random_key

def get_golden_key(pwd: str, salt: bytes, key_length: int=32) -> bytes:
	"""
	Generate golden key
	"""
	from Crypto.Protocol.KDF import PBKDF2
	golden_key = PBKDF2(pwd, salt, dkLen=key_length)
	return golden_key

def get_golden_key_dict(pwd: str) -> dict:
	"""
	Generate golden key dict
	"""
	salt = get_random_key()
	key = get_golden_key(pwd, salt)
	return {pwd: (salt, key)}

def export_bin(content: bytes, name: str) -> None:
	config = read_config()
	bin_path = config['KVA']['BIN_PATH']

	with open(f'{bin_path}/{name}.bin', "wb") as f:
		f.write(content)

def import_bin(name: str) -> bytes:
	config = read_config()
	bin_path = config['KVA']['BIN_PATH']

	result = None
	with open(f'{bin_path}/{name}.bin', 'rb') as f:
		result = f.read()
	return result
