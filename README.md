Chat Application
This project is a real-time Chat Application developed using Python.
It implements a Client–Server architecture using socket programming, allowing multiple users to connect and communicate simultaneously.

The application demonstrates networking concepts and multi-threaded communication in Python.

🚀 Features

🔗 Client–Server Communication

👥 Multiple Clients Support

💬 Real-Time Messaging

🔄 Message Broadcasting

👤 Username-Based Identification

🚪 Join & Leave Notifications

🧵 Multi-threading for handling multiple users

🛠️ Technologies Used

Python 3

Socket Programming (socket module)

Multi-threading (threading module)

TCP/IP Communication

Command Line Interface

No external libraries required ✅

🏗️ Project Structure
chat_app/
│
├── server.py   # Handles multiple clients and broadcasts messages
├── client.py   # Connects to server and sends/receives messages
└── README.md

⚙️ How It Works

The server starts and listens for incoming client connections.

When a client connects:

The server asks for a username.

The username is stored.

Messages sent by any client are broadcasted to all connected clients.

If a client disconnects, other users are notified.

▶️ How to Run the Project
Step 1: Make Sure Python is Installed
python --version

Step 2: Run the Server First
python server.py


Output:

Server listening on 127.0.0.1:5001

Step 3: Run Client (Open New Terminal)
python client.py


Enter username when prompted.

Step 4: Open Multiple Clients

Run client.py in multiple terminals to simulate multiple users.

💡 Key Concepts Implemented

Client–Server Architecture

TCP Socket Programming

Multi-threading

Real-time Communication

Message Broadcasting

Exception Handling

📚 Knowledge Gained

Through this project, I learned:

Fundamentals of Networking

TCP/IP Communication in Python

Handling multiple clients using threads

Managing concurrent connections

Debugging real-time applications

Version control using Git & GitHub

🔮 Future Enhancements

🖥️ GUI using Tkinter

🔐 User Authentication System

🔒 Message Encryption

📁 File Sharing Support

🌐 Web-based Chat Application

💾 Message History Storage

🎯 Internship Outcome

This project strengthened my understanding of Python networking and real-time communication systems. It reflects practical implementation of socket programming concepts during my Infosys Internship.

👩‍💻 Developed By

Kandukuri Aswini
Infosys Internship – Python Programming
