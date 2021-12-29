import random
import time
from tabulate import tabulate

operators=['+','-','*','/']
time_full = time.ctime()[11:19]

class Session:
    qna_record = {}
    
    def question_module():
        rn1=random.randint(1,9)
        rn_op = random.choice(operators)
        rn2=random.randint(1,9)
        eject = str(rn1)+rn_op+str(rn2)
        return eject

class ScorePoints:
    score = []

def report(): #NOT in use
    
    ques = list(Session.qna_record.keys())
    ans = list(Session.qna_record.values())
    marks = ScorePoints.score
    print("""
                                        REPORT
                                        ------
                                        
Sr.No.      Question       Computer's Calculation        User's Answer         Points""")
    
    for i in range(len(Session.qna_record)):
        d1=ques[i]
        d2=ans[i][0]
        d3=ans[i][1]
        d4=marks[i]
             
        print("""
{}          {}                 {}                         {}                   {}""".format(i,d1,d2,d3,d4))
    
def report_tab():
    ques = list(Session.qna_record.keys())
    ans = list(Session.qna_record.values())
    marks = ScorePoints.score

    srno =[]
    quest =[]
    comp =[]
    user =[]
    marksl=[]
    for i in range(len(Session.qna_record)):
        srno.append(i)
        quest.append(ques[i])
        comp.append(ans[i][0])
        user.append(ans[i][1])
        marksl.append(marks[i])

    #CHECK
    if len(srno)==len(quest)==len(comp)==len(user)==len(marksl):
        pass
    else:
        print(srno,quest,comp,user,marksl,"list len not satisfied")
    #Check pass

    data = []
    for n in range(len(srno)):
        data_form = [srno[n],quest[n],comp[n],user[n],marksl[n]]
        data.append(data_form)
        
    print("""
                                    REPORT
                                    ------
""")
    headers = ['Srno','Question',"Computer's calculation","User's answer","Points"]
    print(tabulate(data,headers = headers))    
    
def report_file(name):
    location = "C:\\Users\\UPLC\\Desktop\\"
    file_name = f"{name}'s_RMG_Report_{time_full}"
    file = open(location+file_name+'.txt','w')
    file.write("Sr.No.      Question       Computer's Calculation        User's Answer         Points")
    pass
