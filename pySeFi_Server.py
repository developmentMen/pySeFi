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
import argparse
# =============================
'''
this work in linux

from subprocess import check_output
ips = check_output(['hostname', '--all-ip-addresses'])
print(ips.decode())

'''
def banner():
	return """
  ___      ___      ___ _ 
 | _ \_  _/ __| ___| __(_)
 |  _/ || \__ \/ -_) _|| |
 |_|  \_, |___/\___|_| |_|
      |__/                
===> by ☆ developmentMen☆
"""

def conectar(s):
	con, addr = s.accept()
	print(addr, "se conecto")

	return con

def recibir(con):
	datos = con.recv(1024)
	filename = datos.decode()

	file = open(filename, 'wb')
	while True:
		fileData = con.recv(512)
		if not fileData:
			break
		file.write(fileData)
	file.close()
	print('archivo recibido -> {}'.format(filename))

def cerrar(con, s):
	con.close()
	s.close()

def main():
	s = socket.socket()

	s.bind((args.ipAddress, args.port))
	s.listen(3)
	print("servidor esperando --> {}".format(args.ipAddress))
	con = conectar(s)
	recibir(con)

	cerrar(con, s)


if __name__=='__main__':
	argument = argparse.ArgumentParser(
		description="PySefi server to recive a file")
	g = argument.add_mutually_exclusive_group()
	g.add_argument('-nb', '--noBanner', action='store_true',
		help="no print banner")
	argument.add_argument(
		'-i', '--ipAddress', type=str, required=True,
		metavar="", help="ip to up a server")
	argument.add_argument(
		'-p', '--port', type=int, metavar='',default=6333,
		help="Port 1024 to 65535 -> default=6333")
	args = argument.parse_args()

	if not args.noBanner: print(banner())
	try:
	 	main()
	except Exception as e:
		print('=======ERROR======ERROR=======ERROR=======')
		print(e)
		print('=======ERROR======ERROR=======ERROR=======')

