from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from .util import *

class KVA_AES:
	def __init__(self, golden_key: bytes=None, iv: bytes=None) -> None:
		self.config = read_config()
		self.golden_key = golden_key
		self.iv = iv
	
		if self.golden_key is None or self.iv is None:
			self._setting_golden_key_and_iv()
		else:
			self.cipher = AES.new(key=self.golden_key,\
				mode=AES.MODE_CBC, iv=self.iv)

	def _setting_golden_key_and_iv(self):
		pwd = self.config['KVA']['PWD']
		# get salt and golden key
		key_dict = get_golden_key_dict(pwd)
		
		self.cipher = AES.new(key_dict[pwd][1], AES.MODE_CBC)
		self.golden_key = key_dict[pwd][1]
		self.salt = key_dict[pwd][0]
		self.iv = self.cipher.iv
