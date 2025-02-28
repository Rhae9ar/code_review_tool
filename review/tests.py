from django.test import TestCase

from .models import CodeReview, Comment
from .github_api import get_user_repos, get_repo_pull_requests

from django.contrib.auth.models import User

class GitHubAPITest(TestCase):
    def test_get_user_repos(self):
        # Mock GitHub API response
        # Проверяем, что функция возвращает ожидаемые данные
        pass

    def test_get_repo_pull_requests(self):
        # Mock GitHub API response
        # Проверяем, что функция возвращает ожидаемые данные
        pass

class CodeReviewTest(TestCase):
    def test_create_code_review(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        review = CodeReview.objects.create(pull_request_id=1, user=user, rating=5)
        self.assertEqual(review.rating, 5)


class CommentTest(TestCase):
    def test_create_comment(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        comment = Comment.objects.create(pull_request_id=1, user=user, text='Test comment')
        self.assertEqual(comment.text, 'Test comment')
