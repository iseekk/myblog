from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.forms import CustomAuthForm
from blog.views import change_password
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(authentication_form=CustomAuthForm), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("accounts/update/", change_password, name="profile_update")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
