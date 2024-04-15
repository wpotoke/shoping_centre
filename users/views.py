from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            # session_key for not registrate users
            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, вы вошли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirest_page = request.POST.get("next", None)
                if redirest_page and redirest_page != reverse("user:logout"):
                    return HttpResponseRedirect(request.POST.get("next"))

                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"title": "Home - Авторизация", "form": form}
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)

        # session_key for not registrate users
        session_key = request.session.session_key

        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(
                request,
                f"{user.username}, вы успешно зарегистрированны и вошли в аккаунт",
            )
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Home - Регистрация", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            messages.success(request, "профайл успешно обновлен")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)
    context = {"title": "Home - Кабинет", "form": form}
    return render(request, "users/profile.html", context)


def users_cart(request):
    return render(request, "users/users_cart.html")


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse("main:index"))
