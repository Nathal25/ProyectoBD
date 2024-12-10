from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login, name="login"),
    path('registroP/',views.registroP, name="registroP"),
    path('registroE/',views.registroE, name="registroE")
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)