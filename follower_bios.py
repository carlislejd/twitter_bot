import tweepy

from os import getenv
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(getenv('TWITTER_API_KEY'), getenv('TWITTER_API_KEY_SECRET'))
auth.set_access_token(getenv('ACCESS_TOKEN'), getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth, wait_on_rate_limit=True)

followers = []
hiring = []
for user in tweepy.Cursor(api.get_followers, screen_name=getenv('SCREEN_NAME')).items():
    print(f'{user.screen_name}:, {user.name}, {user.description}')
    followers.append(f'{user.screen_name}:, {user.name}, {user.description}')
    if 'hiring' in user.name.lower() or 'hiring' in user.description.lower():
        print(f"!!! {user.screen_name}")
        hiring.append(user.screen_name)

with open('followers.txt', 'w', encoding='utf-8') as f:
    for line in followers:
        f.write(f"{line}\n")

with open('hiring.txt', 'w', encoding='utf-8') as f:
    for line in hiring:
        f.write(f"{line}\n")