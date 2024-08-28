
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.hellworld,name="signup"),
    path('signup/', views.signup,name="signup"),
]

