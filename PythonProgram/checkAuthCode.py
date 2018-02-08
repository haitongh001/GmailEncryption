#!/usr/bin/python
import Crypto

def checkAuthCode(encryptedFileName, intendedAuthCode) :
    decFile = open(encryptedFileName, 'r+')
    f = open('encryption.txt', 'r')
    message = f.read()

    sk_file = open("./private.txt", "r")
    private_key = RSA.importKey(sk_file.read())
    sk_file.close()
    decrypted = private_key.decrypt(ast.literal_eval(str(message)))

    f = open ('decryption.txt', 'w')
    decFile.write(str(decrypted))
    for line in decFile.input([decFile]):
        currLine = line
    if(intendedAuthCode == currLine):
        print("The authentication codes match. The email has not been \
        modified by an attacker.\n")
    else :
        print("The authentication codes do NOT match. The email HAS been \
        modified by an attacker.\n")
    encFile.close()

    
    
