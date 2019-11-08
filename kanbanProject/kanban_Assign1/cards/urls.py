from django.conf.urls import url
from cards.views import CardList, CardDetail


urlpatterns = [
    url(
        r'^cards$',
        CardList.as_view()
    ),
    url(
        r'^cards/(?P<pk>[0-9]+)$',
        CardDetail.as_view()
    )
]