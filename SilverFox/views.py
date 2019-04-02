from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import User, Photo
from SilverFox.forms import LoginForm, MyUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class MainSiteView(ListView):
    model = Photo

    def get(self, request):
        ctx = {'photos': Photo.objects.all()}
        return render(request, 'main.html', ctx)


class UserView(LoginRequiredMixin, DetailView):
    model = User


class PhotoView(LoginRequiredMixin, DetailView):
    model = Photo


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('file', 'title', 'camera_name', 'film_type', 'film_name', 'film_iso', 'film_option1',
              'film_option2', 'photo_option1', 'photo_option2', 'description')

    def get_success_url(self):
        return reverse('photo', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("main")


class DeletePhotoView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.user
    model = Photo
    success_url = reverse_lazy("main")


class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('profile_image', 'description')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('user', args=[self.object.pk])


class EditPhotoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.user

    model = Photo
    fields = '__all__'
    exclude = ['date_added']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('photo', args=[self.object.pk])


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
    if request.method == 'GET':
        form = MyUserCreationForm()
        return render(request, 'signup.html', {'form': form})
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = MyUserCreationForm()
    return render(request, 'form.html', {'form': form})
