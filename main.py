from util import *
import logging

logger = logging.getLogger(__name__)

def main():
	kva_aes = KVA_AES()
	logging.info(f'{kva_aes.iv}  {kva_aes.golden_key}')

if __name__ == '__main__':
	main()
