#!/usr/bin/python
# This is a simple port-forward / proxy, written using only the default python
# library. If you want to make a suggestion or fix something you can contact-me
# at voorloop_at_gmail.com
# Distributed over IDC(I Don't Care) license
import socket
import select
import time
import sys

def proxy_tuple(proxystring):
    pretuple = proxystring.split(":")
    return ( pretuple[0], int(pretuple[1]) )

def proxy_dict(proxystring):
    predict = proxystring.split(":")

    result = { "host": predict[0], "port": int( predict[1] ) }
    return result

class ProxyServer:
    class Forward:
        def __init__(self):
            self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def start(self, forwardaddress):
            try:
                self.forward.connect( ( forwardaddress['host'], forwardaddress['port'] ) )
                return self.forward
            except Exception as e:
                print(e)
                return False


    def __init__(self, upstream, localaddress):
        self.input_list = []
        self.channel = {}

        self.upstream = proxy_dict(upstream)
        self.localaddress = proxy_dict(localaddress)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind( ( self.localaddress['host'], self.localaddress['port'] ) )
        self.server.listen(200)

    def main_loop(self):
        # Changing the buffer_size and delay, you can improve the speed and bandwidth.
        # But when buffer get to high or delay go too down, you can broke things
        delay = 0.0001
        buffer_size = 4096

        self.input_list.append(self.server)
        while 1:
            time.sleep(delay)
            ss = select.select
            try:
                inputready, outputready, exceptready = ss(self.input_list, [], [])
            except Exception as e:
                print("[EE] {}".format(e))
                self.server.close()
                return

            for self.s in inputready:
                if self.s == self.server:
                    self.on_accept()
                    break

                try:
                    self.data = self.s.recv(buffer_size)
                except Exception as e:
                    print("[EE] {}".format(e))
                    self.server.close()
                    return

                if len(self.data) == 0:
                    self.on_close()
                    return
                else:
                    self.on_recv()

    def on_accept(self):

        forward = ProxyServer.Forward().start( self.upstream )

        clientsock, clientaddr = self.server.accept()

        forward_to = ( self.upstream['host'], self.upstream['port'] )

        if forward:
            print("[II] [{}:{}] connected".format(clientaddr[0], clientaddr[1]) )
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock
        else:
            print("[EE] [{}:{}] Can't establish connection".format(self.upstream['host'], self.upstream['port']))
            print("[EE] [{}:{}] Closing listener.", clientaddr[0], clientaddr[1])
            clientsock.close()

    def on_close(self):
        print("[WW] [{}:{}] disconnected".format(self.s.getpeername()[0], self.s.getpeername()[1]))
        #remove objects from input_list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        # close the connection with client
        self.channel[out].close()  # equivalent to do self.s.close()
        # close the connection with remote server
        self.channel[self.s].close()
        # delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]
        self.server.close()

    def on_recv(self):
        data = self.data
        # here we can parse and/or modify the data before send forward
        # print(data)
        self.channel[self.s].send(data)