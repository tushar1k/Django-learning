from django.urls import path
from .import views

urlpatterns = [
    path('memb/', views.memb, name='memb'),
    path('form/', views.form, name='form'),
    path('coupenCode/', views.coupenCode, name='coupenCode'),
    path('full/', views.full, name='full'),
    path("",views.memb,name='memb'),
    path("january/", views.code, name='1st month'),
    path('feb/', views.feb, name='2nd month'),
    path('myself/', views.myself, name='myself'),
    path('formInput/', views.formInput, name="formInput"),
    path('about/', views.companyAbout, name='about'),
    path('sept/', views.sept, name = 'sept'),
    path('oct/', views.oct, name = 'oct'),
    path('nov/', views.nov, name = 'nov'),
    path('dec/', views.dec, name = 'dec'),
]