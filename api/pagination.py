from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'pagina'
    page_size_query_param = 'cantidad'
    max_page_size = 10