from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import user
from django.db import connections

def onlyapp(request):
    un = request.GET.get('username')
    pwd = request.GET.get('password')
    ans = user.objects.raw("SELECT * FROM onlyapp_user where user_name='{}'".format(un))
    #with connection.cursor() as cursor:
         #cursor.execute("SELECT * from user where username='%s'",[self.un])
         #ans=cursor.fetchall()
    return render(request,'login_form.html',{'ans':ans})
