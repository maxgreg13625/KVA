from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from .util import *

class KVA_AES:
	def __init__(self, golden_key: bytes=None, iv: bytes=None) -> None:
		self.config = read_config()
		self.golden_key = golden_key
		self.iv = iv
	
		if self.golden_key is None or self.iv is None:
			self._setting_golden_key_and_iv()
			self.export_bins()
		else:
			self.cipher = AES.new(key=self.golden_key,\
				mode=AES.MODE_CBC, iv=self.iv)

	def _setting_golden_key_and_iv(self):
		pwd = self.config['KVA']['PWD']
		seed = int(self.config['KVA']['SEED'])
		# get salt and golden key
		key_dict = get_golden_key_dict(pwd, seed)
		
		self.cipher = AES.new(key_dict[pwd][1], AES.MODE_CBC)
		self.golden_key = key_dict[pwd][1]
		self.salt = key_dict[pwd][0]
		self.iv = self.cipher.iv

	def export_bins(self):
		export_bin(self.iv, 'iv')
		export_bin(self.salt, 'salt')
		export_bin(self.golden_key, 'gk')
	
	def encrypt(self, input_str: str):
		input_str_bytes = input_str.encode()
		result_bytes = self.cipher.encrypt(
			pad(input_str_bytes, AES.block_size))
		
		# need further check how to transform to human readable str...
		return result_bytes.decode()
	
	def decrypt(self, input_str: str):
		input_str_bytes = input_str.encode()
		result_bytes = unpad(self.cipher.decrypt(input_str_bytes),
			AES.block_size)
		return result_bytes.decode()
