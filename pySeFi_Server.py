"""
	|Python File Sender|

programa simple para enviar archivos
"""
import socket

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

	s.bind((socket.gethostname(), 6333))
	s.listen(3)
	print("servidor esperando --> {}".format(socket.gethostbyname(socket.gethostname())))
	con = conectar(s) 
	#try:
	recibir(con)
	#except :
		#pass
	
	cerrar(con, s)

def banner():
	ban="  ___      ___      ___ _ \n | _ \_  _/ __| ___| __(_)\n |  _/ || \__ \/ -_) _|| |\n |_|  \_, |___/\___|_| |_|\n      |__/                "
	return ban

if __name__=='__main__':
	main()