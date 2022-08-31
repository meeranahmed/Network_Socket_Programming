import  socket
import threading
import json
import encryption 

#predefined key for encryption
key = b'\xdb6\xc7r\xb3#\xbe"\x9c~C\xd4\xbe\xb8\x8f\xfa\xb6\x01\xe92+U\xde\\\xd7\xc5m\xba\xe2\r\xda\xe9'

HEADER = 64
PORT = 1023
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNCET"
IDLE_MESSAGE = 'IDLE'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

with open('database.json') as json_file:
    try:
        data = json.load(json_file)
    except:
        data = {}


# a function that is executed in a separate thread for each client. 
# it assigns a list for each unique client that contains the answers of the clients,
# responds with a status message to the client socket, when recieving a DISCONNECT_MESSAGE, it closes the connection.
def handle_client(conn, addr):
    print(f"[NEW CONNCETION] {addr} connected")
    connceted = True
    while connceted:
        try:
            conn.settimeout(50.0)
            msg_length = conn.recv(HEADER).decode(FORMAT)
            conn.settimeout(None)
            
            if msg_length:
                msg_length = int(msg_length)
                # Recieve client's msg encrypted
                msg = conn.recv(msg_length)
                # Decrypt and decode client's msg 
                #print(msg)
                msg = encryption.decrypt(key,msg).decode(FORMAT)
                #print("decrypted:"+msg)
                #print(f"[MSG] {addr} : {msg}")
                
                if msg == DISCONNECT_MSG: 
                    print(f"[DISCONNECTED] {addr} has disconnected")
                    connceted = False
                    continue
                
                elif msg[0:9] == 'username:':
                    user = msg[9:].strip()
                    # print("name" +user)
                    # check if username is in database 
                    if user in data:
                        warning_msg = 'Username is already taken ' + data[user]['Depression Score']
                        # print(warning_msg)
                        message = encryption.encrypt(key,warning_msg)
                        message_length = len(message)
                        send_length =  str(message_length).encode(FORMAT)
                        send_length += b' ' * (HEADER - len(send_length))
                        conn.send(send_length)
                        conn.send(message)

                # Handles a new user 
                else:
                    user_data = msg.split(',')
                    data[user_data[0].strip()] = {
                        'Address': addr,
                        'Gender': user_data[1],
                        'Age': user_data[2],
                        'Depression Score': user_data[3]
                    }
                    
                    # save to database
                    with open('database.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                print(f"[{addr}] {msg}")

                #conn.send("msg received".encode(FORMAT))


        except socket.timeout as e:
            print("[TIME OUT] Timed out after 40 seconds")
            #close connection 
            msg = encryption.encrypt(key, DISCONNECT_MSG)
            conn.send(str(len(msg)).encode(FORMAT))
            conn.send(msg)
            print(f"[DISCONNECTED] {addr} has disconnected")
            connected = False

        # except ConnectionResetError:
            # print("[FORCED CLOSED] Connection to the socket was forcedly closed by the client ... ")
            # connected = False
    conn.close()



# starting the server
def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
 
        # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} clients have connected ...")

print ("[STARTING] server is starting...")
start()
