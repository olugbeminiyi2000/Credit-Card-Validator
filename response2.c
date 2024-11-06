import socket

def webbrowser():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('localhost', 9000))
    cmd = "GET /django/django.txt HTTP/1.1\r\nHost: localhost:9000\r\n\r\n".encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mysock.close()

webbrowser()

---------------------------------------------------------------------------------
import os
import socket
import sys

def get_document(root_path, location):
    search_file = os.path.join(root_path, location)
    try:
        with open(search_file, mode="r", encoding="utf-8") as fp:
            data = ""
            for line in fp:
                line += "\r\n"
                data += line
            return data
    except FileNotFoundError:
        default_file = "python.txt"
        default_data = get_document(root_path, default_file)
        return default_data

def webserver():
    # create a phone
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(sys.argv)
    root_path = sys.argv[1]
    try:
        serversocket.bind(("localhost", 9000))
        serversocket.listen(5)
        while True:
            (clientsocket, address) = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])
            rq = pieces[0].split()
            location = rq[1].lstrip("/")
            print(location)
            data = get_document(root_path, location)
            response = "HTTP/1.1 200 OK\r\n\r\n" + data
            clientsocket.sendall(response.encode())
            clientsocket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    serversocket.close()

webserver()
