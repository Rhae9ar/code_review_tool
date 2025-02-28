from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.review_dashboard, name='review_dashboard'),
    path('submit_review/<int:pull_request_id>/', views.submit_review, name='submit_review'),
    path('submit_comment/<int:pull_request_id>/', views.submit_comment, name='submit_comment'),

]