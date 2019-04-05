from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from apps.models import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
import pandas as pd
import matplotlib.pyplot as plt
#import sqlite3
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import django
import io
import matplotlib.pyplot as plt;plt.rcdefaults()


#movies=sqlite3.connect('transactions_practice.csv')

movies=pd.read_csv( 'media/books/pdfs/transactions_practice1.csv' , sep=',')
movies=movies.dropna()

def mywebsite(request):
    return render(request, "shubh.html")


def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def retail(request):
    return render(request, "retail.html")

def analysis(request):
    return render(request, "analysis.html")

def book_list(request):
  books = Book.objects.all()
  return render(request, 'book_list.html', { 'books': books})



@login_required
def upload_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      return redirect('book_list')
  else:
    form = BookForm()
  return render(request, 'upload_book.html', { 'form' : form })


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
           return redirect('upload_book')
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

def Aa(request):
    custgroup = movies[['id','purchaseamount']].groupby('id').sum()
    custgroup1 = custgroup.nlargest(10,'purchaseamount')
    cs = custgroup1
    cs.to_csv('outA.csv',sep='\t')
    f=open('outA.csv','r')
    file_content=f.read()
    f.close()
    context={'file_content':file_content}
    return render(request, "Aa.html" ,context)




def Bb(request):
    chainsales=movies[['chain','purchasequantity','purchaseamount']].groupby('chain').sum()
    cs=chainsales
    cs.to_csv('outB.csv', sep='\t')
    f = open('outB.csv', 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "Bb.html",context)

def Cc(request):
    chainTop10Cust=movies[['chain','id','purchaseamount']].groupby(['chain','id']).sum()
    chainTop10Cust1=chainTop10Cust.groupby('chain')
    chainTop10Cust1.head(10).sort_values(by=['purchaseamount'],ascending=False)
    cp=chainTop10Cust1.head(10)
    cp.to_csv('out2.csv',sep='\t')
    f=open('out2.csv','r')
    file_content=f.read()
    f.close()
    context={'file_content':file_content}
    return render(request, "Cc.html", context)

def Dd(request):
    T10brands=movies[['brand','purchaseamount']].groupby('brand').sum()
    T=T10brands.nlargest(10,'purchaseamount')
    T.to_csv('out3.csv',sep='\t')
    f=open('out3.csv','r')
    file_content=f.read()
    f.close()
    context={'file_content':file_content}
    return render(request, "Dd.html",context)

def Ee(request):
    T10Companies=movies[['company','purchaseamount']].groupby('company').sum()
    T10=T10Companies.nlargest(10,'purchaseamount')
    T10.to_csv('out4.csv',sep='\t')
    f=open('out4.csv','r')
    file_content=f.read()
    f.close()
    context={'file_content':file_content}
    return render(request, "Ee.html",context)

def Ff(request):
    BrandTop10Cust=movies[['id','brand','purchasequantity']].groupby(['id','brand']).sum()
    BrandTop10Cust1=BrandTop10Cust.groupby('brand')
    BrandTop10Cust1.head(10).sort_values(by=['purchasequantity'],ascending=False)
    Bbb=BrandTop10Cust1.head(10)
    Bbb.to_csv('out5.csv',sep='\t')
    f=open('out5.csv','r')
    file_content=f.read()
    f.close()
    context={'file_content':file_content}
    return render(request, "Ff.html",context)









































































