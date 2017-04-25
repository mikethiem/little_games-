# Runs a server for executing code from an ssl (soon) socket
import socket
import threading

class Server:

    def __init__(self, ip="0.0.0.0", port=69331):

        self.socket = socket.socket()
        self.ip = ip
        self.port = port
        self.clients = []

    def serve_forever(self):

        # Bind socket to (ip, port)
        self.socket.bind((ip, port))

        # Listen for connections from client
        self.socket.listen(1)

        # Accept all incoming connections
        while True:

            client_socket, address = self.socket.accept()

            client = Client(client_socket, address)
            self.clients.append(client)
            client.run()


class Client(threading.Thread):

    def __init__(self, client_socket, address):

        super().__init__()

        self.client_socket, self.address = client_socket, address


    def run(self):

        while True:

            # Receive messages
