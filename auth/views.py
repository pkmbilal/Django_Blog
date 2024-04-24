from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    user = request.user
    if request.method == 'POST':
        first_name = request.POST.get('firstname').strip()
        last_name = request.POST.get('lastname').strip()
        email = request.POST.get('email').strip()
        current_password = request.POST.get('currentpassword')
        new_password = request.POST.get('newpassword')
        if not current_password and not new_password:
            messages.error(request,'Empty fields detected!!!')
            return render(request,'authapp/index.html',{'user':user})
        if user.check_password(current_password):
            user.set_password(new_password)
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if email:
                user.email = email
            user.save()
            messages.success(request,'User Updated Successfully.')
            return render(request,'index.html',{'user':user})
        messages.error(request,'Wrong Password!!!')
        return render(request,'authapp/index.html',{'user':user})
    else:
        return render(request,'authapp/index.html',{'user':user})
        
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def adminDashboard(request):
    Dict = {'userobj':User.objects.all()}
    if request.method == 'POST':
        delEmployee = request.POST.get('empDel')
        employee = User.objects.filter(username=delEmployee).exists()
        if employee:
            User.objects.filter(username=delEmployee).delete()
            return render(request,'authapp/admin.html',Dict)
        else:
            return render(request, 'authapp/admin.html',Dict)
    else:
        return render(request, 'authapp/admin.html',Dict)

def signupView(request):
    if request.method == 'POST':
        firstname = request.POST['firstname'].strip()
        lastname = request.POST['lastname'].strip()
        email = request.POST['email'].strip()
        username = request.POST['username'].strip()
        password = request.POST['password']

        existing_username = User.objects.filter(username=username).exists()
        existing_email = User.objects.filter(email=email).exists()

        if email and existing_email:
            messages.error(request,'Email is Already Taken!!!')
            return render(request,'registration/signup.html')
        
        if firstname and username and password is not None:
            if existing_username:
                messages.error(request,'Username is Already Taken!!!')
                return render(request,'registration/signup.html')
            
            user = User.objects.create(username=username)
            user.set_password(password)
            user.first_name = firstname
            user.last_name = lastname
            if email:
                user.email=email
            user.save()
            messages.success(request, 'User created successfully.')
            return redirect('login')
        else:
            messages.error(request,'Firstname or Username or Password is Empty!!!')
            return render(request,'registration/signup.html')
    else:
        return render(request, 'registration/signup.html')

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username, password=password)
        isAdmin=User.objects.filter(username=username).first()
        if user is not None:
            login(request,user)
            if isAdmin.is_superuser == 1:
                return redirect('adminDashboard')
            return redirect('home')
        elif not user:
            messages.error(request,'Wrong Credentials!!!')
            return render(request, 'registration/login.html')
        else:
            messages.error(request,'Empty Username or Password!!!')
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')
    
def logoutView(request):
    logout(request)
    return redirect('home')

def forgotPassword(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname').strip()
        username = request.POST.get('username').strip()
        new_password = request.POST.get('newpassword')

        if not username or not first_name or not new_password:
            messages.error(request, 'Firstname or Username or Password Empty!!!')
            return render(request, 'registration/forgotpassword.html')
        
        try:
            user = User.objects.get(username=username)
            isFirstname = User.objects.filter(first_name=first_name).first()
            if user is not None:
                if isFirstname:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request,'Password Reset Successfully')
                    return redirect('login')
                else:
                    messages.error(request,'Incorrect First name!!!')
                    return render(request, 'registration/forgotpassword.html')
            messages.error(request,'Username is empty!!!')
            return render(request, 'registration/forgotpassword.html')
        except User.DoesNotExist:
            messages.error(request,'User does not exists!!!')
            return render(request, 'registration/forgotpassword.html')
    else:
        return render(request, 'registration/forgotpassword.html')
    