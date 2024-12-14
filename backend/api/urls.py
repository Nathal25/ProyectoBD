from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, ProfesorViewSet

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'profesores', ProfesorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



