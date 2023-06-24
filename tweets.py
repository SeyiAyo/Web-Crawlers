import tweepy

#Authenticate:
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#To scrape tweets from a user's timeline:
tweets = api.user_timeline(screen_name="twitter_handle", count=10)
for tweet in tweets:
    print(tweet.text)

#To scrape tweets containing specific keywords:
tweets = api.search(q="keyword", count=10)
for tweet in tweets:
    print(tweet.text)


#Handle Rate Limits:
for tweet in tweepy.Cursor(api.user_timeline, screen_name="twitter_handle", count=200).items(1000):
    print(tweet.text)


# Scrape tweets from the source account
source_tweets = api.user_timeline(screen_name="source_account", count=10)

# Repost tweets to the destination account
for tweet in source_tweets:
    repost_text = f"Reposted from @{tweet.user.screen_name}: {tweet.text}"
    api.update_status(status=repost_text)
