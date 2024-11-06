import os
import socket
import sys
from urllib.parse import urlparse

def get_document(root_path, location):
    file_path = os.path.join(root_path, location.lstrip('/'))
    try:
        with open(file_path, mode="r", encoding="utf-8") as fp:
            data = ""
            for line in fp:
                line += "\r\n"
                data += line
            return data
    except FileNotFoundError:
        return None

def webserver():
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
            parsed_url = urlparse(rq[1])
            location = parsed_url.path
            data = get_document(root_path, location)
            if data is None:
                response = "HTTP/1.1 404 Not Found\r\n\r\n"
            else:
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n" + data
            clientsocket.sendall(response.encode())
            clientsocket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    serversocket.close()

if __name__ == "__main__":
    webserver()

-------------------------------------------------------------------------
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

if __name__ == "__main__":
    webbrowser()
