from django.conf.urls import url
from . import views

app_name = 'basic_auth'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]