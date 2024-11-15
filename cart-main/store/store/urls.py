
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.urls')),
    path('cart/',include('cart.urls')),
    path('register/',include('user.urls')),
    path('', RedirectView.as_view(url='/products/',permanent=False)),

    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
