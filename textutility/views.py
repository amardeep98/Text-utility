#created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dict = {'name':'Amar', 'place':'Mars'}
    return render(request, 'index.html', dict)

def analyze(request):
    dtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercount=request.POST.get('charactercount','off')
    analyzed_text = ""

    if removepunc=='on':
        punctuations='''!(){}[]'":;,.<>/?@#$%^&_-~*'''
        for char in dtext:
            if char not in punctuations:
                analyzed_text = analyzed_text+char
        params = {'purpose':'removepunc','analyzed_text':analyzed_text}
        dtext=analyzed_text

    if fullcaps=='on':
        for char in dtext:
            analyzed_text=analyzed_text + char.upper()
        params = {'purpose':'Upper Case','analyzed_text':analyzed_text}
        dtext=analyzed_text

    if newlineremover=='on':
        for char in dtext:
            if char !="\n" and char!='\r':
                analyzed_text = analyzed_text + char
        params = {'purpose':'Remove Newline','analyzed_text':analyzed_text}
        dtext=analyzed_text

    if extraspaceremover=='on':
        for index, char in enumerate(dtext):
            if not(dtext[index] ==" " and dtext[index+1]==' '):
                analyzed_text = analyzed_text + char
        params = {'purpose':'Remove Extra Space','analyzed_text':analyzed_text}
        dtext=analyzed_text

    if charactercount=='on':
        count=0
        for char in dtext:
            count+=1
        analyzed_text=count
        params = {'purpose':'Count characters','analyzed_text':analyzed_text}
        
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charactercount!="on"):
        return HttpResponse("<center>Error. Please select an operation and try again</center>")

    return render(request,'analyze.html',params)
    