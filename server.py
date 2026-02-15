import socket
import threading

# ----------------- Server Setup -----------------
HOST = '127.0.0.1'
PORT = 5000  # Port number

server_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server listening on {HOST}:{PORT}")

clients = []
usernames = []

# ----------------- Broadcast Function -----------------
def broadcast(message):
    for client in clients:
        client.send(message.encode())

# ----------------- Handle Each Client -----------------
def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast(message)
        except:
            # Remove client if connection closed
            if client in clients:
                index = clients.index(client)
                left_user = usernames[index]
                clients.remove(client)
                usernames.pop(index)
                client.close()
                broadcast(f"{left_user} has left the chat.")
            break

# ----------------- Accept New Connections -----------------
def receive_connections():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {address}")

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)

        print(f"Username of the client: {username}")
        broadcast(f"{username} has joined the chat!")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Start accepting connections
receive_connections()
