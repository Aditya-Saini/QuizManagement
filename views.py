from django.shortcuts import render, redirect
from django.http import HttpResponse

import pandas as pd
import numpy as np

data=pd.read_csv('/home/fastboi/projects/python/python_django_pbl/mysite/QuizManagement/static/QuizManagement/PblQuest1.csv', index_col=[0])
data['Questions']=data['Questions'].astype(str)
questions=data['Questions']
answers=data.drop(['Questions'],axis=1).values
dList={'ques' : questions, 'ans':answers}
print(answers[0][0])
def home(request):
    
    return render(request, 'QuizManagement/home.html')

def test(request):
    marks=0
    if request.method == "POST":
        for i in range(1,11):
            myVar = request.POST.get("quiz-"+str(i))
            print(myVar,i,answers[i-1][3])
            if(str(myVar) == str(answers[i-1][0])):
                marks+=1
        print(marks)
        return redirect("home")
            
    content={'fin' : dList }
    return render(request, 'QuizManagement/test.html', content)

