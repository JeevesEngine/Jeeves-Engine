#!/usr/bin/python


print """
The Jeeves Engine is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The Jeeves Engine is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

#Functions for Jeeves Engine
#Use function(variables) to call them respectively
#JeevesScoringEngine v1.2

#HTTP Checker
def httpCheck(url):
	import urllib, filecmp

	file = open('score', 'r')
	score = file.read()
	score = int(score)
	file = open('score', 'w')
	urllib.urlretrieve (url, 'index.html')
	isTrueFile = filecmp.cmp('index.html', 'trueIndex.html')
	if isTrueFile is True:
		score += 100
		file.write(str(score))
		print "HTTP OK <br />"
	else:
		file.write(str(score))
		print "HTTP FAIL <br />"


#FTP Checker
def ftpCheck(address, username, password, getFile):
	from ftplib import FTP
	import sys, time
	file = open('score', 'r')
	score = file.read()
	score = int(score)
	file = open('score', 'w')
	try:
		
		ftp = FTP(address)
		ftp.login(username,password)

		status = ftp.retrbinary('RETR '+ getFile, sys.stdout.write)
		ftp.quit()

		if status == '226 File send OK.':
			score += 100
			file.write(str(score))
			print "FTP OK <br />"
			
		else:
			file.write(str(score))
			print "FTP FAIL <br />"
	except:
		file.write(str(score))
		print "FTP FAIL <br />"

#HTTPS Check
def httpsCheck(url):

	import urllib, filecmp, time
	file = open('score', 'r')
	score = file.read()
	score = int(score)
	file = open('score','w')
	urllib.urlretrieve (url, 'httpsIndex.html')
	isTrueFile = filecmp.cmp('httpsIndex.html', 'httpsTrueIndex.html')
	if isTrueFile is True:
		score += 100
		file.write(str(score))
		print "HTTPS OK <br />"

	else:
		file.write(str(score))
		print "HTTPS FAIL <br />"
	

	


#DNS Checker
def dnsCheck(url):

	import dns.resolver, time

	file = open('score', 'r')
	score = file.read()
	score = int(score)
	file = open('score','w')
	try:
	
		answer = dns.resolver.query(url, 'A')
	#	for rdata in answer:
			#print 'Host', rdata
		score += 100
		file.write(str(score))
		print "DNS OK <br />"
	except:
		file.write(str(score))
		print "DNS FAIL <br />"


#SMTP Checker
def smtpCheck(address, user, password, port):
	import smtplib
	
	file = open('score', 'r')
	score = file.read()
	score = int(score)
	file = open('score', 'w')
	try:
		smtpServ = smtplib.SMTP(address, port)
		smtpServ.ehlo()
		smtpServ.starttls()
		smtpServ.ehlo
		smtpServ.login(user,password)
		header = 'To: ' + user+ '<br />' 'From: ' + user +  '<br />' + 'Subject:test'
		smtpServ.sendmail(user,user,'test')
		smtpServ.close()
		score += 100
		file.write(str(score))
		print "SMTP OK <br />"
	except:
		file.write(str(score))
		print "SMTP FAIL <br />"

#SSH Check
def sshCheck(address, userN, passW):

	import ssh
	file = open('score','r')
	score = file.read()
	score = int(score)
	file = open('score','w')
	try:
		s = ssh.Connection('host',username = userN, password = passW)
		s.execute('ls')
		s.close()
		file.write(str(score))
		print "SSH OK <br />"
	except:	
		file.write(str(score))
		print "SSH FAIL <br />"


#!/usr/bin/python

#IMAP /w SSL Checker
def imapCheck_SSL(address, username, password):

	import imaplib
	file = open('score','r')
	score = file.read()
	score = int(score)
	file = open ('score', 'w')
	try:
		con = imaplib.IMAP4_SSL(address, 993)
		con.login(username,password)
		con.logout()
		score += 100
		file.write(str(score))
		print "IMAP /W SSL OK <br />"
	except:
		file.write(str(score))
		print "IMAP /W SSL FAIL <br />"


#IMAP Checker
def imapCheck(address, username, password):

	import imaplib
	file = open('score','r')
	score = file.read()
	score = int(score)
	file = open ('score', 'w')
	try:
		con = imaplib.IMAP4(address, 143)
		con.login(username,password)
		con.logout()
		score +=100
		file.write(str(score))
		print "IMAP OK <br />"
	except:
		file.write(str(score))
		print "IMAP FAIL <br />"

#!/usr/bin/python

#POP3 /w SSL Checker
def popCheck_SSL(address, username, password):

	import poplib
	file = open('score','r')
	score = file.read()
	score = int(score)
	file = open ('score', 'w')
	try:
		con = poplib.POP3_SSL(address, 995)
		con.user(username)
		con.pass_(password)
		score +=100
		file.write(str(score))
		print "POP /W SSL OK <br />"
	except:
		file.write(str(score))
		print "POP /W SSL FAIL <br />"


#POP3 Checker
def popCheck(address, username, password):

	import poplib
	file = open('score','r')
	score = file.read()
	score = int(score)
	file = open ('score', 'w')
	try:
		con = poplib.POP3(address, 110)
		con.user(username)
		con.pass_(password)
		score +=100
		file.write(str(score))
	except:
		file.write(str(score))
		print "POP FAIL <br />"


