from django.shortcuts import render
from django.http import JsonResponse
from urllib.parse import quote
import oauth2
import requests
import json





CONSUMER_KEY = "bRIFJ8Imlul6jE8m4Iae8xoLI"
CONSUMER_SECRET = "xCz4RcYMBSMh7atMsiPTpgphDoNEwX1EKg7ieuquqMH9E1yDkj"

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, http_method, bytes(post_body, "utf-8"), headers=http_headers )
    return content




def tweet_search(request):
	user = request.user
	social_account = user.socialaccount_set.get(user=user.id)
	app_token = social_account.socialtoken_set.get(account=social_account.id)
	token = app_token.token
	token_secret = app_token.token_secret

	query = "@joincoded"
	enc_q = quote(query)
	url = 'https://api.twitter.com/1.1/search/tweets.json?q=%s'%(enc_q)


	response = oauth_req(url, token, token_secret, "GET")
	stuff = json.loads(response)
	return JsonResponse(stuff, safe=False)

def tweet_post(request):
	user = request.user
	social_account = user.socialaccount_set.get(user=user.id)
	app_token = social_account.socialtoken_set.get(account=social_account.id)
	token = app_token.token
	token_secret = app_token.token_secret

	query = "@wazaaaaaaaaaaap"
	enc_q = quote(query)
	url = 'https://api.twitter.com/1.1/statuses/update.json?status=%s'%(enc_q)


	response = oauth_req(url, token, token_secret, "POST")
	stuff = json.loads(response)
	return JsonResponse(stuff, safe=False)
