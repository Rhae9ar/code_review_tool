from django.db import models
from django.contrib.auth.models import User

class CodeReview(models.Model):
    pull_request_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'Review for PR #{self.pull_request_id} by {self.user.username}'

class Comment(models.Model):
    pull_request_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on PR #{self.pull_request_id}'

class PullRequest(models.Model):
    pr_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repository_owner = models.CharField(max_length=255)
    repository_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'PR #{self.pr_id} by {self.user.username}'