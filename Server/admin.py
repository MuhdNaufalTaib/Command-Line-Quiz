
# This program is not 100% complete
# Do take not of some not working stuff
# Only workig is add user but cannot change fail and add question

import string
import csv
import re 


def edit_question():
      out = True
          
      while out == True: 
        
        
        go_back = input('\nGo back to menu options... y/n: ')
        if go_back == 'y':
                 out = False
                 return 1
        elif go_back == 'n':
                 print('')
                 out = True
        else: 
                 print('Invalid input... Plz put y or n')
        
        if go_back.lower() == 'n':
            back = True
              
            while back == True:  
                try: 
                  read_question()
                  print('\na)Edit quiz\nb)Edit topic\nc)Edit question\nd)Edit option (a)\ne)Edit option (b)\nf)Edit option (c)\ng)Edit option (d)\nh)Edit answer\ni)To exit')  
                  edit_choice = str(input('Enter choice: '))
                  question_number = int(input('Enter which question you want to edit or 0 to exit: '))

                  if edit_choice.lower() == 'i' and question_number == 0:
                      back = False

                  elif question_number > len(questions) or question_number == 0 :
                      print('Please input a valid question number')
                  
                  elif edit_choice.lower() == 'a':
                    proceed = True
                    while proceed == True:
                        new_quiz = str(input('Enter quiz: '))
                        if len(new_quiz) == 0:
                            print('Please enter something!')
                        else:
                            proceed = False
                            questions[question_number-1][1] = new_quiz
                            back = False
                  elif edit_choice.lower() == 'b':
                    proceed = True
                    while proceed == True:
                        new_topic = str(input('Enter topic: '))
                        if len(new_topic) == 0:
                            print('Please enter something!')
                        else:
                            proceed = False
                            questions[question_number-1][2] = new_topic
                            back = False
                  elif edit_choice.lower() == 'c':
                       proceed = True
                       while proceed == True:
                         new_question = str(input('Enter new question: '))
                         if len(new_question) == 0:
                            print('Please enter something!')
                         else:
                            proceed = False
                            questions[question_number-1][4] = new_question
                            back = False
                  elif edit_choice.lower() == 'd':
                       proceed = True
                       while proceed == True:
                           option_a = str(input('Enter option (a): '))
                           if len(option_a) == 0:
                             print('Please enter something!')
                           else:
                             proceed = False
                             questions[question_number-1][5] = option_a
                             back = False
                  elif edit_choice.lower() == 'e':
                       proceed = True
                       while proceed == True:
                           option_b = str(input('Enter option (b): '))
                           if len(option_b) == 0:
                             print('Please enter something!')
                           else:
                             proceed = False
                             questions[question_number-1][6] = option_b
                             back = False
                  elif edit_choice.lower() == 'f':
                       proceed = True
                       while proceed == True:
                           option_c = str(input('Enter option (c): '))
                           if len(option_c) == 0:
                             print('Please enter something!')
                           else:
                             proceed = False
                             questions[question_number-1][7] = option_c
                             back = False
                  elif edit_choice.lower() == 'g':
                       proceed = True
                       while proceed == True:
                           option_d = str(input('Enter option (d): '))
                           if len(option_d) == 0:
                             print('Please enter something!')
                           else:
                             proceed = False
                             questions[question_number-1][8] = option_d
                             back = False
                  elif edit_choice.lower() == 'h':
                      new_answer = str(input('Enter new answer: '))
                      back = True
            
                      while back == True:
                        count = 0
                        
                        if new_answer == '0':
                            count = 1

                        elif  new_answer != 'a' and  new_answer != 'b' and  new_answer != 'c' and  new_answer != 'd':
                            count = 2
                
 
                        if count == 1:
                            back = False

                        elif count == 0:
                           questions[question_number-1][9] = new_answer
                           back = False

                        elif count == 2:
                            new_answer = str(input('Please enter the correct answer.... either a,b,c,d or 0 to quit: '))
                  
                  else:
                       print('Please input a valid choice a-g')


                except ValueError:
                    print('Please input a valid question number')

