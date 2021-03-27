import client , server
 
def main():
    portno =  8000
    id = "client"
    c1 = client.client(portno , id)
    c1.createProxy()
    c1.receive()
    print ("DOEN")
    
if __name__ == '__main__':
    main()