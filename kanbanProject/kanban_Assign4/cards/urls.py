from django.conf.urls import url
from cards.views import CardList, CardDetail, TaskList, TaskDetail


urlpatterns = [
    url(
        r'^cards$',
        CardList.as_view(),
        name = CardList.name
    ),
    url(
        r'^cards/(?P<pk>[0-9]+)$',
        CardDetail.as_view(),
        name = CardDetail.name
    ),
    url(
        r'^tasks$',
        TaskList.as_view(),
        name = TaskList.name
    ),
    url(
        r'^tasks/(?P<pk>[0-9]+)$',
        TaskDetail.as_view(),
        name=TaskDetail.name
    )

]