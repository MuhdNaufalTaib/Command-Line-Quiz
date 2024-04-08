# StudentID:	p2129004
# Name:	Muhammad Naufal Bin Taib
# Class:		DISM/FT/1B/01   
# Assessment:	CA2
# 
# Script name:	CA2-server.py
# 
# Purpose:	user script
# This script works fine with client. 100% Complete
# Usage syntax:	Run with Run ->go to intergrated terminal then python server.py
# Input file:	Specify full path, eg. d:/PSEC/user.py
# 
# Python ver:	Python 3
#
# Reference:	This program is adapted from the following:
#		(a) w3schools.com Python
# 		https://www.w3schools.com/python/
#		accessed 20 Nov 2021
#
#		(b) Computer Science Tutorial Threading 
#		https://www.youtube.com/watch?v=Mp6YMt8MSAU&t=361s
#       accessed 27 Nov 2021
#      
#       (c) Python caeser password
#       https://www.youtube.com/watch?v=JEsUlx0Ps9k
#       accessed 27 Nov 2021
# Known issues: Even when user is done and submitted quiz timer still runs and need to wait for timer to run before continue with next user
# Basic Features 100%
# Advanced Features 20% 
# - Randomize presentation of questions pick randomly from question pool
#Program Design: 
#               1)import modules(string,random,time,threading) 
#               2)Create the functions to- read data,encrypt,decrypt,calculate score
#               3)Start program with user input and check if matches in userid_pswdd.text
#               4)User answer questions
#               5)Results Display-Calculation of score, summary of answers
#               
#
#Remarks for second part: give user docimentation with passwords and uses, no create new admin, password when typing must be hidden
# must run one time then stop...that counts as 1 attempt(you can put under userid_pswd)
# ****************************** User-defined functions ***************************


import socket
import os
import threading
import sys
import tqdm

# Create Socket (TCP) Connection
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket created")
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    soc.bind((host, port))
except:
    print("Bind failed. Error : " + str(sys.exc_info()))
    sys.exit()

print('Waitiing for a Connection..')
soc.listen(5)
users = {}
login = []
all_users = []
user_id = ''
attempts = 5




def get_user(): 
    global login
    login = []
    fn = open('./userid_pswd.txt','r')
    for line in fn:
      line = line.strip()
      line_items = line.split(',')
      login.append(line_items)
    fn.close()

    for i in range(len(login)):
        users[login[i][0]] = [login[i][1], login[i][2], login[i][3]]

def login_success():
    global user_id
    
    for i in range(len(login)):
        if login[i][0] == user_id:
            login[i][3] = str(int(login[i][3]) + 1)

    with open('./userid_pswd.txt','w') as f:
        for i in login:
            f.write(",".join(i))
            f.write("\n")
    



def sendfile(filename,connection):
    buffer_size=1024
    filesize=os.path.getsize(filename)
    connection.send(str(filesize).encode())
    progress=tqdm.tqdm(range(filesize),f'Sending {filename}',unit="B") 
    f=open(filename,'rb')
    data=f.read(buffer_size)
    while data:
        connection.sendall(data)
        progress.update(len(data))
        data=f.read(buffer_size)
    f.close()

# Function : For each client 
def threaded_client(connection):

    global user_id
    # Receive Information
    user_info = connection.recv(4096)
    decoded_user_info = user_info.decode().split(' ')
    user_id = decoded_user_info[0]
    password = decoded_user_info[1]
    
    #password= caesar(password, [string.ascii_lowercase, string.ascii_uppercase, string.digits, symbol]) # Password hash using SHA256
    # REGISTERATION PHASE   
    # If new user,  regiter in users Dictionary  
    
    if user_id not in users or ('p' in user_id):
            connection.send(str.encode('Invalid User'))
            
    else:
    # If already existing user, check if the entered password is correct
            if(users[user_id][0] == password) and int(users[user_id][2]) == 0 :
                connection.send(str.encode('Connection Successful...New User')) # Response Code for Connected Client 
                connection.send(str.encode(users[user_id][1]))
                print('Connected : ',user_id)
                login_success()

    
    

                file = open('./question_pool.txt','r')
                data = file.read()

                connection.send('question_pool.txt'.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                connection.send(data.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                file.close()

                file = open('./quiz_settings.txt', 'r')
                data = file.read()

                connection.send('quiz_settings.txt'.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                connection.send(data.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                file.close()

                file = open('./quiz-results.txt', 'r')
                data = file.read()

                connection.send('quiz-results.txt'.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                connection.send(data.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                file.close()
                
                filename = connection.recv(4096).decode()
                print(f'[RECV] Filename Received')
                file = open(filename, 'w')
                connection.send('Filename Received'.encode())

                data = connection.recv(4096).decode()
                print(f'[RECV] Data Received')
                file.write(data)
                connection.send('File data received'.encode())

                file.close()


            elif (users[user_id][0] == password)  and int(users[user_id][2]) < attempts:
                connection.send(str.encode('Connection Successful...Existing User')) # Response Code for Connected Client 
                connection.send(str.encode(users[user_id][1]))
                print('Connected : ',user_id)
                login_success()

    
                file = open('./question_pool.txt','r')
                data = file.read()

                connection.send('question_pool.txt'.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                connection.send(data.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                file.close()

                file = open('./quiz_settings.txt', 'r')
                data = file.read()

                connection.send('quiz_settings.txt'.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                connection.send(data.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                file.close()

                file = open('./quiz-results.txt', 'r')
                data = file.read()

                connection.send('quiz-results.txt'.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                connection.send(data.encode())
                msg = connection.recv(4096).decode()
                print(f'[Server]: {msg}')

                file.close()

                filename = connection.recv(4096).decode()
                print(f'[RECV] Filename Received')
                file = open(filename, 'w')
                connection.send('Filename Received'.encode())

                data = connection.recv(4096).decode()
                print(f'[RECV] Data Received')
                file.write(data)
                connection.send('File data received'.encode())

                file.close()
                

            elif (users[user_id][0] == password)  and int(users[user_id][2]) >= attempts:
                connection.send(str.encode('Connection Successful...No more attempts'))
            else:
                connection.send(str.encode('Login Failed')) # Response code for login failed
                print('Connection denied : ',user_id)
            while True:
               break
            connection.close()






while True:
    get_user()
    Client, address = soc.accept()
    
    client_handler = threading.Thread(target=threaded_client,args=(Client,))
    client_handler.start()
    ThreadCount += 1
    print('Connection Request: ' + str(ThreadCount))


soc.close()



