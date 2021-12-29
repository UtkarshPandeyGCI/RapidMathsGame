import time
import functions

def Welcome_user():
    print("""
                                Rapid Maths Game: Calculation Based Game
                               ``````````````````````````````````````````
                               [ A CLI based game programmed by Utkarsh ]
                               ------------------------------------------

            >> Info about the game
               ~~~~~~~~~~~~~~~~~~~

                           * Every right solution rewards you 1 point.
                           * You have unlimited time to play!
                           * Number of questions displayed is equal to total scores.
                           * Number of attempted questions is equal to obtained points.
                           * If you think answer is in decimals, try to give your answer
                             to two decimal places.

            [::] Note - Type 'done' in 'Your answer here', when you wish to quit the game!
            _____________________________________________________________________________

                                Put Your Best Efforts and Make High Scores!

""")
    #time.sleep(10) #Time provided to read instructions | removed on 29-12-21
    input("Press any key to continue...")
    print('\r')
    
    username = input("Enter your name: ")
    #time.sleep(2) | removed on 29-12-21
    print('\r')
    print("\n\t\tSolve the following questions\n")

    count=0
    while True:
        count+=1
        question = functions.Session.question_module()
        ask_que = f"\nQuestion {count}: What is {question}"
        print(ask_que)
        user_input_answer = input("Your answer here: ")
        #check for quiet
        if user_input_answer == 'done':
            break
        elif user_input_answer == '':
            user_input_answer = '0.0'
        else:
            user_input_answer = float(user_input_answer)
            pass

        #check
        evaluated = eval(question)
        
        #if round(evaluated,2) == round(user_input_answer,2): || REMOVED on December 29, 2021 || Reason: Bug fixed for 3.3333333 != 3.33 as per rule to provide points
            #print(type(evaluated),type(user_input_answer))
            #print(evaluated,user_input_answer)
        
        if evaluated == user_input_answer:
            f=functions.ScorePoints.score.append(1) #+1 point
            print("Computer's calculation: ",evaluated,"\tYour answer: ",user_input_answer)
            pass
        elif str(evaluated)[:4]==str(user_input_answer)[:4]:
            f=functions.ScorePoints.score.append(1) #+1 point
            print("Computer's calculation: ",evaluated,"\tYour answer: ",user_input_answer)
            pass
        
        else:
            print("Computer's calculation: ",evaluated,"\tYour answer: ",user_input_answer)
            f=functions.ScorePoints.score.append(0) #NO points
            pass

        print("You received a total of : ",functions.ScorePoints.score[-1]," points")
        #record_book
        solution_evaluated_n_input = ((evaluated),(user_input_answer))
        functions.Session.qna_record[question] = solution_evaluated_n_input
    
    obtained = sum(functions.ScorePoints.score)
    total = count-1
    print(f"\n{username} scored {obtained} points out of {total}\n")
    print(functions.report_tab())

if '__init__' == '__main__':
    
    Welcome_user()
    input()
    
