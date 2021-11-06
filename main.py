from util import *
import logging

logger = logging.getLogger(__name__)

def main():
	kva_aes = KVA_AES()
	logger.info(f'{kva_aes.iv}  {kva_aes.golden_key}')
	encrypt_str = kva_aes.encrypt('this is test')
	logger.info(f'{encrypt_str}')
	decrypt_str = kva_aes.decrypt(encrypt_str)
	logger.info(f'{decrypt_str}')

if __name__ == '__main__':
	main()
