from django.shortcuts import render
from urllib.parse import quote
import oauth2


CONSUMER_KEY = "971404513759387649-qDApGrr3ICjeoo0Y0vTIrdx5638i7l0"
CONSUMER_SECRET = "N4wItkYqC97fIvIF0awUXoI8ibkgLjvKYmuHBO5NE6NLb"

def oauth_req(url, key, secret, http_method="GET", post_body=””, http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content




def tweet_search(request):
	query = "@joincoded"
	enc_q = quote(query)
	url = 'https://api.twitter.com/1.1/search/tweets.json?q=%s'%(enc_q)
	token = "some_token"
	token_secret = "some_token_secret"
	response = oauth_req(url, token, token_secret, "GET")

	print (response)
	pass
