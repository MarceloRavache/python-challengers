import tweepy

consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'token'
access_token_secret = 'token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
username = 'nome_de_usuario'
tweets = api.user_timeline(screen_name=username, count=10)

for tweet in tweets:
    print('Tweet ID:', tweet.id)
    print('Texto:', tweet.text)
    print('Data da postagem:', tweet.created_at)
    print('Usuário:', tweet.user.screen_name)
    print('---')