#!/usr/bin/python

#Copyright Mike Romano & Brett Au 2010

print """
    Copyright Mike Romano & Brett Au 2010

    The Jeeves Engine is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The Jeeves Engine is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with the Jeeves Engine.  If not, see <http://www.gnu.org/licenses/>.
"""
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
