from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import numpy as np

data=pd.read_csv('/home/fastboi/projects/python/python_django_pbl/mysite/QuizManagement/static/QuizManagement/PblQuest1.csv', index_col=[0])
data['Questions']=data['Questions'].astype(str)
questions=data['Questions']
answers=data.drop(['Questions'],axis=1).values
dList={'ques' : questions, 'ans':answers}

def home(request):
    
    return render(request, 'QuizManagement/home.html')

def test(request):
    content={'fin' : dList }
    return render(request, 'QuizManagement/test.html', content)

