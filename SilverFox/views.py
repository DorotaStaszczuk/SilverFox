from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import User, Photo
from SilverFox.forms import AddPhotoForm, AddUserForm, EditPhotoForm, EditUserForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
class MainSiteView(ListView):
    model = Photo
    paginate_by = 50
    def get(self, request):

        return render(request, template_name='main.html')


class UserView(LoginRequiredMixin, DetailView):
    model = User


class PhotoView(LoginRequiredMixin, DetailView):
    model = Photo


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    exclude = ['date_added']
    success_url = reverse_lazy("/photo")


class AddUserView(CreateView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy("/user")


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("/main")


class DeletePhoto(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy("/user")


class EditUser(LoginRequiredMixin, UpdateView):
    model = User
    fields = '__all__'
    template_name_suffix = '_update_form'


class EditPhoto(LoginRequiredMixin, UpdateView):
    model = Photo
    exclude = ['date_added']
    template_name_suffix = '_update_form'


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)
            if user is None:
                form.add_error('login', 'Login lub hasło jest niepoprawne')
                return render(request, "login.html",
                              {'form': form})
            login(request, user)
            return redirect('main')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'form.html', {'form': form})