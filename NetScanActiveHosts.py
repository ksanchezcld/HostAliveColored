#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from subprocess import Popen, PIPE

class color:
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	RED = '\033[91m'
	ENDC = '\033[0m'
	
print color.BLUE + "\t\t*********************************" + color.ENDC
print color.BLUE + "\t\t***Developed By: @ksanchez_cld***" + color.ENDC
print color.BLUE + "\t\t*(Security + MGP + PS. Auditor)*" + color.ENDC
print color.BLUE + "\t\t**Verificar Host Online/Offline**" + color.ENDC
print color.BLUE + "\t\t*********************************" + color.ENDC

NET = '10.0.0.'

def netscan():
	for x in range(1,255):
		ipadd = str(NET) + str(x)
		print "Escaneando %s" %(ipadd)
		time.sleep(1)
		subprocess = Popen(['ping', '-c 1', ipadd], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout, stderr = subprocess.communicate(input=None)
		if "bytes from" in stdout:
			print color.GREEN + "La direccion %s esta respondiendo..."% ipadd + color.ENDC
		else:
			print color.RED + "No esta respondiento " + ipadd + color.ENDC
netscan()