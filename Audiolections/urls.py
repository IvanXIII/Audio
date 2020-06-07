
from django.contrib import admin
from django.urls import path
from App.views import tasks, lections, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('feedback/', tasks, name='tasks'),
    path('lections/', lections),
    path('home/', home),
]
