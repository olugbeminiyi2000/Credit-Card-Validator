There are a few issues with your code:

1.  In your `webserver` function, you're trying to split `rq` which is already a list. This is why you're getting the `'list' object has no attribute 'split'` error. You should be splitting `pieces[0]` to get the request method, URL, and HTTP version, and then split the URL to get the location.

2.  In your `doOthers` and `doWindows` functions, you're not correctly handling the case when the location is not one of the specified directories. You're trying to split the location by `/` and then reconstruct it, but you're not removing the last part of the path.

3.  In your `getOthersDocument` and `getWindowsDocument` functions, you're not correctly handling the case when the file is not found. You're trying to open the default file, but you're not handling the case when the default file is not found.

4.  In your `webbrowser` function, you're not sending the correct HTTP request. You should be sending a `GET` request with the URL and HTTP version.

Here's the corrected code:

```python
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
```

```python
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
                return "404 Not Found\r\n"

    def webserver():
        # create a phone
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
                url = rq[1]
                location = url.lstrip('/')
                print(location)
                data = get_document(root_path, location)
                clientsocket.sendall(f"HTTP/1.0 200 OK\r\n\r\n{data}".encode())
                clientsocket.shutdown(SHUT_WR)

        except KeyboardInterrupt:
            print("\nShutting down...\n")
        except Exception as exc:
            print("Error:\n")
            print(exc)
        serversocket.close()

    webserver()
```

Note: I've also removed the `doOthers` and `doWindows` functions as they were not necessary. The `get_document` function now handles both Windows and non-Windows paths using the `os.path.join` function. I've also added a `404 Not Found` response when the requested file is not found.

























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
------------------------------------------------------------------------
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
                return "404 Not Found\r\n"

    def webserver():
        # create a phone
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
                url = rq[1]
                location = url.lstrip('/')
                print(location)
                data = get_document(root_path, location)
                clientsocket.sendall(f"HTTP/1.0 200 OK\r\n\r\n{data}".encode())
                clientsocket.shutdown(SHUT_WR)

        except KeyboardInterrupt:
            print("\nShutting down...\n")
        except Exception as exc:
            print("Error:\n")
            print(exc)
        serversocket.close()

    webserver()
