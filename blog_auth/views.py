from django.contrib.auth import login, authenticate
from django.views import View

from .forms import SignUpForm
from django.shortcuts import render, redirect


class CreateSignup(View):
    def get(self, request):
        form = SignUpForm
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')

        return render(request, 'signup.html', {'form': form})
