import keyGen
import keysend
import mainReceiver
import mainSender
import requestPublicKey


def menu():
    while(True):
        
        choice = raw_input("Press 1 to Generate a new Key, Press 2 to Send your Key to someone, Press 3 to request a public key from someone, Press 4 to Encrypt a Message, Press 5 to Decrypt a Message\n")
        if(choice == '1'):
            keyGen.runKeyGen()
        if(choice == '2'):
            keysend.runKeySend()
        if(choice == '3'):
            requestPublicKey.runReq()
        if(choice == '4'):
            mainSender.mainSender()
        if(choice == '5'):
            mainReceiver.mainReceiver()


menu()
