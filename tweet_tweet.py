import tweepy
import time

auth = tweepy.OAuthHandler(input("Input your consumer key, please: "), input("Input your consumer secret, please: "))
auth.set_access_token(input("Input your access token, please: "), input("Input your access token secret, please: "))

api = tweepy.API(auth)
user = api.verify_credentials()

def limit_handler(cursor): # function that prevents twitter from being overloaded by our requests by setting a timeout when we hit TooManyRequests error
    try:
        while True:
            yield cursor.next()
    except tweepy.TooManyRequests:
        time.sleep(300)
    except StopIteration:
        return

search_string = input("Input key text for searching, please: ")
numbers_of_tweets = int(input("Input number of tweets you want to like, please: "))

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numbers_of_tweets):
    try:
        tweet.favorite()
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
