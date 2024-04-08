# StudentID:	p2129004
# Name:	Muhammad Naufal Bin Taib
# Class:		DISM/FT/1B/01   
# Assessment:	CA2 
# 
# Script name:	CA2-client.py
# 
# Purpose:	user script
#
# Usage syntax:	Run with Run ->go to intergrated terminal then python client.py
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
# Advanced Features 80% 
# - Randomize presentation of questions pick randomly from question pool
# - Specify attempts for quiz
# - Specify the time allowed for the quiz
# - Export data to CSV file to facilitate analysis of performance
#Program Design: 
#               1)import modules(string,random,time,threading) 
#               2)Create the functions to- read data,encrypt,decrypt,calculate score
#               3)Start program with user input and check if matches in userid_pswdd.text
#               4)User answer questions
#               5)Results Display-Calculation of score, summary of answers
#               6)Repeat
#
#Remarks for second part: give user docimentation with passwords and uses, no create new admin, password when typing must be hidden
# must run one time then stop...that counts as 1 attempt(you can put under userid_pswd)
# ****************************** User-defined functions ***************************


from fileinput import filename
import socket
import sys
import string
from random import sample
import random

#def receive_file(filename, client):

        # print(f'[RECV] Filename Received')
        # file = open(filename, 'w')
        # client.send('Filename Received'.encode())

        # data = client.recv(4096).decode()
        # print(f'[RECV] Data Received')
        # file.write(data)
        # client.send('File data received'.encode())

        # file.close()
        # client.close()
        # print('Finished')

def display_past_results(): #here for new
    with open('./quiz-results.txt','r') as f:
         for line in f:
            line = line.strip()
            line_items = line.split(',')
            past_results.append(line_items)

    print('Here are your past results')
    for i in range(len(past_results)):
        x = 1
        a = 2
        b = 3
        if past_results[i][0] == user_id:
            print(f'\nUser: {past_results[i][0]}')
            print(f'Score: {past_results[i][24]}')
            for f in range(5):
                if past_results[i][a]== past_results[i][b]:
                    print(f'Question {f+1}: {past_results[i][x]}   - Correct')
                    x = x + 3
                    a = a + 3
                    b = b + 3
                else:
                    print(f'Question {f+1}: {past_results[i][x]}   - Wrong')
                    x = x + 3
                    a = a + 3
                    b = b + 3





def get_summary():
    for i in range(len(random_questions)):
        random_questions[i][3] = qn_order[i]

    summary.append(user_id)
    summary.append(random_questions[0][0])
    summary.append(random_questions[0][1])
    summary.append(random_questions[0][2])
    for i in range(len(user_answer)):

        summary.append(str(random_questions[i][3]))
        summary.append(random_questions[i][4])
        summary.append(user_answer[i])
        summary.append(correct[i])

    summary.append(str(score))
    with open('./quiz-results.txt','a') as f:

         
         f.write(",".join(summary))
         f.write("\n")


         #f.write(",".join(summary))
         #f.write("\n")

def get_answer():
    global answer
    answer = []
    for i in range(len(random_questions)):
        answer.append(random_questions[i][9])
    return answer


#calculate_score of the quiz
def calculate_score(answer, correct):
    global score
    marks = 0
    for i in range(len(answer)):
        if answer[i] == correct[i]:
           marks += 1

    overall = marks/5*100
    score = marks*2


    return overall

def display_changed():
    check = True
    while check == True:
        answer = input('<Enter (a) to (d) for answer>\n>>')

        if answer.lower() in options:
                    check = False
                    return answer.lower()
        else:
            print('Error. You are attempting a question\n')

def change_answer(list1, num):
    print(read_question(list1[num-1]))
    changed_answer = display_changed()

    if changed_answer.lower() == 'p':
       user_answer[num-1] = 'NONE'

    elif changed_answer.lower() == 'n':
       user_answer[num-1] = 'NONE'
    else:
       user_answer[num-1] = changed_answer

