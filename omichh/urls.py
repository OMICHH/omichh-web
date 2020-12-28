from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

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
    path('logout/', users_views.logout_view, name='logout'),
    path('singup/', users_views.sing_up_view, name='singup'),
    path('home/', users_views.dashboard, name='dashboard'),

    #Verification user
    path('activate/<uidb64>/<token>', users_views.VerificationView.as_view(), name='activate'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
