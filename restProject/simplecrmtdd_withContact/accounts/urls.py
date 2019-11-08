from django.conf.urls import url
from accounts.views import AccountList, ContactList


urlpatterns = [
    url(
        r'^accounts$',
        AccountList.as_view(),
        name=AccountList.name
    ),
    url(
        r'^contacts$',
        ContactList.as_view(),
        name=ContactList.name
    )
]