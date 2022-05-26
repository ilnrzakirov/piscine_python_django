import json
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import auth


# Create your views here.
def index_view(request):
    data = request.POST
    if request.is_ajax():
        resData = json.dumps({'user': None})
        user = User.objects.filter(username=data['username'])
        if user:
            userAuth = auth.authenticate(username=data['username'], password=data['password'])
            if userAuth.is_active:
                auth.login(request, userAuth)
                resData = json.dumps({'user': userAuth.get_username()})
        return HttpResponse(resData, content_type='application/json')
    else:
        resData = json.dumps({'user': None})
    return HttpResponse(data, content_type='application/json')
