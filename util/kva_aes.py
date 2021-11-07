from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from .util import *
from base64 import b64decode, b64encode
import logging

logger = logging.getLogger(__name__)

class KVA_AES:
	def __init__(self, golden_key: bytes=None, iv: bytes=None) -> None:
		self.config = read_config()
		self.golden_key = golden_key
		self.iv = iv
		self.block_size = 64

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

	def _reset_cipher(self):
		# cipher is stateful which mean can't encrypt and decrypt with same object
		# reference: https://github.com/Legrandin/pycryptodome/blob/v3.7.2/lib/Crypto/Cipher/_mode_eax.py#L205
		if self.golden_key is not None and\
			self.iv is not None:
			self.cipher = AES.new(key=self.golden_key,\
				mode=AES.MODE_CBC, iv=self.iv)

	def export_bins(self):
		export_bin(self.iv, 'iv')
		export_bin(self.salt, 'salt')
		export_bin(self.golden_key, 'gk')
	
	def encrypt(self, input_str: str):
		self._reset_cipher()
		result_bytes = self.cipher.encrypt(
			pad(input_str.encode(), AES.block_size))

		# use b64encode to transform human readable str
		return b64encode(result_bytes).decode()

	def encrypt_list(self, input_list: list):
		self._reset_cipher()
		result_list = list()

		for ts in input_list:
			result_list.append(
				b64encode(self.cipher.encrypt(
					pad(ts.encode(), AES.block_size))).decode())
		return result_list

	def decrypt(self, input_str: str):
		self._reset_cipher()
		input_str_bytes = b64decode(input_str.encode())
		result_bytes = unpad(self.cipher.decrypt(input_str_bytes), AES.block_size)
		return result_bytes.decode()

	def decrypt_list(self, input_list: list):
		self._reset_cipher()
		result_list = list()

		for ts in input_list:
			result_list.append(
				unpad(self.cipher.decrypt(
					b64decode(ts.encode())), AES.block_size).decode())
		return result_list