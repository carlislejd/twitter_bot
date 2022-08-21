import random
import tweepy

from os import getenv
from time import sleep
from dotenv import load_dotenv

load_dotenv()



client = tweepy.Client(bearer_token=getenv('BEARER_TOKEN'), access_token=getenv('ACCESS_TOKEN'))

likes = client.get_liking_users(id='1488515618185883659')
print(f'{len(likes[0])} People liked it')
usernames = []
for users in likes[0]:
    sleep(.3) #add dramatic pause
    print(users.username)
    usernames.append(users.username)
    
print('______________')
print('Selecting a winner....') # more dramatic pause
sleep(3) # more dramatic pause
print(f'Congrats {random.choice(usernames)}!')