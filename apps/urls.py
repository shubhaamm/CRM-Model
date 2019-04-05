from apps import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include , path
from django.conf.urls import include , url
import apps.views




path('apps/', include('apps.urls')),
url(r'mplimage.png' ,apps.views.mplimage),
