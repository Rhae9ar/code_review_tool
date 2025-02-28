from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.CodeReviewList.as_view()),
    path('reviews/<int:pk>/', views.CodeReviewDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('pullrequests/', views.PullRequestList.as_view()),
    path('pullrequests/<int:pk>/', views.PullRequestDetail.as_view()),
]