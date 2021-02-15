from dataclasses import dataclass
from os import environ


@dataclass
class TweeterConfig:
    # Twitter API public and private key
    api_key = environ.get('TWITTER_API_KEY')
    api_secret = environ.get('TWITTER_API_SECRET')

    # Twitter account access token
    access_token = environ.get('TWITTER_ACCESS_TOKEN')
    access_secret = environ.get('TWITTER_ACCESS_SECRET')

    # Bot Settings
    time_of_publish = 60
    language = 'en'

    topics = [
        'payday2',
        'coding',
        'deep learning',
        'machine learning',
        'artificial intelligence',
        'neural network',
        'technology'
    ]


@dataclass
class Config:
    twitter = TweeterConfig()


# Init a global config object
config = Config()
