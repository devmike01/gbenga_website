from django.contrib import admin
from django.urls import path, include
from gbenga_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'my_profile', views.ProfileView, 'profile')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
