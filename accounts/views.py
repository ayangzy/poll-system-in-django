from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {'error': 'This username Already Exist'})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'accounts/register.html', {'error': 'This email is already taken'})
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password
                    )
                    user.save()
                    # you can decide to log the user in after successful registration
                    # auth.login(request, user)
                    # return redirect('constestants')
                    # return render(request, 'accounts/login.html', {'success': 'You have successfully registered, you can now login to vote for your prefered candidate'})
                    return redirect('login')

        else:
            return render(request, 'accounts/register.html', {'error': 'Password must match'})
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('contestants')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    else:
        return render(request, 'accounts/logout.html')
