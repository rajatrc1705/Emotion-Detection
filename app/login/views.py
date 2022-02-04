from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import StreamingHttpResponse
from login.emotion_detection import Emotion_detection
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
global username

def indexView(request):
    global username
    username=request.user
    return render(request,'home.html')

def aboutView(request):
    global username
    username=request.user
    return render(request,'aboutus.html') 


@login_required(login_url='login_url')  
def dashboardView(request):
    global username
    username=request.user
    return render(request,'dashboard.html') 

@login_required(login_url='login_url')  
def testView(request):
    global username
    username=request.user
    return render(request,'test.html')     

def registerView(request): 
    if request.user.is_authenticated:
        global username
        username=request.user
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == "POST" :
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Succesfully!')
                return redirect('login_url')

        context = {'form' :form}
        return render(request,'register.html',context) 



def loginView(request): 
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == "POST" :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is Incorrect!')
        
        context ={}

        return render(request,'login.html',context)
        
def logoutView(request): 
    logout(request)
    return redirect('login_url')

#rest api

class ReactView(APIView):
    
    def get(self, request):
        global username
        detail =  {"name": str(username),"detail": "sdfasdf"}
        return Response(detail)

global a
b=True

def facecam_feed(request):
    try:
        global a
        a=Emotion_detection()

        return StreamingHttpResponse(gen(a), content_type="multipart/x-mixed-replace;boundary=frame")
    except: 
        pass



def gen(camera):
    global b
    b=True
    
    while b:
        frame = camera.get_frame()
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

              
# def disableCamera(request):
#     global a
#     a.vs.stream.release()
    