def show_report():
    total_marks = 0
    marks = []
    
    print('\nHere is the report\n')
    if len(results) > 0:
     for i in range(len(results)): 
     
      count = 0
      print(f'\n{results[i][0]} - Score: {results[i][24]}')
      print('Correctly answed question')
      for x in range(5):
        if results[i][4*x + 6] == results[i][4*x + 7]:
          print(f'Question {x + 1}: {results[i][4*x + 6]}  Correct Answer - {results[i][4*x + 7]}')
          count = 2
       
      if count == 0:
           print('No question was answered correctly') 

      print('\nWrongly anwsed question')
      for x in range(5):
       if results[i][4*x + 6] != results[i][4*x + 7]:
          print(f'Question {x + 1}: {results[i][4*x + 6]}  User Answer - {results[i][4*x + 6]} Correct Answer - {results[i][4*(x + 6)]}')
          count = 3
      
      if count == 2:
           print('No question was answered wrongly') 
     
     
      marks.append(int(results[i][len(results[i])-1]))
      total_marks += (int(results[i][len(results[i])-1]))


     print(f'\nAverage score is {round(float(total_marks/len(results)), 1)}')
     print(f'Lowest score is {min(marks)}')
     print(f'Highest score is {max(marks)}')
     print(marks)
    else:
        print('No report so far')

def read_question():
    print(questions)
    if len(questions) == 0:
        print('No questions added yet')
    else:
     for i in range(len(questions)):
        print(f'\n{i + 1} {questions[i][1]} {questions[i][2]} {questions[i][4]} a){questions[i][5]} b){questions[i][6]} c){questions[i][7]} d){questions[i][8]} Correct: {questions[i][9]}')

def add_question():
      out = True
          
      while out == True: 
       
        question_list = []
        go_back = input('\nGo back to menu options... y/n: ')
        if go_back == 'y':
                 out = False
                 return 1
        elif go_back == 'n':
                 print('')
                 out = True
        else: 
                 print('Invalid input... Plz put y or n')
        
        if go_back.lower() == 'n': 
            read_question()
            proceed = True
            while proceed == True:
             quiz = str(input('Enter Quiz : '))
             if len(quiz) == 0:
                 print('Please enter something!')
             else:
                 proceed = False

            proceed = True
            while proceed == True:
             topic = str(input('Enter topic: '))
             if len(topic) == 0:
                 print('Please enter something!')
             else:
                 proceed = False

            proceed = True
            while proceed == True:
             new_question = str(input('Enter a new question to add: '))
             if len(new_question) == 0:
                 print('Please enter something!')
             else:
                 proceed = False

            proceed = True
            while proceed == True:
             choice_a = str(input('Enter the choice (a): '))
             if len(choice_a) == 0:
                 print('Please enter something!')
             else:
                 proceed = False
                  
            proceed = True
            while proceed == True:
             choice_b = str(input('Enter the choice (b): '))
             if len(choice_b) == 0:
                 print('Please enter something!')
             else:
                 proceed = False

            proceed = True
            while proceed == True:
             choice_c = str(input('Enter the choice (c): '))
             if len(choice_c) == 0:
                 print('Please enter something!')
             else:
                 proceed = False

            proceed = True
            while proceed == True:
             choice_d = str(input('Enter the choice (d): '))
             if len(choice_d) == 0:
                 print('Please enter something!')
             else:
                 proceed = False
            correct_answer = str(input('Enter the correct answer.... a,b,c,d or 0 to quit: '))
            
            back = True
            
            while back == True:
                count = 0
                if correct_answer == '0':
                    count = 1
                elif correct_answer != 'a' and correct_answer != 'b' and correct_answer != 'c' and correct_answer != 'd':
                    count = 2
                
 
                if count == 1:
                    back = False
                elif count == 0:
                    #question_list.append(str(len(questions)+1))
                    question_list.append('Sports')
                    question_list.append(quiz)
                    question_list.append(topic)
                    question_list.append('11')
                    question_list.append(new_question)
                    question_list.append(choice_a)
                    question_list.append(choice_b)
                    question_list.append(choice_c)
                    question_list.append(choice_d)
                    question_list.append(correct_answer)
                    questions.append(question_list)
                    back = False

                elif count == 2:
                    correct_answer = str(input('Please enter the correct answer.... either a,b,c,d or 0 to quit: '))
