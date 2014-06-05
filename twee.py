"""
Scraping tweets of Heat players
6-5-14

"""

import tweepy

# aka api_key and api_secret
consumer_key = "yQRF7kad5xihOjRUXeBfp8lHC"
consumer_secret = "Z0BUjHm3S9kaqrfcicebclWpuHl1LO8v7rhRx5t3LrT2YrEugC"

access_token = '51443987-GCVx1Ou7gGkrl0eHrKLtscVhnQ9gt6YfIYEgOKjje'
access_token_secret = 'znleGuqjNuxOqxdefkidEZqlU2lFa8uj5yxLi8CqAl1QZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

spurs = api.get_user('tonyparker')
heat = api.get_user('kingjames')

print api.show_friendship(source_id=heat.id, target_id=spurs.id)


"""
p1 = api.get_user('mchalmers15')
p2 = api.get_user('dwyanewade')
p3 = api.get_user('shanebattier')
p4 = api.get_user('kingjames')
p5 = api.get_user('chrisbosh')


print api.show_friendship(source_id=p1.id, target_id=p2.id)[0].all_replies
print api.show_friendship(source_id=p1.id, target_id=p3.id)[0].all_replies
print api.show_friendship(source_id=p1.id, target_id=p4.id)[0].all_replies
print api.show_friendship(source_id=p1.id, target_id=p5.id)[0].all_replies

print api.show_friendship(source_id=p2.id, target_id=p1.id)[0].all_replies
print api.show_friendship(source_id=p2.id, target_id=p3.id)[0].all_replies
print api.show_friendship(source_id=p2.id, target_id=p4.id)[0].all_replies
print api.show_friendship(source_id=p2.id, target_id=p5.id)[0].all_replies

print api.show_friendship(source_id=p3.id, target_id=p1.id)[0].all_replies
print api.show_friendship(source_id=p3.id, target_id=p2.id)[0].all_replies
print api.show_friendship(source_id=p3.id, target_id=p4.id)[0].all_replies
print api.show_friendship(source_id=p3.id, target_id=p5.id)

print api.show_friendship(source_id=p4.id, target_id=p1.id)[0].all_replies
print api.show_friendship(source_id=p4.id, target_id=p2.id)[0].all_replies
print api.show_friendship(source_id=p4.id, target_id=p3.id)[0].all_replies
print api.show_friendship(source_id=p4.id, target_id=p5.id)[0].all_replies

print api.show_friendship(source_id=p5.id, target_id=p1.id)[0].all_replies
print api.show_friendship(source_id=p5.id, target_id=p2.id)[0].all_replies
print api.show_friendship(source_id=p5.id, target_id=p3.id)
print api.show_friendship(source_id=p5.id, target_id=p4.id)[0].all_replies
"""
