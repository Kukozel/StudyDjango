from django.conf.urls import url
from lists import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^(\d+)/$',views.view_list, name='view_list'),
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
    url(r'^login_page$', views.login_page, name='login_page'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
    url(r'^register$', views.register, name='register'),

]
