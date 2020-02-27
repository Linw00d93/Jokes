import requests
import tweepy
import random

CONSUMER_KEY ="#########################"
CONSUMER_SECRET = "######################"
ACCESS_KEY = "###############################"
ACCESS_SECRET = "##############################"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET )
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET )
api = tweepy.API(auth)

url = "https://sv443.net/jokeapi/v2/joke/Programming?type=twopart"

response = requests.request("GET", url)

data = response.json()
response.text
print(data)
joke = data['setup']
answer = data['delivery']

api.update_status("%s\n%s" %(joke,answer))
