from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

#, password_change_done, password_change

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('portfolio.urls', namespace='portfolio')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    #url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^reset-password/$', views.password_reset, name='password_reset'),
    url(r'^reset-password/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', views.password_reset_complete, name='password_reset_complete'),

    url(r'^password-change/$', views.password_change, name='password_change'),
    url(r'^password-change/done/$', views.password_change_done, name='password_change_done'),
    #url(r'^password-change/done/$', views.login, name='password_change_done'),
   #i wanted to change the default screen opened after a successful pwd change to be the login screen but had issues of not logging off automatically

   # url(r'^password-change/$', password_change, name='password_change'),
   # url(r'^password-change/done/$', password_change_done, name='password_change_done'),
]


