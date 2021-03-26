"""
	|Python File Sender|

programa simple para enviar archivos
"""
import socket
import sys

def banner():
	return "  ___      ___      ___ _ \n | _ \_  _/ __| ___| __(_)\n |  _/ || \__ \/ -_) _|| |\n |_|  \_, |___/\___|_| |_|\n      |__/                "

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
	print(banner()+'\n\t\tby developmentMen')

	s = socket.socket()

	s.bind((sys.argv[1], 6333))
	s.listen(3)
	print("servidor esperando --> {}".format(sys.argv[1]))
	con = conectar(s) 
	recibir(con)
	
	cerrar(con, s)


if __name__=='__main__':
	try:
	 	main()
	except Exception as e:
	 	print ("uso: \t PySeFi_Server [ip-server]")