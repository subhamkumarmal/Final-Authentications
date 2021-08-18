from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('students',views.StudentView)
urlpatterns=[
    path('',include(router.urls)),
    path('api-token-auth/',obtain_auth_token)
]