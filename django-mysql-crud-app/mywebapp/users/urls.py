# from django.conf.urls import url
from django.urls import re_path

from users import views

urlpatterns = [
    re_path(r'^api/users$',views.users_list),
    re_path(r'^api/users/(?P<pk>[0-9]+)$', views.user_detail),
    # re_path('testcookie/', views.cookie_session),
    # re_path('deletecookie/',views.cookie_delete),
]