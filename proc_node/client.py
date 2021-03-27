import xmlrpc.client
from node import Node

class client(Node):
    
    def __init__(self , port , id):
        super().__init__(id)
        self.portno = port

    
    def createProxy(self):
        self.proxy = xmlrpc.client.ServerProxy("http://localhost:"+str(self.portno)+"/")
    
    def receive(self):
        with open("received_img.jpg", "wb") as handle:
            handle.write((self.proxy.image()).data)  

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
    