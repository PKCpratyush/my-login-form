from os import renames
from django.http import HttpResponse
# from django.shortcuts import render

# from ..log.models import our_users

# def index(request):
#     return render(request, 'index.html')

# def show_data(request):
    
#     user_id = request.POST.get('ID','')
#     user_name  = request.POST.get('Name','')
#     user_password = request.POST.get('Password','')

#     # print(identity,name,password)

#     user = our_users(user_name = user_name, user_id = user_id,  user_password = user_password)
#     user.save()

#     result = our_users.objects.all()
#     return render(request, 'information.html', {"data":result})