#!/usr/bin/env python
import socket
import sys
import time

# some defaults
username = ""
SERVER = "irc.freenode.net"
PORT = 6667


def usage():
    print "\n\nIRC simple Python client\n"
    print "usage:\n"
    print "./irc_client.py USERNAME CHANNEL\n\n"
    print "where: USERNAME - your username, CHANNEL - channel you'd like to join (eg. channelname or #channelname)"


def channel(channel):
    """
    ensure that channel name starts with #
    """
    if channel.startswith("#") == False:
        return "#" + channel
    return channel


class Client:
    """
    IRC CLient
    """

    def __init__(self, username, channel, server="irc.freenode.net", port=6667):
        self.username = username
        self.server = server
        self.port = port
        self.channel = channel

    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.server, self.port))

    def get_response(self):
        return self.conn.recv(512)

    def send_cmd(self, cmd, message):
        command = "{} {}\r\n".format(cmd, message)
        print ">>> {}".format(command)
        self.conn.send(command)

    def send_message_to_channel(self, message):
        command = "PRIVMSG {}".format(self.channel)
        message = ":" + message
        self.send_cmd(command, message)

    def join_channel(self):
        cmd = "JOIN"
        channel = self.channel
        self.send_cmd(cmd, channel)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        usage()
        exit(0)
    else:
        username = sys.argv[1]
        channel = channel(sys.argv[2])

    cmd = ""
    joined = False

    client = Client(username, channel, SERVER, PORT)
    client.connect()

    while(joined == False):
        resp = client.get_response()
        print resp.strip()

        # time to introduce to the server:
        if "No Ident response" in resp:
            client.send_cmd("NICK", username)
            client.send_cmd(
                "USER", "{} * * :{}".format(username, username))

        # we're accepted, now let's join the channel!
        if ":{} MODE {} :+i".format(username, username) in resp:
            client.join_channel()

        # we've joined, say Hello! to everyone
        if "End of /NAMES list" in resp:
            joined = True

    # main loop
    while(cmd != "exit"):
        cmd = raw_input("[#{}] ".format(channel))
        
        if cmd == "exit":
            client.send_cmd("QUIT", "Good bye!")

        client.send_message_to_channel(cmd)
        resp = client.get_response()
        print resp.strip()
        