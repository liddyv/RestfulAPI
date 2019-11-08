from django.conf.urls import url
from accounts.views import AccountList, AccountDetail, ContactList, ContactDetail

urlpatterns = [
    url(
        r'^accounts$',
        AccountList.as_view()
    ),
    url(
        r'^accounts/(?P<pk>[0-9]+)$',
        AccountDetail.as_view()
    ),
    url(
        r'^contacts$',
        ContactList.as_view()
    ),
    url(
        r'^contacts/(?P<pk>[0-9]+)$',
        ContactDetail.as_view()
    )
]
