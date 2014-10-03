#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
import sys
import os
from os.path import basename
from urlparse import urlsplit

class color:
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	RED = '\033[91m'
	ENDC = '\033[0m'
	
print color.BLUE + "\t\t*********************************" + color.ENDC
print color.BLUE + "\t\t***Developed By: @ksanchez_cld***" + color.ENDC
print color.BLUE + "\t\t*(Security + MGP + PS. Auditor)*"  + color.ENDC
print color.BLUE + "\t\t*** @ksanchez_cld on twitter ***"  + color.ENDC
print color.BLUE + "\t\t**Verificar Host Online/Offline**" + color.ENDC
print color.BLUE + "\t\t*********************************" + color.ENDC

EXTENSIONS = ['.pcap.gz']

def download_files_from_url(url):
	if not url.lower().startswith('http://') and not url.lower().startswith('https://'):
		url = 'http://%s'%url
	print 'Descargando desde %s...'%url
	urlContent = urllib2.urlopen(url).read()

	fileExt = re.findall('a .*?href="(.*?)"', urlContent)

	for fileExt in fileExt:
		print fileExt
		os.system('wget -q -nc ' + fileExt)
	return 0

if __name__=='__main__':
	args = sys.argv
	if len(args) < 2:
		print "Necesitas digitar la URL a extraer..."
		exit(-1)
	print args[1]
	download_files_from_url(args[1])
	exit(0)