# Social media presence (twitter bot)
With a defined config ...
```python
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
```

... this bot is able to retweet interesting post for you.

**Like that :**

![Exemple](assets/exemple.png)
