![PySeFi](img/pySefiBanner.png)

(Python File Sender)

#### `PySeFi` es una simple aplicacion escrita en python que mediante sockets envia un archivo de **imagen, video, audio, texto o varios archivos en un comprimido** a otra computadora de la misma red mediante la ip y sin *necesidad de conexion a internet*.

## Como se usa?

### inicia servidor
se inicia el *socket server* desde la computadora que quiere **recibir el archivo**
' python pySeFi_Server.py [ip]'

![inica el servidor](img/serverWin.png)

### enviando...
desde la computadora encargada de **enviar el archivo**
'python pySeFi_Server [la ip destino] [el archivo]'

![servidor windows](img/EnviadoWin.png)

## que formato de puede enviar?
- .jpg
- .png
- .pdf
- .txt
- .md
- .srt
- .zip
- .tar
- .c
- .mp4
- .mkv
- .mp3
- ...

## problemas
- .avi
	(se pierden o daña la imagen tanto en fichero como en comprimido) 

---

## recomendacion para usuarios **Linux**
editar el archivo /etc/hosts para poder usar *PySeFi* sin necesidad de la ip

### inicia servidor
![serverLin](img/serverLin.png)

en este caso fue probado en maquina virtual por lo que la mascara de red ip es diferente

### editar /etc/hosts
![editar fichero hosts](img/myFriendTom.png)

### enviando...
![enviando](img/Enviado.png)

### todo salio bien
![final](img/archivoRecibido.png)
