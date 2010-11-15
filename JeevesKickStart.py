
def imapCheck_SSL(address, username, password):

	import imaplib, re, os
	try:
		con = imaplib.IMAP4_SSL(address, 993)
		con.login(username,password)
		con.select()
		typ, data = con.search(None, 'FROM', 'fromsendergoeshere')
		for num in data[0].split(":"):
			typ, data = con.fetch(num, '(RFC822)')
			temp =  'Message %s\n%s\n' % (num, data[0][1])
			if str(re.search('Http up', temp)) != 'None':
				print "Executing command"
			#command wil go here for example see below
			#	os.system("/etc/init.d/apache2 start")
				con.store(num, '+FLAGS', '\\Deleted')
			else:
				print "Match not found"
		con.close()
		con.logout()
		print "IMAP /W SSL OK \n"
		imapSSLDoNotify = 0
	except:
		print "IMAP /W SSL FAIL \n"
		imapSSLDoNotify = 1
	return imapSSLDoNotify
import time
while 1:
	time.sleep(5)

	imapCheck_SSL('imapserver', 'account', 'password')
