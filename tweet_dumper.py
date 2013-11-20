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
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	# liste für alle tweets
	alltweets = []	
	
	# anfrage für 200 tweets, das ist das maximum
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	# die letzten 200 tweets in die alltweets liste schreiben
	alltweets.extend(new_tweets)
	
	# älteste id speichern, damit danach die nächsten tweets geladen werden können 
	oldest = alltweets[-1].id - 1
	
	# solange tweets speichern bis es keine mehr gibt
	while len(new_tweets) > 0:
		print "hole tweets vor %s" % (oldest)
		
		# max_id gibt an, ab welchem tweet die nächsten 200 geladen werden sollen 
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		alltweets.extend(new_tweets)
		
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets heruntergeladen" % (len(alltweets))
	
	# schreibe tweets in zweidimensionale liste	
	outtweets = []
	for tweet in alltweets:
		outtweets.append([tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.source.encode("utf-8")])
	# csv datei schreiben
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(outtweets)
        print "\n\n--- Tweets gespeichert unter %s_tweets.csv ---\n\n" % screen_name
	pass
    

if __name__ == '__main__':
	# aufforderung zwei user anzugeben, für die die tweets runtergeladen werden sollen
    name_to_get1 = raw_input("Von welchem User sollen die letzten 3200 Tweets abgeholt werden?\nUsername: ")
    get_all_tweets(name_to_get1)
    name_to_get2 = raw_input("Bitte den zweiten User angeben, dessen Tweets gespeichert werden sollen.\nUsername: ")
    get_all_tweets(name_to_get2)
    
    
    