def submit():
 counter = 0
 x = 0
 results = 1

 while results != 0:
    not_answered = []
    key = True

    while key == True:
      try:
       submit = int(input('Enter 0 to submit your quiz or [1 to 5] to change your answer.\n>> '))
       key = False

       if submit < 0 or submit > 5:
         key = True
         print('Invalid input...Plz enter 0-5')


      except ValueError:
        key = True
        print(f'Invalid input...Plz enter 0-5')


    if submit == 0:
      for i in user_answer:
        if user_answer[i] == 'NONE':
            x += 1
            not_answered.append(i + 1)

      if x > 0:
        print(f'>> Unanswered question(s): {not_answered} ')
      else:
         results = 0

      counter += 1
      if counter > 1:
         results = 0
    elif submit in number:
        change_answer(random_questions, submit)
        print_results()

def print_results():

  print('\nHere are your answers:')
  for i in range(len(user_answer)):
    count = 1

    print(f'Question-{random_questions[i][3]}: {random_questions[i][4]}')
    if user_answer.get(i) == 'a':
        count += 4
    elif user_answer.get(i) == 'b':
        count += 5
    elif user_answer.get(i) == 'c':
        count += 6
    elif user_answer.get(i) == 'd':
        count += 7

    if user_answer[i] == 'NONE': #
        print(f'Answer: NONE\n')
    else:
        print(f'Answer:({user_answer[i]}) {random_questions[i][count]}\n')

def randomize(list):

    for i in range(len(list)):
        if list[i][2] == first_topic:
            topic1.append(list[i])
        elif list[i][2] == second_topic:
            topic2.append(list[i])


    quiz_questions = sample(topic1,t1)
    b = sample(topic2,t2)
    quiz_questions.extend(b)

    #quiz_questions = sample(quiz_questions,5)
    random.shuffle(quiz_questions)

    #x = sample(list,5)
    for i in range(len(quiz_questions)):
        qn_order.append(quiz_questions[i][3] )
        quiz_questions[i][3] = i+1
    print(qn_order)
    return quiz_questions

def answers():
    check = True
    while check == True:
        answer = input('<Enter (a) to (d) for answer, P for previous question, N for next question>\n>>')
        if answer.lower() in options:
                    check = False
                    return answer.lower()
        elif answer.lower() == 'p' or answer.lower() == 'n':
                    check = False
                    return answer.lower()
        else:
            print('Error. You are attempting a question\n')

def read_question(lol):
    return f'\nQuestion {lol[3]}:\n{lol[4]}\na){lol[5]}\nb){lol[6]}\nc){lol[7]}\nd){lol[8]}'

def get_question():
   fn = open('./question_pool.txt','r')
   for line in fn:
      line = line.strip()
      line_items = line.split(',')
      questions.append(line_items)
   fn.close()

def user_find():
    print('\n*** Welcome to Quiz Application ***\n')


