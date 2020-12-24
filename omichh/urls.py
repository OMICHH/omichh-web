from django.contrib import admin
from django.urls import path

# Static files config
from django.conf import settings
from django.conf.urls.static import static

# Views
from django.contrib.auth import views as auth_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users Views
    path('', users_views.landing_view, name='landing'),
    path('login/', users_views.login_view, name='login'),
    path('home/', users_views.dashboard, name='dashboard')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
