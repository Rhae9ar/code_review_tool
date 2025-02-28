import requests
from django.core.cache import cache

GITHUB_API_URL = 'https://api.github.com'

def get_user_repos(token):
    cache_key = f'user_repos_{token}'
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{GITHUB_API_URL}/user/repos', headers=headers)
    if response.status_code == 200:
        data = response.json()
        cache.set(cache_key, data, 3600)  # Кэшируем на 1 час
        return data
    return []

def get_repo_pull_requests(token, repo_owner, repo_name):
    cache_key = f'repo_pull_requests_{repo_owner}_{repo_name}'
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data
    headers = {'Authorization': f'token {token}'}
    response = requests.get(f'{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/pulls', headers=headers)
    if response.status_code == 200:
        data = response.json()
        cache.set(cache_key, data, 300)  # Кэшируем на 5 минут
        return data
    return []