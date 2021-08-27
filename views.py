from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    return render(request, 'textutils/index.html')


def analyze(request):
    # GET the text
    dj_text = request.POST.get('text', 'default')
    # Check radio button is ON
    removePunc = request.POST.get('removePunc', 'off')
    upperCase = request.POST.get('upperCase', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    doubleSpaceRemover = request.POST.get('doubleSpaceRemover', 'off')
    charCounter = request.POST.get('charCounter', 'off')
    print(dj_text)
    print(removePunc)
    # Analyze the text
    if (removePunc != 'on' and upperCase != 'on' and newLineRemover != 'on' and doubleSpaceRemover != 'on' and charCounter != 'on'):
        return HttpResponse('Error - Please select any operation and try again.')
    else:
        if removePunc == 'on':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ''
            for char in dj_text:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': 'Removed Punctuation is', 'analyzed_text': analyzed}
            dj_text = analyzed
        if upperCase == 'on':
            analyzed = ''
            for char in dj_text:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
            dj_text = analyzed
        if newLineRemover == 'on':
            analyzed = ''
            for char in dj_text:
                if char != '\n' and char != '\r':
                    analyzed = analyzed + char
            params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
            dj_text = analyzed
        if doubleSpaceRemover == 'on':
            analyzed = ''
            for index, char in enumerate(dj_text):
                if not(dj_text[index] == ' ' and dj_text[index+1] == ' '):
                    analyzed = analyzed + char
            params = {'purpose': 'Double Space Remover', 'analyzed_text': analyzed}
            dj_text = analyzed
        if charCounter == 'on':
            analyzed = 'Character Count: ', len(dj_text)
            params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}

        
        return render(request, 'textutils/analyze.html', params)
        

def read_text(request):

    site = ['<h1>read_text!</h1><hr><a href="http://localhost:8000/textutils/">Home!</a><hr>'] # Not working

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    f = open('textutils/one.txt')
    content = f.read()
    print(content)
    f.close()
    return HttpResponse(content)


def personal_navigator(request):
    sites = '''
    <h1>personal_navigator!</h1><hr>
    <a href="http://localhost:8000/textutils/">Home!</a><hr>
    <a href="https://www.coreyms.com">Visit CoreyMS!</a><br>
    <a href="https://www.techwithtim.net">Visit techwithtim.net!</a><br>
    <a href="https://www.codewithtomi.com">Visit codewithtomi.com!</a><br>
    <a href="https://www.dennisivy.com">Visit dennisivy.com!</a><br>
    <a href="https://www.freecodecamp.org">Visit freecodecamp.org!</a><hr>
    '''
    return HttpResponse(sites)