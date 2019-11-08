from django.conf.urls import url, include
from django.urls import path
from accounts.web_views import index, api_first_index

urlpatterns = [
    url(
        r'^api/',
        include('accounts.urls')
    ),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    path('', api_first_index)
]