def caesar(text, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[3:] + alphabet[:3]



    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

def main():
    global name
    global user_id
    global client
# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # connect the client
    # client.connect((target, port))
    try:
        client.connect(('127.0.0.1', 1233))
    except:
        print("Connection Error")
        sys.exit()
    print('\n*** Welcome to Quiz Application ***\n')
    #response = client.recv(4096)
    # Input UserName
    ole = ''
    while ole != 'out':
        user_id = input('\nPlease enter username: ')
        password = input('Please enter password: ')
        if user_id == '' or password == '':
            print('Please enter something')
        else:

            ole = 'out'


    #client.send(user_id.encode())
    #response = client.recv(4096)
    # Input Password
    #password = input(response.decode())
    password= caesar(password, [string.ascii_lowercase, string.ascii_uppercase, string.digits, symbol])
    user_info = f'{user_id} {password}'
    client.send(str.encode(user_info))
    # Receive response
    response = client.recv(4096)
    response = response.decode()
    print(response)

    if response == 'Connection Successful...New User':
        name = client.recv(4096)
        name = name.decode()

        filename = client.recv(4096).decode()
        print(f'[RECV] Filename Received')
        file = open(filename, 'w')
        client.send('Filename Received'.encode())

        data = client.recv(4096).decode()
        print(f'[RECV] Data Received')
        file.write(data)
        client.send('File data received'.encode())

        file.close()


        filename = client.recv(4096).decode()
        print(f'[RECV] Filename Received')
        file = open(filename, 'w')
        client.send('Filename Received'.encode())

        data = client.recv(4096).decode()
        print(f'[RECV] Data Received')
        file.write(data)
        client.send('File data received'.encode())

        file.close()

        filename = client.recv(4096).decode()
        print(f'[RECV] Filename Received')
        file = open(filename, 'w')
        client.send('Filename Received'.encode())

        data = client.recv(4096).decode()
        print(f'[RECV] Data Received')
        file.write(data)
        client.send('File data received'.encode())

        file.close()

    elif response == 'Connection Successful...Existing User':
        name = client.recv(4096)
        name = name.decode()

        filename = client.recv(4096).decode()
        print(f'[RECV] Filename Received')
        file = open(filename, 'w')
        client.send('Filename Received'.encode())

        data = client.recv(4096).decode()
        print(f'[RECV] Data Received')
        file.write(data)
        client.send('File data received'.encode())

        file.close()


        filename = client.recv(4096).decode()
        print(f'[RECV] Filename Received')
        file = open(filename, 'w')
        client.send('Filename Received'.encode())

        data = client.recv(4096).decode()
        print(f'[RECV] Data Received')
        file.write(data)
        client.send('File data received'.encode())

        file.close()

        filename = client.recv(4096).decode()
        print(f'[RECV] Filename Received')
        file = open(filename, 'w')
        client.send('Filename Received'.encode())

        data = client.recv(4096).decode()
        print(f'[RECV] Data Received')
        file.write(data)
        client.send('File data received'.encode())

        file.close()
        print('Finished')




    return response

symbol = '!@#$%'
name = ''
questions = []

index = 0
user_answer = {}
options = ['a','b','c','d']
i = 0
number = [1,2,3,4,5]
score = 0
user_id = ''
summary = []
past_results = []
count = 0
key = ''
assignment ='Quiz-1'
first_topic = 'Soccer'
second_topic = 'Diet'
topic1 = []
topic2 = []
t1 = 2
t2 = 3
qn_order = []
client = ''


if __name__ == "__main__":
    pi = main()

while pi != 'Connection Successful...New User' and pi != 'Connection Successful...Existing User' and pi != 'Connection Successful...No more attempts' and count < 3:
      #client.close()
      pi = main()
      count += 1


if count >= 3:
    print('Connection Timeout. Too many failed logins')
    sys.exit()

if pi == 'Connection Successful...Existing User':
    still_in = True
    while still_in == True:
        try:
            choice = int(input('\nYou have already attempted the quiz. Please choose an option:\n1)See past results\n2)Start new attempt\n >>>'))
            if choice == 1:
                    display_past_results()
            elif choice == 2:
                key = 'enter'
                still_in = False
            # elif choice == 3:
            #     still_in = False
            #     sys.exit
            else:
                print('Please enter 1,2 or 3 only')
        except Exception:
            print('Please enter 1,2 or 3 only')




elif pi == 'Connection Successful...No more attempts':
     choices = input('\nYou have exceeded number of attempts for the quiz. Do you want to see past results?(yes/no): ')
     if choices.lower() == 'yes':
         display_past_results()
elif pi == 'Connection Successful...New User':
    key = 'enter'




if key == 'enter':
    get_question()
    print(f'Welcome {name}, please choose the best anwsers.Good Luck!')
    random_questions = randomize(questions)

    try:
                    while index < 5:
                        print(read_question(random_questions[index]))
                        register = answers()

                        if register.lower() == 'p':
                            if i  >= 0:
                                user_answer[i] = 'NONE'
                                index -= 1
                                i = i - 1



                        elif register.lower() == 'n':
                            if i  >= 0:
                                user_answer[i] = 'NONE'
                                index += 1
                                i = i + 1

                        else:
                            user_answer[i]=register
                            index += 1
                            i = i + 1



                        if index < 0:
                            index += 1
                            i = i + 1
                            input("Cannot go back this is the first question...PLZ press enter")

    except ValueError:
                        print('Error')


    print_results()
    submit()

    correct = get_answer()
    print(f'\nYour score is {round(calculate_score(user_answer, correct))}%')
    #print(score)

    if calculate_score(user_answer, correct) <= 40:
        print('Poor. You need to work harder.')
    elif calculate_score(user_answer, correct) < 80 :
        print('Fair. You can do better with more effort.')
    else:
        print('Good. Well done.')


    get_summary()


    file = open('./quiz-results.txt','r')
    data = file.read()
    

    client.send('quiz-results.txt'.encode())
    msg = client.recv(4096).decode()
    print(f'[Server]: {msg}')
   
    client.send(data.encode())
    msg = client.recv(4096).decode()
    print(f'[Server]: {msg}')

    file.close()
    #print(summary)
    #print(past_results)



