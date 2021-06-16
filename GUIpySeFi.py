#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================

#cols	_|_______0______|_______1_______|_______2_______|_______3_______|
#rows	0|  by DevMen	|      banner	      banner	|      Exit	|
#	1|	<--		      send			-->	|
#	2|  ip Address	|      port	|     file	|  SEND Button	|
#	3|   Entry ip 	|   Entry Port	|  Entry file	|  SEND Button	|
#	4|	<--		     Recive			-->	|
#	5|     Port	|	 path to recive		| REVICE Button	|
#	6|  Entry port	|	   Entry path		| REVICE Button	|
#	7|_____<--__________________Outputs_____________________-->_____|
# =============================
# Imports
import socket
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
# ============================


class GUIpySeFi(Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.pySefiGUI()

	def pySefiGUI(self):
# ============================
# Row 0
		self.l1 = Label(self, text="☆ |PySeFy|☆ ",
		font="Times 33 italic", bg="black", fg="white", height=3,
		width=20, cursor="star").grid(
                column=0, row=0,columnspan=4 ,sticky="nwe",
		padx=15)
		self.l2 = Label(self,
                text='________by________\n|DevelopmentMen|',
                font=", 7", bg="black", fg="grey", cursor="star").grid(
                column=0, row=0, sticky="nw",padx=15)
		self.b1 = Button(self, text='Exit' ,command=exit,
		width=7, bg="black", fg="white",cursor="X_cursor").grid(
		column=3,row=0, sticky='ne',padx=14)
# ============================
# Row 1
		self.sendLabel = Label(self, text="- S e n d -",
		bg='black',fg='yellow'
		).grid(column=0,row=1,columnspan=4,sticky="ew")

# ============================
# Row 2
		self.l4 = Label(self, text="Ip address").grid(
		column=0, row=2,sticky="e")
		self.l5 = Label(self, text="Port",width=10).grid(
		column=1, row=2,sticky='w')
		self.l6 = Label(self, text="File", width=15).grid(
		column=2, row=2, sticky="w")
		self.b2 = Button(self, text="Send\nfile",
		command=self.sendBut,height=3, width=10).grid(
		column=3, row=2,rowspan=2,pady=3,padx=3,sticky="ew")
# ============================
# Row 3
		self.ipAdress = Entry(self, width=14,justify="right")
		self.ipAdress.grid(column=0,row=3,sticky="e")
		portlist=[]
		for e in range(1025,65536):portlist.append(e)
		self.ports = ttk.Combobox(self, values=portlist,
		width=6)
		self.ports.current(5308)
		self.ports.grid(column=1, row=3,sticky="w")
		self.file = Button(self, text="file", width=19,
		command=self.filePath)
		self.file.grid(column=2, row=3, sticky="ewns", pady=5)
# ============================
# Row 4
		self.reciveLabel = Label(self, text="- R e c i v e -",
		bg='black', fg='yellow').grid(column=0,row=4,
		columnspan=4,sticky="ew")

# ============================
# Row 5
		self.p = Label(self, text='Port').grid(column=0,
		row=5)
		self.pathRec = Label(self, text="Save in folder",
		).grid(column=1, row=5, columnspan=2)
		self.b3 = Button(self, text="UP\nPySeFi\nServer",
		width=10,command=self.reciveBut).grid(column=3,
		row=5,rowspan=2,pady=3,padx=3,sticky="ew")

# ============================
# Row 6
		self.ports2 = ttk.Combobox(self, values=portlist,width=6)
		self.ports2.grid(column=0, row=6)
		self.ports2.current(5308)
		self.savePath = Button(self, text="browse folder",
		width=19,command=self.pathBro)
		self.savePath.grid(column=1, row=6, sticky="ewns",
		pady=5, columnspan=2)

# ============================
# Row 7
		self.output = Label(self, text="Output here",
		bg='black', fg='white', font="Terminal 12 roman",
		width=70)
		self.output.grid(column=0,row=7,
		columnspan=4, sticky="ew")

	def filePath(self):
                f = filedialog.askopenfilename()
                self.file["text"] = f
#                self.outs(f)
	def pathBro(self):
		p = filedialog.askdirectory()
		self.savePath["text"] = p
#		self.outs(p)
	def sendBut(self):
		s = socket.socket()
		var = self.ipAdress.get()
		s.connect((var, int(self.ports.get())))
		s.send(self.file["text"].split("/")[-1].encode())
		time.sleep(1)
		with open(self.file["text"], 'rb') as f:
			while True:
				str = f.readline(512)
				if not str:
					break
				s.send(str)
		self.output["text"] = "Archivo enviado o fin de func"
#self.file["text"].encode()
		s.close()
	def reciveBut(self):
		#s = socket.socket()
		#s.bind((args.ipAd))
		comText = self.ports2.get()+self.savePath["text"]
		self.output["text"] = comText

#if __name__=='__name__':
r = Tk()
r.wm_title("PySeFi")
app = GUIpySeFi(r)
app.mainloop()
