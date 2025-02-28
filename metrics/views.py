from django.shortcuts import render
from django.db.models import Avg
from review.models import CodeReview, Comment

def review_metrics(request):
    total_reviews = CodeReview.objects.count()
    average_rating = CodeReview.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']
    total_comments = Comment.objects.count()

    return render(request, 'metrics/review_metrics.html', {
        'total_reviews': total_reviews,
        'average_rating': average_rating,
        'total_comments': total_comments,
    })