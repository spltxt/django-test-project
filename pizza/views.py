from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from pizza.forms import CustomAuthenticationForm, CustomUserCreationForm


User = get_user_model()


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    error_message = None
    form = CustomAuthenticationForm
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('products:products')
        else:
            error_message = 'Произошла ошибка'

    context = {
        'form': form,
        'error_message': error_message,
    }

    return render(request, 'auth/login.html', context)


def sign_up_view(request):
    error_message = None
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('products:products')
        else:
            error_message = 'Произошла ошибка. Пожалуйста, заполните форму ещё раз.'

    context = {
        'form': form,
        'error_message': error_message,
    }

    return render(request, 'auth/sign_up.html', context)
