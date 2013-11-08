#!/usr/bin/env python
# encoding: utf-8
# QUELLE: https://gist.github.com/yanofsky/5436496

import tweepy, csv, geheim

#Twitter API credentials
consumer_key = geheim.consumer_key
consumer_secret = geheim.consumer_secret
access_key = geheim.access_key
access_secret = geheim.access_secret


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	print dir(tweet)
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text","source"])
		writer.writerows(outtweets)
        print "\n\n--- Tweets gespeichert unter %s_tweets.csv ---\n\n" % screen_name
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
    name_to_get1 = raw_input("Von welchem User sollen die letzten 3200 Tweets abgeholt werden?\nUsername: ")
    get_all_tweets(name_to_get1)
    name_to_get2 = raw_input("Bitte den zweiten User angeben, dessen Tweets gespeichert werden sollen.\nUsername: ")
    get_all_tweets(name_to_get2)
    
    
    