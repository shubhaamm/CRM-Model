from django.contrib import admin
from django.urls import path
from apps import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact , name='contact'),
    path('mywebsite/', views.mywebsite , name='mywebsite'),
    path('login/', views.login , name='login'),
    path('signup/', views.signup , name='signup'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
             name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
             name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
             name='password_reset_complete'),

    path('image/', views.image , name='image'),

    path('tajm/', views.tajm , name='tajm'),

    path('like_image/', views.like_image, name='like_image')


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






