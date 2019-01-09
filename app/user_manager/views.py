from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegisterForm, LoginForm
from .models import User


class IndexView(TemplateView):
    template_name = 'user_manager/index.html'
    form = LoginForm

    def get(self, request):
        if 'userauth' in request.session:
            return redirect('task-list')

        return render(request, self.template_name, {'form': self.form()} )

    def post(self, request):
        if 'userauth' in request.session:
            return redirect('task-list')

        form = self.form(request.POST)

        if form.is_valid():
            try:
                user_email = request.POST.get('email')
                user_password = request.POST.get('password')
                user_obj = User.objects.get(email=user_email)
                if check_password(user_password, user_obj.password):
                    request.session['userauth'] = {
                        'username': user_obj.username,
                        'email': user_obj.email,
                        'user_id': user_obj.id
                    }
                    return redirect('task-list')
                else:
                    messages.error(request, "Invalid password.")
            except Exception as e:
                messages.error(request, str(e))

        return render(request, self.template_name, {'form': form})


class RegisterView(TemplateView):
    template_name = 'user_manager/register.html'
    form = RegisterForm

    def get(self, request):
        if 'userauth' in request.session:
            return redirect('task-list')

        return render(request, self.template_name, {'form': self.form()} )


    def post(self, request):
        if 'userauth' in request.session:
            return redirect('task-list')

        form = self.form(request.POST)

        if form.is_valid():
            data = {
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
                'password': make_password(request.POST.get('password')),
            }
            try:
                userObj = User(**data)
                userObj.save()
                messages.success(request, 'User Registered successfully !!')
                return redirect('login')
            except IntegrityError as e:
                messages.error(request, "This email is already exists Please try with another email")

        return render(request, self.template_name, {'form': form} )        


class Logout(TemplateView):
    def get(self, request):
        request.session['userauth'] = ''
        messages.success(request, 'Logged out successfully')
        return redirect('login')
