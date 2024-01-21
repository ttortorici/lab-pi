import socket


def send(message, port, host="rogerspi.local"):
    if message:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # connect to server
            s.connect((host, port))

            # send message to server
            s.send(message.encode())

            # get response from the server
            msg_back = s.recv(1024)
        # print(msg_back)
        return msg_back.decode()
    else:
        return "did not send anything"


def shutdown_command(host, port):
    send("shutdown")