def add_user():
      out = True
      
      while out == True: 
        new_user = []
        
    
        go_back = input('Go back to menu options... y/n: ')
        if go_back == 'y':
                 out = False
                 return 1
        elif go_back == 'n':
                 print('')
                 out = True
        else: 
                 print('Invalid input... Plz put y or n')
        
        
        if go_back.lower() == 'n': 
            a = 0
            b = 0
            c = 0
            check = True
            user = str(input("Enter the username to add...for  Users is uXXXX where X is numbers: "))
            password = str(input("Enter the password for this username: "))
            name = str(input("Enter the name: "))
            for i in range(len(login)):
              if user == login[i][0]:
                  a = 1

            for x in user[1:]:
                if not (x.isdigit()):
                    check = False
                    
                    #c = 1
            # require at least one upper case letter,require at least one lower case letter,require at least one number,require at least one symbol,make sure that only these characters and symbols appear in the string
            #make sure the string is at least 4 letters and max 20 letters
            RegexPattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%])[A-Za-z\d@$!#%*?&]{4,20}$'
            result= re.search(RegexPattern,password)
            if result and  'u' in user[0] and len(user) == 5 and check != False and a != 1 and name != '':
                  encrypt = caesar(password, [string.ascii_lowercase, string.ascii_uppercase, string.digits, symbol])
                  new_user.append(user)
                  new_user.append(encrypt)
                  new_user.append(name)
                  new_user.append('0')
                  login.append(new_user)
                  print(f'Name: {name} User: {user} Password: {password} successfully added\n')
            else:
                print('Failed to register user')
                print('Please follow the rules:\n1)Password must be 4 to 20 characters long\n2)Password must have at least 1 lower & upper case\n3)Password must have at least 1 digit\n4)Password must inlclude at least 1 {symbol}')

         

def user_find():
    
    
    for i in range(len(login)):
        login[i][1] = decrypt(login[i][1], [string.ascii_lowercase, string.ascii_uppercase, string.digits, symbol])
    
    print(login)
    
    for i in range(len(login)):

        login[i][1] = caesar(login[i][1], [string.ascii_lowercase, string.ascii_uppercase, string.digits, symbol])

def decrypt(text, alphabets):
    
    def shift_alphabet(alphabet):
        return alphabet[-3:] + alphabet[:-3]



    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

def caesar(text, alphabets):
    
    def shift_alphabet(alphabet):
        return alphabet[3:] + alphabet[:3]



    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

#get user from text file
def get_user():
    fn = open('./userid_pswd.txt','r')
    for line in fn:
      line = line.strip()
      line_items = line.split(',')
      login.append(line_items)
    fn.close()

#get question from text file
def get_question():
    fn = open('./question_pool.txt','r')
    for line in fn:
      line = line.strip()
      line_items = line.split(',')
      questions.append(line_items)
    fn.close()

#get results from text file
def get_results():
    fn = open('./quiz-results.txt','r')
    for line in fn:
      line = line.strip()
      line_items = line.split(',')
      results.append(line_items)
    fn.close()
     
#get settings from text file
def get_settings():
    fn = open('./quiz_settings.txt','r')
    for line in fn:
      line = line.strip()
      line_items = line.split(',')
      settings.append(line_items)
    fn.close()

#defining variables
settings = []
results = []
questions = []
login = []   
symbol = '!@#$%'
x = False
out = True
x = 0

#calls all the functions to put the items from text fill into list
get_user()
get_question()
get_results()
get_settings()

while out == True: 
        print('*** Welcome to Quiz Application for admins ***\n')
        count = 0
        counts = 0
        user = input('Please enter username: ')
        password = input('Please enter password: ')
        encrypt_password =caesar(password, [string.ascii_lowercase, string.ascii_uppercase, string.digits, symbol])
        for i in range(len(login)):
            if user == login[i][0] and encrypt_password == login[i][1] and 'p' in user:


                count = 1
                out = False
                x = True
                break
            elif user == login[i][0] and encrypt_password == login[i][1]:
                counts = 2
                
            else:
                count = 3
                
        if count == 1:
            print('')
        elif counts == 2:
            print('You have just entered a user account ... This is a warning, any more attempts may lead to severe consequences\n')
        elif count == 3:
            print('Invalid username or password\n')

#choose questions based on option...follow instructions               
        while x == True:
            print('\n*** Welcome Admin ***\n')
            print('1)Register User\n2)Setup the pool of questions\n3)Change settings of quiz\n4)Generate Report\n5)Exit')
            choice = str(input('Enter a choice: '))
            if choice == '1':
            
             user_find()
             add_user()
            elif choice == '2':
                #read_question()
                out = True
                while out == True:

                 print('\n1)Add question\n2)Edit Question\n3)Back to main')
                 choice_question = str(input('Enter a choice: '))
                 if choice_question == '1':
                      add_question()
                      out = False
                 elif choice_question == '2':
                      edit_question()
                      out = False
            
                 elif choice_question == '3':
                      out = False
                 else:
                    print('Please enter 1-4 only')

                
            elif choice == '3':
                out = True
                while out == True:

                 print('\n1)Edit number of attempts\n2)Back to main')
                 choice_question = str(input('Enter a choice: '))
                 if choice_question == '1':
                      out = False
                 elif choice_question == '2':
                
                      out = False
                 else:
                    print('Please enter 1-3 only')
            elif choice == '4':
                show_report()
            elif choice == '5':
                print('Ok goodbye!!!')
                x = False
            else:
                print('Invalid input...Please put 1-5 only')