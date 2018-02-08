import msvcrt,sys
def pwd_input():    
	chars = []
	chars_n = []
	while True:
		while True:  
			newChar = msvcrt.getch().decode(encoding="utf-8")   
			if newChar in '\r\n':              
				break   
			elif newChar == '\b':
				if chars:    
					del chars[-1]   
					msvcrt.putch('\b'.encode(encoding='utf-8'))
					msvcrt.putch(' '.encode(encoding='utf-8'))
					msvcrt.putch('\b'.encode(encoding='utf-8'))                   
			else:  
				chars.append(newChar)  
				msvcrt.putch('*'.encode(encoding='utf-8'))
		print "\r\nPlease confirm your password:\r"
		while True:  
			confirm = msvcrt.getch().decode(encoding="utf-8")   
			if confirm in '\r\n':              
				break   
			elif confirm == '\b':
				if chars_n:    
					del chars_n[-1]   
					msvcrt.putch('\b'.encode(encoding='utf-8'))
					msvcrt.putch(' '.encode(encoding='utf-8'))
					msvcrt.putch('\b'.encode(encoding='utf-8'))                   
			else:  
				chars_n.append(confirm)  
				msvcrt.putch('*'.encode(encoding='utf-8'))
		if (chars == chars_n):              
			break   
		else:  
			print('Passwords do not match, try again!\n') 
	
	return (''.join(chars) )

	'''
	
import sys
import getpass
def pwd_input():    
    chars = []
    while True:  
        newChar = getpass.getpass()
        confirm = getpass.getpass('Please Confirm Your Password')
        if (newChar == confirm):    
            break   
                                   
        else:  
            print('Passwords Do Not Match, Try Again \n') 
            
    return (''.join(chars) )  
'''
