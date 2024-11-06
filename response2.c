import os

def getDocument(root_path, location=""):
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
        default_data = getDocument(root_path, default_file)
        return default_data

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
            location = rq[1].split("//", maxsplit=1)[-1]
            print(location)
            data = getDocument(root_path, location)
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)
    serversocket.close()
