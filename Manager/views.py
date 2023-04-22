from django.shortcuts import render,redirect,get_object_or_404
from .models import tasks
from .forms import inputfiled,InputField
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from email_validator import validate_email

# Create your views here.

def index(request):
    

    if request.method == "POST":
        if request.user.is_authenticated:
            input_text = request.POST["task"]
            forms = InputField(request.POST)
            if forms.is_valid():
                #current_user = request.user.id
                #current = request.user
                #user = User.objects.get(id=current_user)
                #tasks.userr = user
                #tas = tasks.objects.create(task=input_text)
                tas = forms.save(commit=False)
                tas.userr = request.user
                #tas = tasks(userr=request.user,task=input_text)
                tas.save()
                return redirect("index")
        else:
            messages.error(request, "Please signup before adding task")
            #return redirect("index")
    else:
        if request.user.is_authenticated:
            taskss = tasks.objects.filter(userr = request.user)
            forms = InputField()
        else:
            taskss = None
            forms = InputField()
    
    return render(request, "Manager/index.html", {"tasks":taskss,"forms":forms})
    


def editt(request, pk):
    redit = get_object_or_404(tasks, pk=pk)

    if request.method == "POST":
        forms = InputField(request.POST, instance=redit)
        if forms.is_valid():
            forms.save()
            return redirect("index")
        
    else:
        forms = InputField(instance=redit)
        return render(request, "Manager/edit.html", {"forms":forms,"redit":redit})
    

def deletee(request, pk):

    task =  tasks.objects.get(pk=pk)
    task.delete()

    return redirect("index")


def register(request):

    if request.method == "POST":
        firstn = request.POST.get("First Name")
        secondn = request.POST.get("Second Name")
        usernamee = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        usernamee = usernamee.lower()

        def checkk(emailll):
            try:
                # validate and get info
                v = validate_email(email, check_deliverability=True)
                # replace with normalized form
                emailll = v["email"] 
                return True

            except:
                return False


        if User.objects.filter(username=usernamee).exists():
            messages.error(request, "Username is already taken")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken")
            return redirect("register")
        elif checkk(email) != True:
            messages.error(request, "Please provide a valid email")
            return redirect("register")
        elif password1 != password2:
            messages.error(request, "Make sure that the passwords are matching")
            return redirect("register")
        else:
            userr = User.objects.create_user(username=usernamee,password=password1,email=email)
            userr.save()
            return redirect('login')
        
    else:
        return render(request, 'Manager/register.html')

def login_in(request):
    if request.method == "POST":
        usernamee = request.POST.get('username')
        password = request.POST.get('password')

        usernamee = usernamee.lower()
        
        user = authenticate(request, username=usernamee,password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credintials")
            return redirect('login')


    return render(request, 'Manager/login.html')

def logout_it(request):
    logout(request)

    return redirect('/')