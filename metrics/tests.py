from django.test import TestCase
from review.models import CodeReview, Comment
from django.contrib.auth.models import User
from .views import review_metrics
from django.test import RequestFactory

class MetricsTest(TestCase):
    def test_review_metrics(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        CodeReview.objects.create(pull_request_id=1, user=user, rating=5)
        Comment.objects.create(pull_request_id=1, user=user, text='Test comment')
        request = RequestFactory().get('/metrics/')
        response = review_metrics(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Total Reviews: 1')