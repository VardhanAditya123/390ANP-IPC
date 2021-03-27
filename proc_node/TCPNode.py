
from collections import defaultdict
from queue import Queue, Empty
from multiprocessing import Queue as MPQueue
from .msg import Msg
import socketserver  # import socketserver preinstalled module
import http.server
import node


class TCPNode(node.Node):
    
    def __init__(self, id):
        self.mssg = "A"
        super().__init__(id)

    '''
        Turn on (deploy) the node.
    '''
    def start(self):
        super().start()


    '''
        Turn off (undeploy) the node.
    '''
    def stop(self, disconnect = True):
        super().stop()

    '''
        Connect an undeployed node to this one directly through memory.
        If duplex is true, the given node will also be connected to this one.
    '''
    def connectTCP(self, id, host, port):                                       #TODO: add code to connect to a remote TCPNode at host:port.
        self._connectConn(node)
        
    
    def _connectConn(self, node):
        connRec = self._buildConnRec(node)
        self.conns[node.id] = connRec


    
    def _buildConnRec(self, node):
        connRec = dict()
        connRec["line"] = node.inputLine
        connRec["type"] = "TCP"
        connRec["ssocket"] = self.buildServerSocket(5050)
        connRec["csocket"] = self.buildClientSocket(5050)
        return connRec
    
    def buildServerSocket(self , portno):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', portno))
        return s
    
    def startServer(self, s):
        s.listen(5)
        while True:
            (clientsocket, address) = s.accept()
            data = clientsocket.recv(1024)
            print ('client connected')
            print("Msg from client: "+ data)
            self.mssg = data
        clientsocket.close()
    

    def returnMsg(self):
        return self.mssg

   
    def buildClientSocket(self , portno):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s
    
    def startClient(self, s  , portno):
        s.connect(('localhost', portno))
        print ("Yeah! I'm connected :")
        s.close()
    
    '''
        Turn a present connection into a duplex.
    '''
    def duplexify(self, id):                                                    #TODO: All tcp conns are duplexes, so check if id is a tcp node.
        raise NotImplementedError                                               #      If so, ignore the call. else, call super version.
        super().duplexify(id)

    '''
        Disconnect the node from node1 with given id.
        If notify is true, node1 will be instructed to disconnect from this node too.
    '''
    def disconnect(self, id, notify = True):                                    #TODO: If id is a tcp node, disconnect in your own way. else, call super version.
        raise NotImplementedError
        super().disconnect(id, notify = notify)

    '''
        Quickly handle all updates on the inputLine.
        Node msgs are relocated to the msgQueue.
    '''
    def update(self):                                                           #TODO: Implement for super version and tcp nodes.
        raise NotImplementedError
        super().update()

    '''
        Send a node msg to the node indexed by id.
        If the id is not connected, raise a ValueError.
    '''
    def send(self, id, msg):                                                    #TODO: Implement for super version and tcp nodes.
       if connRec["type"] == "TCP":
        connRec["line"].put(msg)

    '''
        Gets a node msg.
        If block is true, recv will only return when a msg is found, but will continue to update internally.
        If block is false, recv will finish updating and either return a found msg or raise Empty.
    '''
    def recv(self, block = True):                                               #TODO: Implement for super version and tcp nodes.
        raise NotImplementedError
        super().recv(block = block)






#===============================================================================

# class MyTCPHandler(socketserver.BaseRequestHandler):
#     """
#     The request handler class for our server.

#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """

#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print("{} wrote:".format(self.client_address[0]))
#         print(self.data)
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())
#         # here you can do self.request.sendall(use the os library and display the ls command)

# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999

#     # Create the server, binding to localhost on port 9999
#     with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
#         # Activate the server; this will keep running until you
#         # interrupt the program with Ctrl-C
#         server.serve_forever()
        