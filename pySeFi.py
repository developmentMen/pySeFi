#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================
# Author	--> devMen
# Date created	--> 01/04/2021
# Last modified	--> 01/04/2021
# Version	--> Python 3.8.5
# =============================
"""
	|Python File Sender|
programa simple para enviar archivos
"""
# =============================
# Imports
import socket
import sys
import time
# =============================

def banner():
	return "  ___      ___      ___ _ \n | _ \_  _/ __| ___| __(_)\n |  _/ || \__ \/ -_) _|| |\n |_|  \_, |___/\___|_| |_|\n      |__/                "

def enviar(s, filename):
	s.send(filename.encode())
	time.sleep(1)
	file = open(filename, 'rb')
	while True:
		strng = file.readline(512)
		if not strng:
			break
		s.send(strng)
	file.close()
	print("archivo enviado con exito")

def main():
	print(banner()+'\n\t\t\tby developmentMen\n')

	s = socket.socket()
	s.connect((sys.argv[1], 6333))
	enviar(s, sys.argv[2])

	s.close()


if __name__=='__main__':
	try:
	 	main()
	except Exception as e:
	 	print ("uso: \t PySeFi [ip-server] [archivo]")
