import sys
from password import pwd_input
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import Encoders
from Tkinter import Tk
from tkFileDialog import askopenfilename

def keyGen(name):
	'''
	exponent = 65537 in PEM format
	'''
	from Crypto.PublicKey import RSA 
	new_key = RSA.generate(bits=2048, e=65537) 
	public_key = new_key.publickey().exportKey("PEM") 
	private_key = new_key.exportKey("PEM")
	sk_file = open("./keys/"+name+"_private.txt", "w")
	sk_file.write(private_key)
	sk_file.close()
	pk_file = open("./keys/"+name+"_public.txt", "w")
	pk_file.write(public_key)
	pk_file.close()
	#return private_key, public_key
	
print "Welcome to Gmail Encryption System, you can generate a pair of keys here~\r"
print "~***********************************************************************~\r"
print "Please input your email address:\r"
from_addr = raw_input()
confirm_addr= raw_input("Please Confirm Your Email Address:\n")
while(from_addr <> confirm_addr):
	print "Emails Do Not Match, Please Try Again \r"
	print "Please input your email address:\r"
	from_addr = raw_input()
	print "\r Please Confirm Your Email Address:\n"
	confirm_addr= raw_input()
print "Please enter the password:\r"
password = pwd_input()
print "\r\nKey Generating~~~"
keyGen(from_addr)
print "Do you want to send the public key to some person? [y/n]\r"
ans = raw_input()
if ans == 'y':
	print "\rPlease input the destination address:\r"
	to_addr = raw_input()
	msg = MIMEMultipart()
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Subject'] = "Public Key File"
	print "Please select the public key file that you want to send:\r"
	Tk().withdraw()
	keyfile = askopenfilename()
	print(keyfile)
	attachment = MIMEBase('application', "octet-stream")
	attachment.set_payload(open(keyfile, "rb").read())
	Encoders.encode_base64(attachment)
	command= 'attachment; filename='
	command =command+from_addr+"_public.txt"
	
	attachment.add_header('Content-Disposition', command)
	msg.attach(attachment)
	mailserver = smtplib.SMTP('smtp.gmail.com',587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login(from_addr, password)
	mailserver.sendmail(from_addr, to_addr ,msg.as_string())
	print "Done~\r"
	mailserver.quit()