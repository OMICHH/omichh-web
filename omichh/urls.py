from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

# Static files config
from django.conf import settings
from django.conf.urls.static import static

# Views
from django.contrib.auth import views as auth_views
from users import views as users_views
from blog import views as blog_views
from events import views as events_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users Views
    path('', users_views.landing_view, name='landing'),
    path('login/', users_views.login_view, name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('singup/', users_views.sing_up_view, name='singup'),
    path('home/', users_views.dashboard, name='dashboard'),
    path('complete_profile/', users_views.complete_profile_view, name='complete_profile'),
    path('info_profile/', users_views.info_profile_view, name='info_profile'),
    
    path('coach_admin/', users_views.coach_admin_view, name='coach_admin'),
    path('results/', users_views.results_view, name='results'),

    #Events Views
    path('calendar/', events_views.calendar_view, name='calendar'),

    # Blog views
    path('blog/', blog_views.blog_view, name='blog'),

    #General Views
    path('about/', TemplateView.as_view(template_name="index/about.html"), name='about'),
    path('contact/', users_views.contact_view, name='contact'),

    #Verification user
    path('activate/<uidb64>/<token>', users_views.VerificationView.as_view(), name='activate'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
