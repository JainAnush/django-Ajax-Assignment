from django.shortcuts import render
import mysql.connector
from mysql.connector import Error
from .models import quiz
def showThankYouPage(request):
    return render(request,'thanks.html')
def showHomePage(request):
    return render(request,'homepage.html')
# def addQuestions(request):
#     record1=quiz(question_id=1,question="who developed python",option1="dennis ritchie",option2="james gosling",option3="guido van rossum",option4="none",correctans=3)
#     record1.save()
#     record2=quiz(question_id=2,question="who developed java",option1="dennis ritchie",option2="james gosling",option3="guido van rossum",option4="none",correctans=2)
#     record2.save()
#     record3=quiz(question_id=3,question="who developed C",option1="dennis ritchie",option2="james gosling",option3="guido van rossum",option4="none",correctans=1)
#     record3.save()
#     record4=quiz(question_id=4,question="who developed JS",option1="dennis ritchie",option2="james gosling",option3="guido van rossum",option4="none",correctans=4)
#     record4.save()
#     record5=quiz(question_id=5,question="who developed C++",option1="dennis ritchie",option2="james gosling",option3="guido van rossum",option4="bjarne stroustrup",correctans=4)
#     record5.save()
#     record_count=quiz.objects.count()
#     return render(request,'quesadded.html',{'count':record_count})

def getAllQuestions(request):
    question_list=[]
    all_questions=quiz.objects.all()
    objcount=quiz.objects.count()
    for ques in all_questions:
        question_list.append({'question':ques.question,'option1':ques.option1,'option2':ques.option2,'option3':ques.option3,'option4':ques.option4})
        print(objcount)
    for i in range(objcount):
        question_list[i].update({'name':i})  
    return render(request,'questions.html',{'ques_list':question_list})    

def processresult(request):
    score=0
    correct=0
    wrong=0
    correctanslist=[]
    all_questions=quiz.objects.all()
    objcount=quiz.objects.count()
    for ques in all_questions:
        correctanslist.append(ques.correctans)
    for i in range(objcount):
        userans=request.GET[str(i)]
        if int(userans)==correctanslist[i]:
            score+=4
            correct+=1
        else:
            wrong+=1
            score-=1        
    percentage=score/20*100
    remarks=''
    if percentage>=50:
        remarks="CONGRATULATIONS YOU PASSED THE TEST"
    else:
         remarks="SORRY YOU COULD NOT PASS THE TEST THIS TIME"            
    return render(request,'result.html',{'score':score,'correct':correct,'wrong':wrong,'remarks':remarks,'percentage':percentage})
# def getAllQuestions(request):
#     questions_list=[]
#     try:
#         connection=mysql.connector.connect(host='localhost',database='django',user='root',password='root')
#         if connection.is_connected():
#             cursor = connection.cursor()
#             cursor.execute("select * from questions;")
#             records = cursor.fetchall()
#             # print("connected to database: ", records)
#             for record in records:
#                 questions_list.append({'question':record[0],"option1":record[1],"option2":record[2],"option3":record[3],"option4":record[4]})
#                 # print('QUESTION :',record[0])
#                 # print("OPTION 1:",record[1])
#                 # print("OPTION 2:",record[2])
#                 # print("OPTION 3:",record[3])
#                 # print("OPTION 4:",record[4])
#                 # print("CORRECT ANS:",record[5])
#             print(questions_list)    
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")  
#             for i in range(5):
#                 questions_list[i].update({'name':i})   
#             return render(request,'questions.html',{'ques_list':questions_list})  
# def processresult(request):
#     try:
#         correctanslist=[]
#         connection=mysql.connector.connect(host='localhost',database='django',user='root',password='root')
#         if connection.is_connected():
#             cursor = connection.cursor()
#             cursor.execute("select correctans from questions;")
#             records = cursor.fetchall()
#             # print("You're connected to database: ", record)
#             for record in records:
#                 correctanslist.append(record[0])   
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")  
#             score=0
#             correct=0
#             wrong=0
#             for i in range(5):
#                 userans=request.GET[str(i)]
#                 if int(userans)==correctanslist[i]:
#                     score+=4
#                     correct+=1
#                 else:
#                     wrong+=1
#                     score-=1    
#             percentage=score/20*100
#             remarks=''
#             if percentage>=50:
#                 remarks="CONGRATULATIONS YOU PASSED THE TEST"
#             else:
#                 remarks="SORRY YOU COULD NOT PASS THE TEST THIS TIME"            
#             return render(request,'result.html',{'score':score,'correct':correct,'wrong':wrong,'remarks':remarks,'percentage':percentage})                

