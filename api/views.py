from rest_framework import generics
from review.models import CodeReview, Comment, PullRequest
from .serializers import CodeReviewSerializer, CommentSerializer, PullRequestSerializer

class CodeReviewList(generics.ListCreateAPIView):
    queryset = CodeReview.objects.all()
    serializer_class = CodeReviewSerializer

class CodeReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodeReview.objects.all()
    serializer_class = CodeReviewSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PullRequestList(generics.ListCreateAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

class PullRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer