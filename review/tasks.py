from celery import shared_task
import requests
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import PullRequest 
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json



GITHUB_API_URL = 'https://api.github.com'

def get_user_repos(token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{GITHUB_API_URL}/user/repos', headers=headers)
    return response.json()

def get_repo_pull_requests(token, repo_owner, repo_name):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/pulls', headers=headers)
    return response.json()

@shared_task
def check_new_pull_requests():
    for user in User.objects.all():
        try:
            social_auth = user.social_auth.get(provider='github')
            token = social_auth.extra_data['access_token']
            repos = get_user_repos(token)
            for repo in repos:
                owner = repo['owner']['login']
                repo_name = repo['name']
                pull_requests = get_repo_pull_requests(token, owner, repo_name)
                for pr in pull_requests:
                    if not PullRequest.objects.filter(pr_id=pr['id'], user=user).exists():
                        PullRequest.objects.create(pr_id=pr['id'], user=user)
                        send_mail(
                            'New Pull Request',
                            f'A new pull request "{pr['title']}" has been created in {repo_name}.',
                            'from@example.com',
                            [user.email],
                            fail_silently=False,
                        )
        except Exception as e:
            print(f"Error processing user {user.username}: {e}")

@shared_task
def update_pull_requests_status():
    pull_requests = PullRequest.objects.all()
    for pr in pull_requests:
        token = pr.user.social_auth.get(provider='github').extra_data['access_token']
        repo_owner = pr.repository_owner
        repo_name = pr.repository_name
        pulls = get_repo_pull_requests(token, repo_owner, repo_name)
        for pull in pulls:
            if pull['id'] == pr.pr_id:
                pr.status = pull['state']
                pr.save()
                break
