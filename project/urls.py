"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from SilverFox.views import MainSiteView, UserView, PhotoView, LoginView, LogoutView, signup, AddPhotoView, \
    EditUserView, DeleteUserView, DeletePhotoView, EditPhotoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', MainSiteView.as_view(), name='main'),
    url(r'^user/(?P<pk>\d+)/$', UserView.as_view(), name="user"),
    url(r'^edit_user/(?P<pk>\d+)/$', EditUserView.as_view(), name="edit-user"),
    url(r'^edit_photo/(?P<pk>\d+)/$', EditPhotoView.as_view(), name="edit-photo"),
    url(r'^photo/(?P<pk>(\d)+)/$', PhotoView.as_view(), name="photo"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', LogoutView.as_view(), name="logout"),
    url(r'^signup$', signup, name="signup"),
    url(r'^add_photo$', AddPhotoView.as_view(), name="add-photo"),
    url(r'^delete_user/(?P<pk>(\d)+)/$', DeleteUserView.as_view(), name="delete-user"),
    url(r'^delete_photo/(?P<pk>(\d)+)/$', DeletePhotoView.as_view(), name="delete-photo"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
