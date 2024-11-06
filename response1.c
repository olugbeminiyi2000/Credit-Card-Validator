"""webbrowser function"""
if __name__ == "__main__":
    import socket

    def webbrowser():
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect(('localhost', 9000))
        cmd = "GET /django/django.txt HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end='')
        mysock.close()

    webbrowser()

------------------------------------------------------------------------------------
"""webserver"""
if __name__ == "__main__":
    import platform
    from socket import *
    import sys
    import os

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
            default_file_path = os.path.join(root_path, default_file)
            try:
                with open(default_file_path, mode="r", encoding="utf-8") as efp:
                    error_data = ""
                    for line in efp:
                        line += "\r\n"
                        error_data += line
                    return error_data
            except FileNotFoundError:
                return "Default file not found"

    def webserver():
        serversocket = socket(AF_INET, SOCK_STREAM)
        print(sys.argv)
        root_path = sys.argv[1]
        try:
            serversocket.bind(("localhost", 9000))
            serversocket.listen(5)
            while (1):
                (clientsocket, address) = serversocket.accept()
                rd = clientsocket.recv(5000).decode()
                pieces = rd.split("\n")
                if len(pieces) > 0:
                    print(pieces[0])
                rq = pieces[0].split()
                location = rq[1]
                print(location)
                data = get_document(root_path, location)
                clientsocket.sendall(data.encode())
                clientsocket.shutdown(SHUT_WR)

        except KeyboardInterrupt:
            print("\nShutting down...\n")
        except Exception as exc:
            print("Error:\n")
            print(exc)
        serversocket.close()

    webserver()
