### Automate sending a CSV through Gmail
	## IMAP: Internet Messaging Access Protocol (keep everything synced) (retrieval)

import smtplib ## Simple Mail Transfer Protocol (delivery)
from email.mime.multipart import MIMEMultipart ## Multipurpose Internet Mail Extension
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import re




##---------------------
## Input
## ---------------------

	## User credentials
gmail_user = 'fred.corpuz06@gmail.com'
gmail_password = 'qactextlabpython'

	## Email Metadata
to = ['lmedina@wesleyan.edu', 'kkoech@wesleyan.edu', 'fcorpuz@wesleyan.edu']
# to = 'fcorpuz@wesleyan.edu'
subject = '[Text Lab] Send Email w/ .csv through Python'
body = 'Test attach \n Hey, what\'s up?\n\n - Fred'
doc = r'P:\QAC\Projects\datadive17\NotAnAccident\Fred_files\ManualGeoLoc1228_clean.csv'



##------------------------------
## Test for 1 email
##-----------------------------
'''
	## Email Text
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = ', '.join(to) ## needs to be a string (just a visible address)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

	# Setting up type
# ctype, encoding = mimetypes.guess_type(file) ## returns a tuple (type, encoding)
# if ctype is None or encoding is not None:
# 	ctype = 'application/octet-stream'
# maintype, subtype = ctype.split('/', 1)
# att = MIMEBase(maintype, subtype)	
	
	# Attachment
match = re.search(r'[^\\]*\.[a-z]{3}$', str(doc))
doc_name = doc[match.start():match.end()]
f = open(doc, 'rb')
att = MIMEBase('application', 'csv')
att.set_payload(f.read())
f.close()
encoders.encode_base64(att)
att.add_header('Content-Disposition', 'attachment', filename=doc_name)
msg.attach(att)



	# code to send email
try:
		## ServerLocation: smtp.gmail.com is an outward facing interface to their server (used by Outlook, etc.)
		## PortToUse
	server = smtplib.SMTP('smtp.gmail.com', 587)
	# server.ehlo()
	server.starttls() ## Upgrade to secure connection
	server.login(gmail_user, gmail_password)

	server.sendmail(gmail_user,to, msg.as_string()) ## to needs t obe a list
	server.close()

	print 'Email sent!'
except:
	print 'Something went wrong...'

'''

##-----------------------
## Send message
##------------------------------
	## @params Gmail Username, PS, Email address of recepient/s in a list, Body text, CSV address
	## @return Sends an email
def send_message(user, pw, to, subject, body, doc):
		## Buid message piece by piece
	msg = MIMEMultipart()
	msg['From'] = user
	msg['To'] = ', '.join(to)
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'plain')) ## plain body text

		## One .csv Attachment
	match = re.search(r'[^\\]*\.[a-z]{3}$', str(doc))
	doc_name = doc[match.start():match.end()]
	f = open(doc, 'rb')

	att = MIMEBase('application', 'csv')
	att.set_payload(f.read())
	f.close()
	encoders.encode_base64(att)
	att.add_header('Content-Disposition', 'attachment', filename=doc_name)
	msg.attach(att)


	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls() ## Upgrade to secure connection
		server.login(user, pw)
		server.sendmail(user,to, msg.as_string()) ## to needs to be a list
		server.close()

		print 'Email sent!'
	except:
		print 'Something went wrong...'


send_message(gmail_user, gmail_password, to, subject, body, doc)









