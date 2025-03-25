# Program Name: program_b.py
# Course: Adv Application Development Section W02
# Student Name: Foster North
# Assignment Number: 4
# Due Date: 03/24/2025
# Purpose: Waits on a port for a string, converts it to caps, and send it back
# List Specific resources used to complete the assignment: https://stackoverflow.com/questions/57717402/send-a-string-between-python-programs and https://www.youtube.com/watch?v=4iIcjDxmRT0&ab_channel=LearnPython 

import socket

def main():
    # Setting up the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binds the socket to port 40001
    server_address = ('localhost', 40001)
    sock.bind(server_address)

    # Listen for the incoming string
    sock.listen(1)

    while True:
        # Waits for a connection
        connection, client_address = sock.accept()

        try:
            print("Connection from", client_address)

            # Receives the string and converts it to caps
            while True:
                data = connection.recv(1024)
                if data:
                    print("Received:", data.decode())
                    # converts the string to caps
                    data = data.decode().upper().encode()
                    # Sends the string back to the client
                    connection.sendall(data)
                else:
                    break

        finally:
            connection.close()

if __name__ == '__main__':
    main()
