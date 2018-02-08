import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'haitongh001@gmail.com'
msg['To'] = 'hh1674@nyu.edu'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('haitongh001@gmail.com', 'hy951208')
mailserver.sendmail('haitongh001@gmail.com', 'hh1674@nyu.edu',msg.as_string())
mailserver.quit()