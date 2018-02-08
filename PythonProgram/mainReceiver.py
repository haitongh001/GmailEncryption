import sys
import Crypto
from Crypto.PublicKey import RSA
import ast
from Tkinter import Tk
from tkFileDialog import askopenfilename
import hashlib

print "Welcome to Gmail Encryption System~\r"
print "~*********************************~\r"
print "Please input the message you want to decrypt:\r"
message = raw_input()
print "Please select the private key file that you want to use for decryption:\r"
Tk().withdraw()
keyfile = askopenfilename()
print(keyfile)
sk_file = open(keyfile, "r")
private_key = RSA.importKey(sk_file.read())
sk_file.close()
decrypted = private_key.decrypt(ast.literal_eval(str(message)))
print "The plaintext is as follows:\r"
print str(decrypted)
h = hashlib.sha256()
h.update(str(decrypted))
print "The corresponding hash value, please compare it with the hash value in the mail:\r"
print h.hexdigest()
