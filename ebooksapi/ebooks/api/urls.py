from django.urls import path
from ebooks.api.views import EbookList, EbookDetail, ReviewCreate, ReviewDetailAPIView

urlpatterns = [
    path('ebooks/', EbookList.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>/', EbookDetail.as_view(), name='ebook-detail'),
    path('ebooks/<int:ebook_pk>/review/', ReviewCreate.as_view(), name='ebook-review'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
