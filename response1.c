import socket

def webbrowser():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('localhost', 9000))
    cmd = "GET http://127.0.0.1/django/django.txt HTTP/1.0\r\n\r\n".encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    mysock.close()

webbrowser()

------------------------------------------------------------------------------------
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
        default_path = os.path.join(root_path, default_file)
        if os.path.exists(default_path):
            with open(default_path, mode="r", encoding="utf-8") as efp:
                error_data = ""
                for line in efp:
                    line += "\r\n"
                    error_data += line
                return error_data
        else:
            return "Default file not found"

def webserver():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            location = rq[1].split("//", maxsplit=1)[-1]
            location = location.lstrip('/')
            print(location)
            data = get_document(root_path, location)
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    serversocket.close()

webserver()
