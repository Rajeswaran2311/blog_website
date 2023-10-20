from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeRe,name='home'),
    path('Home/',views.home,name='home'),
    path('Home/login/',views.LoginPage,name='login'),
    path('Home/logout/',views.LogoutPage,name='logout'),
    path('Home/signup/',views.SignupPage,name='signup'),
    path('Home/<str:tag>/',views.index_fetch,name='index_ai'),

     
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
