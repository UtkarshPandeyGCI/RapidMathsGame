import random
import time

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

def report():
    
    ques = list(Session.qna_record.keys())
    ans = list(Session.qna_record.values())
    #ans_u = Session.qna_record.values()[1]
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
