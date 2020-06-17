from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from App.views import tasks, lections, home, lol, lect1, lect2, lect3, lect4, lect5
from Audiolections import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('feedback/', tasks, name='tasks'),
    path('lections/', lections),
    path('home/', home),
    path('lections/list_of_lections/', lol),
    path('lections/list_of_lections/lect1/', lect1),
    path('lections/list_of_lections/lect2/', lect2),
    path('lections/list_of_lections/lect3/', lect3),
    path('lections/list_of_lections/lect4/', lect4),
    path('lections/list_of_lections/lect5/', lect5),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
