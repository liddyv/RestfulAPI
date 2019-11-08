from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    max_limit = 4


class BookPagination(LimitOffsetPagination):
    default_limit = 10
