import urllib

def fileMake():
	file = open('score', 'w')
	file.write('0')

def httpCheck(url):
	urllib.urlretrieve (url, 'trueIndex.html')

def httpsInit(url):
	urllib.urlretrieve (url, 'httpsTrueIndex.html')
