from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from datetime import datetime
from home.models import contact
from django.contrib import messages


def login_page(request):
   if request.method=='POST':
      username=request.POST.get("username")
      password=request.POST.get("password")
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
         #return render(request,'home.html')
         return redirect('home')
      else:
         messages.error(request,"Invalid Username or Password!")
   return render(request,'login.html')

def signup(request):
   if request.method=='POST':
      username=request.POST.get('new-user-username')
      password1=request.POST.get('new-user-password1')
      password2=request.POST.get('new-user-password2')
      print(username)
      if (password1!=password2):
         messages.warning(request,"Entered Passwords Dosen't Mathch")
      else:
         User.objects.create_user(username=username,password=password1)
         return redirect('login')
   return render(request,'signup.html')

def logout_user(request):
   logout(request)
   return redirect('login')

def home(request):
   if request.user.is_anonymous:
      return redirect('login')

   return render(request,'home.html')
   
def contact_page(request):
   if request.method=="POST":
      name1=request.POST.get('first_name')
      name2=request.POST.get('last_name')
      email=request.POST.get('email')
      phone_number=request.POST.get('phone_number')
      country=request.POST.get('country')
      query=request.POST.get('query')
      username=request.user
      Contact=contact(username=username,first_name=name1,last_name=name2,email=email,phone_number=phone_number,country=country,query=query,date_time=datetime.now())
      Contact.save()
      messages.success(request,"Form Has Been Submitted Successfully!!")

   #return HttpResponse("<h1>Contact</h1>")
   return render(request,'contact.html')

def link(request):
   return render(request,'link.html')