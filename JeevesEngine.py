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


#Functions for Jeeves Engine
#Use function(variables) to call them respectively
#JeevesEngine version 1.3


#Global Variables if sysNotify is enabled

httpDoNotify = 0
http_Check = 0
httpsDoNotify = 0
https_Check = 0
dnsDoNotify = 0
dns_Check = 0
imapDoNotify = 0
imap_Check = 0
imapSSLDoNotify = 0
imapSSL_Check = 0
popDoNotify = 0
pop_Check = 0
popSSLDoNotify = 0
popSSL_Check = 0
sshDoNotify = 0
ssh_Check = 0
smtpDoNotify = 0
smtp_Check = 0
ftpDoNotify = 0
ftp_Check = 0
ftpFileDoNofiy = 0
ftpFile_Check = 0
ADDoNotify = 0
Ad_Check = 0


#HTTP Checker
def httpCheck(url):
	import urllib2, urllib
	
	try:
		#Timeout set to 25 seconds
		urllib2.urlopen(url,'index.html',25)
		result1 = 1
	except:
		result1 = 0
	try:
		urllib.urlopen(url)
		result2 = 1
	except:	
		result2 = 0 
	if result1 == 1 or result2 == 1:
		print "HTTP OK \n"
		httpDoNotify = 0
	else:

		print "HTTP FAIL \n"
		httpDoNotify = 1
	return httpDoNotify

#FTP File Retrieve Checker
def ftpFileCheck(address, username, password, getFile):
	from ftplib import FTP
	import sys
	try:
		
		ftp = FTP(address)
		ftp.login(username,password)

		status = ftp.retrbinary('RETR '+ getFile, sys.stdout.write)
		ftp.quit()

		if status == '226 File send OK.':
			print "FTP OK \n"
			ftpFileDoNotify = 0
		else:
			print "FTP FAIL \n"
			ftpFileDoNotify = 1
	except:
		print "FTP FAIL \n"
		ftpFileDoNotify = 1
	return ftpFileDoNotify

#FTP Check
def ftpCheck(address, username, password):
	from ftplib import FTP
	import sys
	try:
		
		ftp = FTP(address)
		ftp.login(username,password)
		print "FTP OK \n"
		ftpDoNotify = 0
	except:
		print "FTP FAIL \n"
		ftpDoNotify = 1
	return ftpDoNotify


#HTTPS Check
def httpsCheck(url):
	import urllib2, urllib
	
	try:
		#Timeout set to 25 seconds
		urllib2.urlopen(url,'index.html',25)
		result1 = 1
	except:
		result1 = 0
	try:
		urllib.urlopen(url)
		result2 = 1
	except:	
		result2 = 0 
	if result1 == 1 or result2 == 1:
		print "HTTPS OK \n"
		httpsDoNotify = 0
	else:
		print "HTTPS FAIL \n"
		httpsDoNotify = 1
	return httpsDoNotify


#DNS Checker
#Note: dnsCheck will only validate from servers established as the hosts nameservers
#at this point in time there is no support to specify a single server unless
#it is set that way in the dns config.
def dnsCheck(url):

	import dns.resolver, time

	try:
	
		answer = dns.resolver.query(url, 'A')
		print "DNS OK \n"
		dnsDoNotify = 0
	except:
		print "DNS FAIL \n"
		dnsDoNotify = 1
	return dnsDoNotify

#SMTP Checker
def smtpCheck(address, user, password, port):
	import smtplib
	
	try:
		smtpServ = smtplib.SMTP(address, port)
		smtpServ.ehlo()
		smtpServ.starttls()
		smtpServ.ehlo
		smtpServ.login(user,password)
		smtpServ.sendmail(user,user,'test')
		smtpServ.close()
		print "SMTP OK \n"
		smtpDoNotify = 0
	except:
		print "SMTP FAIL \n"
		smtpDoNotify = 1
	return smtpDoNotify
	
#SSH Check
def sshCheck(address, userN, passW):

	import ssh
	try:
		s = ssh.Connection(address,username = userN, password = passW)
		print "connected"
		s.execute('ls')
		s.close()
		print "SSH OK \n"
		sshDoNotify = 0
	except:	
		print "SSH FAIL \n"
		sshDoNotify = 1
	return sshDoNotify

#IMAP /w SSL Checker
def imapCheck_SSL(address, username, password):

	import imaplib
	try:
		con = imaplib.IMAP4_SSL(address, 993)
		con.login(username,password)
		con.logout()
		print "IMAP /W SSL OK \n"
		imapSSLDoNotify = 0
	except:
		print "IMAP /W SSL FAIL \n"
		imapSSLDoNotify = 1
	return imapSSLDoNotify

#IMAP Checker
def imapCheck(address, username, password):

	import imaplib
	try:
		con = imaplib.IMAP4(address, 143)
		con.login(username,password)
		con.logout()
		print "IMAP OK \n"
		imapDoNotify = 0
	except:
		print "IMAP FAIL \n"
		imapDoNotify = 1
	return imapDoNotify

#POP3 /w SSL Checker
def popCheck_SSL(address, username, password):

	import poplib
	try:
		con = poplib.POP3_SSL(address, 995)
		con.user(username)
		con.pass_(password)
		print "POP /W SSL OK \n"
		popSSLDoNotify = 0
	except:
		print "POP /W SSL FAIL \n"
		popSSLDoNotify = 1
	return popSSLDoNotify

