from django.shortcuts import render ,redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count']+=1
    else :
        request.session['count']=1

    request.session['random']=get_random_string(length=14)
    return render(request, 'index.html')

def clean(request):
    del request.session['count']
    return redirect("/random_word")
