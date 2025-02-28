from django.shortcuts import render, redirect
from .github_api import get_user_repos, get_repo_pull_requests

from .forms import CodeReviewForm, CommentForm
from .models import CodeReview, Comment



def review_dashboard(request):
    token = request.session.get('oauth_token')['access_token']
    repos = get_user_repos(token)
    pull_requests = []
    for repo in repos:
        prs = get_repo_pull_requests(token, repo['owner']['login'], repo['name'])
        pull_requests.extend(prs)
    return render(request, 'review/dashboard.html', {'pull_requests': pull_requests})



def submit_review(request, pull_request_id):
    if request.method == 'POST':
        form = CodeReviewForm(request.POST)
        if form.is_valid():
            CodeReview.objects.create(
                pull_request_id=pull_request_id,
                user=request.user,
                rating=form.cleaned_data['rating']
            )
            return redirect('review_dashboard') # Замените 'review_dashboard' на URL вашей страницы
        else:
            form = CodeReviewForm()
    return render(request, 'review/submit_review.html', {'form': form, 'pull_request_id': pull_request_id})

from .forms import CommentForm
from .models import Comment

def submit_comment(request, pull_request_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                pull_request_id=pull_request_id,
                user=request.user,
                text=form.cleaned_data['text']
            )
            return redirect('review_dashboard')  # Замените 'review_dashboard' на URL вашей страницы
    else:
        form = CommentForm()
    return render(request, 'review/submit_comment.html', {'form': form, 'pull_request_id': pull_request_id})