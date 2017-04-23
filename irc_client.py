#!/usr/bin/env python
import socket

USERNAME = "misiopysio"
SERVER = "irc.freenode.net"
PORT = 6667


class Client:

    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((SERVER, PORT))

    def get_response(self):
        return self.conn.recv(512)

    def send_message(self, cmd, message):
        command = "{} {}\r\n".format(cmd, message)
        print ">>> {}".format(command)
        self.conn.send(command)


if __name__ == "__main__":

    client = Client()
    client.connect()

    while(1):
        resp = client.get_response()
        print resp.strip()
        if "No Ident response" in resp:
            client.send_message("NICK", USERNAME)
            client.send_message(
                "USER", "{} * * :{}".format(USERNAME, USERNAME))
