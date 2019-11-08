from django.conf.urls import url
from accounts.views import AccountList, AccountDetail

urlpatterns = [
    url(
        r'^accounts$',
        AccountList.as_view()
    ),
    url(
        r'^accounts/(?P<pk>[0-9]+)$',
        AccountDetail.as_view()
    )
]
