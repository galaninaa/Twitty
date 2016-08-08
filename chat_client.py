# chat_client.py

import sys
import socket
import select
import string

def find_username(data):
    end = string.find(']',data)
    user = data[:end]
    data = data[end+1:]
    return user,data

 
def chat_client():
    #if(len(sys.argv) < 3) :
    #    print 'Usage : python chat_client.py hostname port'
    #    sys.exit()

    host = 'localhost' #sys.argv[1]
    port = 9009 #int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. You can start sending messages'
    ch_name = '[Sender]'
    #input('Enter you chat name:')
    sys.stdout.write(str(ch_name)); sys.stdout.flush()
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #user,data = find_username(data)

                    #user = '[Reciver]'
                    #print user
                    sys.stdout.write(data)
                    sys.stdout.write(data); sys.stdout.flush()
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write(ch_name); sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())