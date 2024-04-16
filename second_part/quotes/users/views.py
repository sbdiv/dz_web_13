from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ResetPasswordForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.conf import settings

def reset_password_request(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')

            try:
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    form.add_error('username', 'User with this username or email does not exist.')
                    return render(request, 'your_app/reset_password.html', {'form': form})

            token = default_token_generator.make_token(user)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_password_url = f"{settings.BASE_URL}/reset-password/{uid}/{token}/"

            subject = 'Reset your password'
            message = render_to_string('your_app/reset_password_email.html', {'reset_password_url': reset_password_url})
            sender_email = settings.DEFAULT_FROM_EMAIL
            recipient_email = user.email
            send_mail(subject, message, sender_email, [recipient_email])

            return render(request, 'your_app/reset_password_success.html')
    else:
        form = ResetPasswordForm()
    return render(request, 'your_app/reset_password.html', {'form': form})




def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotesapp:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
       return redirect(to='quotesapp:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotesapp:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotesapp:main')