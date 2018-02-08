from Tkinter import Tk
from tkFileDialog import askopenfilename
from rsaEnc import rsaEnc
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import Encoders
from password import pwd_input

print "Welcome to Gmail Encryption System~\r"
print "~*********************************~\r"
print "Please input your email address:\r"
from_addr = raw_input()
print "Login password:(Press 'Enter' as end)\r"
password = pwd_input()
print "\rPlease input the destination address:\r"
to_addr = raw_input()
print "Please select the public key file that you want to use:\r"
Tk().withdraw()
keyfile = askopenfilename()
print(keyfile)
print "What is the subject of this email:\r"
subject = raw_input()
print "Do you want to input the message below[1] or attach a file[2]:\r"
ans = raw_input()
if ans == 1:
	print "Please enter the message below:\r"
	message = raw_input()
else:
	print "Please upload the file:\r"
	Tk().withdraw()
	uploadfile = askopenfilename()
	print(uploadfile)
	f = open(uploadfile, 'r')
	message = f.read()
ciphertext = rsaEnc(message, keyfile)
print "Sending~~~"
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
if ans == 1:
	msg.attach(MIMEText(ciphertext))
else: 
	attachment = MIMEBase('application', "octet-stream")
	encryptedfile = open("./encryptedfile.txt", "w")
	encryptedfile.write(ciphertext)
	encryptedfile.close()
	attachment.set_payload(open("./encryptedfile.txt", "rb").read())
	Encoders.encode_base64(attachment)
	attachment.add_header('Content-Disposition', 'attachment; filename="file.txt"')
	msg.attach(attachment)
mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(from_addr, password)
mailserver.sendmail(from_addr, to_addr,msg.as_string())
mailserver.quit()




