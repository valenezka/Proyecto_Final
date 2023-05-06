import socket
import juego
def Cliente_1():
    puntuacion=juego.iniciar_juego()
    # Crear socket
    socketConexion = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    # Servidor de conexión
    servidor = "localhost"
    # El puerto a utilizar (el servidor debe estar escuchando en este puerto)
    puerto = 8080

    msg = str(puntuacion)+".1" + "\r\n"
    socketConexion.sendto(msg.encode(),(servidor,puerto))

    # Cerrar el socket
    socketConexion.close()