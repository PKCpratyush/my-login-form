from os import renames
from django.http import HttpResponse
from django.shortcuts import render

from .models import our_users

def index(request):
    return render(request, 'index.html')

def show_data(request):
    
    user_id = request.POST.get('ID','')
    user_name  = request.POST.get('Name','')
    user_password = request.POST.get('Password','')

    # print(identity,name,password)

    if user_id == "":
        return render(request, "index.html", {"id_exist":"please do not leave ID blank"})

    if user_name == "":
        return render(request, "index.html", {"id_exist":"please fill the username section"})

    if user_password == "":
        return render(request, "index.html", {"id_exist":"please provide password"})

    flag = False
    result = our_users.objects.all()
    for item in result:
        if item.user_id == user_id:
            if item.user_password == user_password and item.user_name == user_name:
                return render(request, 'information.html', {"user_exist":True, "data":result})
            flag = True
            break
    if flag == True:
        result = {"message": "please provide unique user ID"}
        return render(request, "index.html", {"id_exist":"please provide unique user ID"})

    user = our_users(user_name = user_name, user_id = user_id,  user_password = user_password)
    user.save()

    print(result)
    return render(request, 'information.html', {"user_exist":False, "data":result})