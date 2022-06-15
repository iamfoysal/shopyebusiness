from django.urls import path

from . import views



urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('account/', views.account, name='account'),
    path('account_update/', views.account_update, name='account_update'),

]
