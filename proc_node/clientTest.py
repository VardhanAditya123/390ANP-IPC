import client , server
 
def main():
    portno =  61619
    id = "client"
    host = "data.cs.purdue.edu"
    c1 = client.client(portno , id , host)
    c1.sendMsg("Finished stage 1")
    c1.receive()
    
if __name__ == '__main__':
    main()