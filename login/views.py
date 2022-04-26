from django.http import  HttpResponse
from django.shortcuts import redirect, render

from login.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')

def otp(request):
    if(request.method == 'GET'):
        return redirect('/')
    elif(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        user = User()
        user.username = username
        user.password = password
        user.phone = phone
        user.save()
        context = {
            'username' : username
        }
        return render(request, 'otp.html', context)

def message(request):
    if(request.method == 'GET'):
        return redirect('/')
    elif(request.method == 'POST'):
        username = request.POST['username']
        otp = request.POST['otp']
        context = {'message' : 'User Created! We\'ll verify you soon.', 'messageClass': 'success'}
        try:
            user = User.objects.get(username=username)
            user.otp = otp
            user.save()
            context = {'message' : 'User Created! We\'ll verify you soon.', 'messageClass': 'success'}
        except:
            context = {'message' : 'There was an error. Please retry later.', 'messageClass': 'danger'}
        return render(request, 'index.html', context)