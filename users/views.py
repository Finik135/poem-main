from django.shortcuts import render
from django.shortcuts import redirect

from users.forms import RegistrationForm, AuthorizationForm

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate


def registrate(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorization')
        messages.error(request, "doesn't valid username or password.")
    else:
        form = RegistrationForm()

    context = {
        "form": form
    }
    return render(request, "users/registration.html", context)


def authorize(request):
    if request.method == "POST":
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("poems:home")
            messages.error(request, 'Invalid login or password.')
    else:
        form = AuthorizationForm()

    context = {
        "form": form
    }
    return render(request, "users/authorization.html", context)


def logout_view(request):
    logout(request)
    return redirect("poems:home")
