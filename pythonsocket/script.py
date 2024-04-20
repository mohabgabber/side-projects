import socket
import argparse
import threading
parser = argparse.ArgumentParser(
    prog="Python Socket", description="Just A Script With Different Ideas Implemented In The Socket Library")
parser.add_argument("tcpserver")
parser.add_argument("--ip", type=str)
parser.add_argument("--port", type=int)
args = parser.parse_args()


def tcpserver(ip: str, port: int):
    # AF_INET -> IPv4, SOCK_STREAM -> TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))  # takes a tuple
    server.listen(10)  # Handles 10 connections
    print(f"Listening on port {port}")

    while True:
        # accepts incoming connections, returns client socket object, and the ip then port of the client as a pair
        client, address = server.accept()
        print(f"Connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handleclients, args=(client,))


def handleclients(clientobj):
    with clientobj as sock:
        req = sock.recv(1024)
        print(f"[+] Received: {req.decode("utf-8")}")
        sock.send(b"ACK")


def main():
    if args.tcpserver:
        tcpserver(args.ip, args.port)
    else:
        pass


if __name__ == "__main__":
    main()
