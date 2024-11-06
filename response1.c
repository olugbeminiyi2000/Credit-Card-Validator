I have developed a basic web server and client browser in Python for local network interactions. The client (webbrowser function) is meant to connect to localhost on port 9000, send an HTTP GET request for a specified file defined in the URL variable, and print the server's response. The server (webserver function) should listen for incoming client requests, process them to determine the requested file, and serve the appropriate text file content from the local directory. Helper functions are used to handle file retrieval and platform-specific path formatting for compatibility with Windows and non-Windows systems. The server should return a default Python file content if a file isn't found and gracefully handle exceptions for shutdown or runtime issues. On running my code, the web browser did not print a response whereas the web server crashed and printed an error message (Error:  'list' object has no attribute 'split').
I want you to debug the below code to figure out why the program does not run as expected and fix the issues:
```python
"""webbrowser function"""
if __name__ == "__main__":
  import socket


  def webbrowser():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('localhost', 9000))
    cmd = "GET http://127.0.0.1/django/django.txt HTTP/1.0".encode()
    mysock.send(cmd)

    while True:
      data = mysock.recv(512)
      if len(data) < 1:
        break
      print(data, end='')
    mysock.close()
webbrowser()
```
```python
"""webserver"""
if __name__ == "__main__":
	import platform
	from socket import *
	import sys
	def doOthers(root_path, location):
		if location == "django/" or location == "django":
			if location.endswith("/"):
				location = f"{location[:len(location)]}/django.txt"
				print(location)
			else:
				location = f"{location}/django.txt"
				print(location)
			data = getOthersDocument(root_path, location)
		elif location == "web/" or location == "web":
			if location.endswith("/"):
				location = f"{location[:len(location)]}/web.txt"
			else:
				location = f"{location}/web.txt"
			data = getOthersDocument(root_path, location)
		elif location == "postgres/" or location == "postgres":
			if location.endswith("/"):
				location = f"{location[:len(location)]}/postgres.txt"
			else:
				location = f"{location}/postgres.txt"
			data = getOthersDocument(root_path, location)
		else:
			if location == "":
				data = getOthersDocument(root_path, location)
			else:
				location_split = location.split("/")
				new_location = ""
				for i in range(len(location_split)):
					if i == len(location_split) - 1:
						continue
					new_location += f"{location_split[i]}/"
				data = getOthersDocument(root_path, location)
		return data
	
	def getOthersDocument(root_path, location="", error=0):
		search_file = f"{root_path}/{location}"
		if error == 1:
			with open(search_file, mode="r", encoding="utf-8") as efp:
				error_data = ""
				for line in efp:
					line += "\r\n"
					error_data += line
				return error_data
		try:
			with open(search_file, mode="r", encoding="utf-8") as fp:
				data = ""
				for line in fp:
					line += "\r\n"
					data += line
				return data
		except FileNotFoundError:
			default_file = "/python.txt"
			default_data = getOthersDocument(root_path, location=default_file, error=1)
			return default_data
		
	def doWindows(root_path, location):
		if location == "django/" or location == "django":
			if location.endswith("/"):
				location = f"{location[:len(location)]}\\django.txt"
				print(location)
			else:
				location = f"{location}\\django.txt"
				print(location)
			data = getWindowsDocument(root_path, location)
		elif location == "web/" or location == "web":
			if location.endswith("/"):
				location = f"{location[:len(location)]}\\web.txt"
			else:
				location = f"{location}\\web.txt"
			data = getWindowsDocument(root_path, location)
		elif location == "postgres/" or location == "postgres":
			if location.endswith("/"):
				location = f"{location[:len(location)]}\\postgres.txt"
			else:
				location = f"{location}\\postgres.txt"
			data = getWindowsDocument(root_path, location)
		else:
			if location == "":
				data = getWindowsDocument(root_path, location)
			else:
				location_split = location.split("/")
				new_location = ""
				for i in range(len(location_split)):
					if i == len(location_split) - 1:
						new_location += f"{location_split[i]}"
						continue
					new_location += f"{location_split[i]}\\"
				data = getWindowsDocument(root_path, location)
		return data
	
	def getWindowsDocument(root_path, location="", error=0):
		search_file = f"{root_path}\\{location}"
		if error == 1:
			with open(search_file, mode="r", encoding="utf-8") as efp:
				error_data = ""
				for line in efp:
					line += "\r\n"
					error_data += line
				return error_data
		try:
			with open(search_file, mode="r", encoding="utf-8") as fp:
				data = ""
				for line in fp:
					line += "\r\n"
					data += line
				return data
		except FileNotFoundError:
			default_file = "\\python.txt"
			default_data = getWindowsDocument(root_path, location=default_file, error=1)
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
				location = rq.split("//", maxsplit=1)[1]
				print(location)
				if platform.system() == "Windows":
					data = doWindows(root_path, location)
				else:
					data = doOthers(root_path, location)
				clientsocket.sendall(data.encode())
				clientsocket.shutdown(SHUT_WR)

		except KeyboardInterrupt:
			print("\nShutting down...\n")
		except Exception as exc:
			print("Error:\n")
			print(exc)
		serversocket.close()
	webserver()
```
