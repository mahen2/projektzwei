#!/usr/bin/env python
# encoding: utf-8
# quelle: http://matplotlib.org/examples/units/bar_unit_demo.html 
# quelle: vorlesung informetrie projektseminar

import numpy as np
import matplotlib.pyplot as plt
import read_tweets_from_csv

datei = raw_input("Dateinamen angeben: ")

(hashtag1_sorted, mentions1_sorted, clients1_sorted, woerter1_sorted, jahre1, monate1, tage1) = read_tweets_from_csv.analyse_tweets(datei)
username = datei.split("_tweets.csv")[0]


days_percent = []

days_whole = sum(tage1.values())

for key, value in tage1.iteritems():
    value_percent = 100 * float(value)/float(days_whole)
    days_percent.append(value_percent)


labels='Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
sizes=days_percent
colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'white','red']
explode=(0, 0, 0, 0, 0, 0, 0) # explode nothing for now
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.show()
