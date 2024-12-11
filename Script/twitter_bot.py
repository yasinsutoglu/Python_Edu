import tweepy
import time

consumer_key = 'UhGZOyvUbcV2AdP6qKO0JVyO5'
consumer_secret = '4rBfUDC5GI5vfWZ7wrRGWC6z8L2IRnUHVRy552kuucr22ihucr'
access_token = '184273645-bdNU0KIie6lF5dt7befq1E0O22xCB8y2w4HfMn8Z'
access_token_secret = 'LKmvs4A7c2auo4RlVLP5ArNcij1wCIhgSQ6nOeguuWq0f'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
# print(user)   # it gives all the details, like name, scree_name, location, and various other info.
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = "bitcoin"
numberOfTweets = 2

def limit_handle(cursor):
	while True:
		try:
			yield cursor.next()

		except tweepy.RateLimitError:
			print("Sleeping now....")
			time.sleep(10)  # sleeps for 10 secs


# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     if follower.name == 'Usernamehere':
#         print(follower.name)
#         follower.follow()


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
	try:
		tweet.favorite()
		tweet.retweet()
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

# ----------------X_API_v2--------------------
# pip install tweepy
# import tweepy

# config.py : where I keep my keys as constants
# import config
#
#
# def about_me(client: tweepy.Client) -> None:
# 	"""Print information about the client's user."""
# 	# The `public_metrics` addition will give me my followers count, among other things
# 	me = client.get_me(user_fields=["public_metrics"])
# 	print(f"My name: {me.data.name}")
# 	print(f"My handle: @{me.data.username}")
# 	print(f"My followers count: {me.data.public_metrics['followers_count']}")
#
#
# def get_ztm_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
# 	"""Return a list of latest ZTM tweets"""
# 	ztm = client.get_user(username="zerotomasteryio")
# 	response = client.get_users_tweets(ztm.data.id)
# 	return response.data
#
#
# if __name__ == "__main__":
# 	client = tweepy.Client(
# 		bearer_token=config.BEARER_TOKEN,
# 		consumer_key=config.API_KEY,
# 		consumer_secret=config.API_SECRET,
# 		access_token=config.ACCESS_TOKEN,
# 		access_token_secret=config.ACCESS_SECRET,
# 	)
# 	print("=== About Me ===")
# 	about_me(client)
# 	print()
# 	print("=== ZTM Tweets ===")
# 	for tweet in get_ztm_tweets(client):
# 		print(tweet, end="\n\n")
