import sys
import Crypto
from Crypto.PublicKey import RSA
import ast
import hashlib
from datetime import datetime

def rsaEnc(message, keyfile):
	
	pk_file = open(keyfile, "r")
	public_key = RSA.importKey(pk_file.read())
	pk_file.close()
	plaintext = str(datetime.now())+' '+message
	encrypted = public_key.encrypt(plaintext, 32)
	h = hashlib.sha256()
	h.update(plaintext)
	ciphertext = str(encrypted)+'\r'+'Digest Below\r'+h.hexdigest()
	'''
	f = open ('encryption.txt', 'w')
	f.write(str(encrypted)+'\r')
	f.write('Digest Below'+'\r')
	f.write(h.hexdigest())
	f.close()
	'''
	return ciphertext

