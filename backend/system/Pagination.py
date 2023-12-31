from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,
            'page_size': self.page_size,
            'count': self.page.paginator.count,
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'data': data
        })