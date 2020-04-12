from django.shortcuts import render
from  . import fake_model
from . import ML_predict

def home(request):
    return render(request,'index.html')

def result(request):
    pcclass = int(request.GET['pcclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])
    prediction = ML_predict.prediction_model(pcclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request,'result.html', {'prediction': prediction})
