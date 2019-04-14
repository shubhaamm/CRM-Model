from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from apps.models import Image
#from tkinter import messagebox
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def mywebsite(request):
    return render(request, "shubh.html")


def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def signup(request):
     if request.method == 'POST':
         if request.POST['password1'] == request.POST['password2']:
             try:
                 user= User.objects.get(username=request.POST['username'])
                 return render(request, 'signup.html', {'error': 'Username is already taken '})
                 user = User.objects.get(email=request.POST['email'])
                 return render(request, 'signup.html', {'error': 'email is already taken '})
             except User .DoesNotExist:
                 user =User.objects.create_user(request.POST['username'],request.POST['email'],password =request.POST['password1'])
                 auth.login(request, user)
                 return redirect('mywebsite')

         else :
             return render(request, 'signup.html',{'error':'Password does not matched '} )

     else :
          return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
       user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
       if user is not None :
           auth.login(request, user)
           return redirect('mywebsite')
       else :
           return render(request, 'login.html' , {'error': 'username or password is incorrect'})


    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        messages.info(request, "logout successfully")
        return redirect('mywebsite')



def image(request):
    apps = Image.objects
    return render(request, "image.html" ,{'apps':apps} )

def tajm(request):
    return render(request, "tajm.html" )



def portfolio(request):
    value =['Shubham Singhal' ,'shivam singhal','shivay bansal']
    return render(request, "portfolio.html" ,{'name':value} )


#@login_required(login_url = 'login')
#def like_image(request, image_id):
 #   image = Image.object.get(id=image_id)
  #  image.likes.add(request.user)
   # return redirect('image')

@login_required(login_url = 'login')
def like_image(request):
    post = get_object_or_404(Image , id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('image')









































































