from rest_framework import serializers
from review.models import CodeReview, Comment, PullRequest

class CodeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeReview
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PullRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequest
        fields = '__all__'