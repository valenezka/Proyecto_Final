
import socket
import comparacion_puntajes
# Crear socket
socketAbierto = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

equipo = "localhost"
# Puerto de escucha del servidor
puerto = 8080
socketAbierto.bind((equipo, puerto))
puntajes=[]
print("Escuchando en el puerto: ", puerto)
while True:
    # A la espera de una conexión de un cliente
    connection,address = socketAbierto.recvfrom(1024)
    print("Cliente ", address[0],address[1], " conectado")
    puntajes.append(connection.decode())
    print(connection.decode())
    
   
    if len(puntajes)==2:
        break
#Cerrar el socket
socketAbierto.close()
comparacion_puntajes.comparacion_puntajes(puntajes)


        
           

        