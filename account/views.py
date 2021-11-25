from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect


from .models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict


def register(request):
    if request.method == 'GET':
        user_form = UserRegistrationForm()
    elif request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            form = user_form.save(commit=False)
            form.password = make_password(request.POST['password'])
            form.save()
            return redirect('login')   
    context = {'user_form': user_form}
    return render(request, 'account/register.html', context)

        
def login(request):
    if request.method == 'GET':
        user_form = UserLoginForm()
    elif request.method == 'POST':
        user_form = UserLoginForm(data=request.POST)
        if user_form.is_valid():
            email = request.POST['email']
            user = User.objects.get(email=email)
            request.session['user'] = model_to_dict(user)
            return redirect('shop:home')
    context = {'user_form': user_form}
    return render(request, 'account/login.html', context)

def logout(request):
    del request.session['user']
    return HttpResponseRedirect(reverse('login'))
    
    
