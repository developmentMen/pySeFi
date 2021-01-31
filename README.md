![PySeFi](img/pySefiBanner.png)

#### `PySeFi` es una simple aplicacion escrita en python que mediante sockets envia un archivo de **imagen, video, audio, texto o varios archivos en un comprimido** a otra computadora de la misma red mediante la ip y sin *necesidad de conexion a internet*.

# `en sistemas Linux es recomendable primero editar el archivo */etc/hosts* para poder ver la ip sin problema`
![edit hosts file](img/editHosts.png)

## Como se usa?
se inicia el *socket server* desde la computadora que quiere **recibir el archivo**
> python pySeFi_Server.py

![inica el servidor](img/serverWin.png)

desde la computadora encargada de **enviar el archivo**
> python pySeFi_Server [la ip destino] [el archivo]

![servidor windows](img/EnviadoWin.png)

## recomendacion para usuarios **Linux**
editar el archivo /etc/hosts para poder usar *PySeFi* sin necesidad de la ip

### inicia servidor
![serverLin](img/serverLin.png)

en este caso fue probado en maquina virtual por lo que la ip es diferente

### editar /etc/hosts
![editar fichero hosts](img/myFriendTom.png)

### enviando...
![enviando](img/Enviado.png)

### todo salio bien
![final](img/archivoRecibido.png)
