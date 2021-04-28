from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
import json
import requests
import pandas as pd
import time
#from .serializers import TaskSerializer
# Create your views here.
#@api_view(['GET'])
mydict = {}

@csrf_exempt
def show(request):
    return render(request,'fifth.html',context=mydict)
def table(request):
        return render(request,'fifth.html',context=mydict)
def getdata(request):
        return JsonResponse(mydict)
@csrf_exempt
def apioverview(request):
    f1 = json.loads(request.body)
    column = f1.get('column')
    #print(column)
    df = pd.DataFrame(columns = column)
    row = f1.get('row')
    #print(row,type(row))
    for i in range(len(row)):
        df_length = len(df)
        df.loc[df_length] = row[i]
    #print(df)
    dict1= {
        'column':column,
        'row':row
    }
    global mydict
    mydict = dict1
    redirect('/api/view')
    try:
        return HttpResponse('ok')
    finally:
        return redirect('/api/table')
def uploadpage(request):
    return render(request,'fourth.html')
def upload(request):
    print(request.method)
    if request.method == "POST":
        my_uploaded_file1 = request.FILES['myfile']
        data_file = request.FILES['myfile'] # get the uploaded file
        print(str(my_uploaded_file1))
        c = str(my_uploaded_file1)
        c = c.endswith('.csv')
        #print(my_uploaded_file)
        if c == True:
            files = {'data_file': request.FILES['myfile']}
            url = 'https://auto-allocation-ocxgf5ajua-uc.a.run.app/webhook'
            try:
                test_response = requests.post(url, files = files, timeout=180)
            except:
                return redirect('/api/view')
            #print(type(test_response))
            return redirect('/api/view')
        else:
            return HttpResponse('File is not a csv')
        # do something with the file
        # and return the result            
    else:
        return HttpResponse('some error')