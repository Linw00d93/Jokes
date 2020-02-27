from twilio.rest import Client
import random
import requests
import tweepy


url = "https://sv443.net/jokeapi/v2/joke/Miscellaneous?type=twopart"

response = requests.request("GET", url)

data = response.json()
response.text
#print(data)
joke = data['setup']
answer = data['delivery']
message = joke + answer

account_sid = '#############################'
auth_token = '#########################'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='##################',
                              body= message,
                              to='######################'
                          )

#print(message.sid)
