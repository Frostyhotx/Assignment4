# Program Name: program_a.py
# Course: Adv Application Development Section W02
# Student Name: Foster North
# Assignment Number: 4
# Due Date: 03/24/2025
# Purpose: Prompts the user for a string and waits for the response to come back capitilized
# List Specific resources used to complete the assignment: https://stackoverflow.com/questions/57717402/send-a-string-between-python-programs and https://www.youtube.com/watch?v=4iIcjDxmRT0&ab_channel=LearnPython 

import socket

def main():
    # sets up the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connects to the port 40001
    server_address = ('localhost', 40001)
    sock.connect(server_address)

    try:
        # prompts the user for a string to enter
        message = input("Enter a string to send: ")
        # Sends the string
        sock.sendall(message.encode())

        # this recieves the message from the 2nd program
        data = sock.recv(1024)
        print("Received: ", data.decode())

    finally:
        sock.close()

if __name__ == '__main__':
    main()