#POP3 Checker
def popCheck(address, username, password):

	import poplib
	try:
		con = poplib.POP3(address, 110)
		con.user(username)
		con.pass_(password)
		print "POP OK \n"
		popDoNotify = 0
	except:
		print "POP FAIL \n"
		popDoNotify = 1
	return popDoNotify

def ADCheck(address, username, password):
	import ldap, sys, ldap.sasl

	try:
		con = ldap.initialize(address)
		con.simple_bind_s(username,password)
		print "AD OK \n"
		ADDoNotify = 0
	except:
		print "Invalid connection settings or LDAP unavailable"
		ADDoNotify = 1
	return ADDoNotify

#System Notification from JeevesNotify 
def sysNotify(address, fromUser, toUser, password, port, service, status, checkType):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	checkType = status
	try:
		smtpServ = smtplib.SMTP(address, port)
		smtpServ.ehlo()
		smtpServ.starttls()
		smtpServ.ehlo
		smtpServ.login(fromUser,password)
		msg = MIMEMultipart() 
		msg['Subject'] = service +' Down'
		msg['From'] = 'Jeeves Notification'
		msg['To'] = toUser
		smtpServ.sendmail(fromUser,toUser,msg.as_string())
		smtpServ.quit()
		print "Notification Sent \n"
	except:
		print "Notification Failed to Send \n"
	return checkType


def httpNotify(url, http_Check):

	#HTTP
	status = httpCheck(url)
	if status != http_Check:
		if status == 0:
			http_Check = 0
		else:
			http_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'HTTP', status,http_Check)
	else:
		http_Check = http_Check

	return http_Check

def httpsNotify(url, https_Check):

	#HTTPS
	status = httpsCheck(url)
	if status != https_Check:
		if status == 0:
			https_Check = 0
		else:
			https_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'HTTPS', status, https_Check)
	else:
		https_Check = https_Check

	return https_Check

def dnsNotify(url, dns_Check):

	#DNS
	status = dnsCheck(url)
	if status != dns_Check:
		if status == 0:
			dns_Check = 0
		else:	
			dns_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'DNS', status, dns_Check)
	else:
		dns_Check = dns_Check

	return dns_Check

def imapNotify(address, username, password, imap_Check):
	#IMAP
	status = imapCheck(address, username, password)
	if status != imap_Check:
		if status == 0:
			imap_Check = 0
		else:
			imap_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'IMAP', status, imap_Check)
	else:
		imap_Check = imap_Check

	return imap_Check

def imapSSLNotify(address, username, password, imapSSL_Check):

	#IMAP /w SSL
	status = imapCheck_SSL(address, username, password)
	if status != imapSSL_Check:
		if status == 0:
			imapSSL_Check = 0
		else:
			imapSSL_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'IMAP /w SSL', status, imapSSL_Check)		
	else:
		imapSSL_Check = imapSSL_Check

	return imapSSL_Check

def popNotify(address, username, password, pop_Check):

	#POP
	status = popCheck(address, username, password)
	if status != pop_Check:
		if status == 0:
			pop_Check = 0
		else:
			pop_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'POP', status, pop_Check)
	else:
		pop_Check = pop_Check

	return pop_Check

def popSSLNotify(address, username, password, popSSL_Check):
	
		#POP /w SSL
	status = popCheck_SSL(address, username, password)
	if status != popSSL_Check:
		if status == 0:
			popSSL_Check = 0
		else:
			popSSL_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'POP /w SSL', status, popSSL_Check)
	else:
		popSSL_Check = popSSL_Check

	return popSSL_Check

def ftpNotify(address, username, password, ftp_Check):

	#FTP
	status = ftpCheck(address, username, password)
	if status != ftp_Check:
		if status == 0:
			ftp_Check = 0
		else:
			ftp_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'FTP', status, ftp_Check)
	else:
		ftp_Check = ftp_Check

	return ftp_Check

def ftpFileNotify(address, username, password, getFile, ftpFile_Check):

	#FTP File Download
	status = ftpFileCheck(address, username, password, getFile)
	if status != ftpFile_Check:
		if status == 0:
			ftpFile_Check = 0
		else:
			ftpFile_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'FTP File Download', status, ftpFile_Check)
	else:
		ftpFile_Check = ftpFile_Check
		
	return ftpFile_Check

def smtpNotify(address, username, password, port, smtp_Check):

	#SMTP 
	status = smtpCheck(address, username, password, port)
	if status != smtp_Check:
		if status == 0:
			smtp_Check = 0
		else:
			smtp_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'SMTP', status, smtp_Check)
	else:
		smtp_Check = smtp_Check

	return smtp_Check

def sshNotify(address, username, password, ssh_Check):

	#SSH
	status = sshCheck(address, username, password)
	if status != ssh_Check:
		if status == 0:
			ssh_Check = 0
		else:
			ssh_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'SSH', status, ssh_Check)
	else:
		ssh_Check = ssh_Check

	return ssh_Check

def ADNotify(address, username, password, AD_Check):
	
	#Active Directory
	status = ADCheck(address,username,password)
	if status != AD_Check:
		if status == 0:
			AD_Check = 0
		else:
			AD_Check = sysNotify(notifyAddress, notifyFrom, notifyTo, notifyFromPassword, notifyPort, 'AD', stuats, AD_Check)

	else:
		AD_Check = AD_Check

	return AD_Check

