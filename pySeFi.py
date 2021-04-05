#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================
# Author	--> devMen
# Date created	--> 01/04/2021
# Last modified	--> 05/04/2021
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
import argparse

# =============================

def banner():
	return """
  ___      ___      ___ _ 
 | _ \_  _/ __| ___| __(_)
 |  _/ || \__ \/ -_) _|| |
 |_|  \_, |___/\___|_| |_|
      |__/               
===> by ☆ developmentMen☆
 """

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
	s = socket.socket()
	s.connect((args.ipAddress, args.port))
	enviar(s, args.file)

	s.close()


if __name__=='__main__':
	argumentos = argparse.ArgumentParser(
		description="Python file sender")
	g = argumentos.add_mutually_exclusive_group()
	g.add_argument('-nb', '--noBanner', action='store_true',
		help="no print banner")
	argumentos.add_argument(
		'-i', '--ipAddress', type=str, required=True, metavar="",
		help="ip PySeFi Server")
	argumentos.add_argument(
		'-p', '--port', type=int, metavar='',
		default=6333, help='Port 1024 to 65535 -> default=6333')
	argumentos.add_argument(
		'-f', '--file', type=str, required=True, metavar="",
		help="file to send")
	args = argumentos.parse_args()

	if not args.noBanner: print(banner())
	try:
	 	main()
	except Exception as e:
		print('=======ERROR======ERROR=======ERROR=======')
		print(e)
		print('=======ERROR======ERROR=======ERROR=======')
