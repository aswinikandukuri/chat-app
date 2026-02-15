import socket
import threading

# ----------------- Client Setup -----------------
HOST = '127.0.0.1'
PORT = 5000  # Same as server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input("Enter your username: ")

# ----------------- Receive Messages -----------------
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "USERNAME":
                client_socket.send(username.encode())
            else:
                print(message)
        except:
            print("Connection closed.")
            client_socket.close()
            break

# ----------------- Send Messages -----------------
def send_messages():
    while True:
        msg = input()
        full_msg = f"{username}: {msg}"
        client_socket.send(full_msg.encode())

# ----------------- Start Threads -----------------
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
