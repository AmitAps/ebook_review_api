from rest_framework.pagination import PageNumberPagination

#https://www.django-rest-framework.org/api-guide/pagination/#modifying-the-pagination-style
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
