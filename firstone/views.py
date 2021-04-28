from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import requests
import apiview
from django.shortcuts import redirect
import json
import pandas as pd
# Create your views here.
def about(request):
    return HttpResponse('about # its 2nd func')
def myfunccall(request):
    return HttpResponse('Hello world!')
def about(request):
    return HttpResponse('about # its 2nd func')
def add(request,a,b):
    c = 'sum is='+str(a+b)+str('  and its 3rd func')
    return HttpResponse(c)
def name(request,name1,age):
    dict = {
        'name': name1,
        'age' : age
    }
    return JsonResponse(dict)
def firstpage(request):
    return render(request,'index.html')
def secondpage(request):
    return render(request,'second.html')
def thirdpage(request):
    name = 'rishi'
    options = ['lol','die','wtf']
    num1,num2 = 3,5
    ans = num1 > num2
    mydict = {'name':name, 'options':options,'num1':num1,'num2':num2,'ans':ans}
    return render(request,'third.html',context=mydict)
def fourthpage(request):
    return render(request,'fourth.html')
@csrf_exempt
def upload(request):
    print(request.body)
    if request.method == "POST":
        my_uploaded_file1 = request.FILES['myfile']
        data_file = request.FILES['myfile'] # get the uploaded file
        c = str(my_uploaded_file1)
        c = c.endswith('.csv')
        #print(my_uploaded_file)
        if c == True:
            files = {'data_file': request.FILES['myfile']}
            url = 'https://auto-allocation-ocxgf5ajua-uc.a.run.app/webhook'
            try:
                test_response = requests.post(url, files = files, timeout=10)
            except:
                return render(request,'fifth.html')
            response = redirect('thirdpage')
            return HttpResponse('File is csv')
        else:
            return HttpResponse(c)
        # do something with the file
        # and return the result            
    else:
        return render(request, 'index.html')
@csrf_exempt
@csrf_protect
def fifthpage(request):
    print(type(request.body))
    f1 = json.loads(request.body)
    column = f1.get('column')
    print(column)
    df = pd.DataFrame(columns = column)
    row = f1.get('row')
    print(row,type(row))
    for i in range(len(row)):
        df_length = len(df)
        df.loc[df_length] = row[i]
    print(df)
    dict1= {
        'column':column,
        'row':row
    }
    mydict = dict1
    return HttpResponse('ok')
def fifthpage1(request):
    return render(request,'fifth.html')
def upload1(request):
        return render(request, 'index.html')