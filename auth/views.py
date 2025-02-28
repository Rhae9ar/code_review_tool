from django.shortcuts import render



from django.shortcuts import redirect
from requests_oauthlib import OAuth2Session

GITHUB_CLIENT_ID = 'your_github_client_id'
GITHUB_CLIENT_SECRET = 'your_github_client_secret'
REDIRECT_URI = 'http://localhost:8000/auth/callback/'
AUTHORIZATION_BASE_URL = 'https://github.com/login/oauth/authorize'
TOKEN_URL = 'https://github.com/login/oauth/access_token'

def github_login(request):
    github = OAuth2Session(GITHUB_CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = github.authorization_url(AUTHORIZATION_BASE_URL)
    request.session['oauth_state'] = state
    return redirect(authorization_url)

def github_callback(request):
    github = OAuth2Session(GITHUB_CLIENT_ID, state=request.session['oauth_state'])
    token = github.fetch_token(TOKEN_URL, client_secret=GITHUB_CLIENT_SECRET, authorization_response=request.build_absolute_uri())
    request.session['oauth_token'] = token
    return redirect('home') # Замените 'home' на URL вашей домашней страницы