import socket
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1234))
s.listen(5)
url = "http://127.0.0.1:8000/api/v1/cars/location/"
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    data = clientsocket.recv(2048)
    break
data = data.decode()
print(data)
req = requests.patch(url, json={"id": "48bc948c-e5a4-4c14-8e90-84df8dac038c", 
                        "location": "54.324234, 52.5353"})
# print(req.respo)

# req = requests.patch(url, {"id": "48bc948c-e5a4-4c14-8e90-84df8dac038c", 
#                         "location": data})