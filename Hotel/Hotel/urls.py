"""
Definition of urls for Hotel.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib.auth.views import logout

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^signup$', app.views.sign_up, name='signup'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^profile$', app.views.profile, name='profile'),
    url(r'^editprofile$', app.views.edit_profile, name='edit_profile'),
    url(r'^roomsdetails/(?P<room_id>\d+)$', app.views.rooms_details, name='rooms_details'),
    url(r'^$', app.views.login, name='login'),
    #url(r'^login/$',
   #     django.contrib.auth.views.login,
    #    {
     #       'template_name': 'app/login.html',
      #      'authentication_form': app.forms.BootstrapAuthenticationForm,
       #     'extra_context':
        #    {
         #       'title': 'Log in',
          #      'year': datetime.now().year,
           # }
        #},
        #name='login'),
    #url(r'^logout$',
     #   django.contrib.auth.views.logout,
      #  {
       #     'next_page': '/',
       # },
        #name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
