#!/usr/bin/env python
# encoding: utf-8
# quelle: http://matplotlib.org/examples/units/bar_unit_demo.html 
# quelle: vorlesung informetrie projektseminar

import numpy as np
import matplotlib.pyplot as plt
import read_tweets_from_csv, operator

datei = raw_input("Dateinamen angeben: ")

(hashtag1_sorted, mentions1_sorted, clients1_sorted, woerter1_sorted, jahre1, monate1, tage1) = read_tweets_from_csv.analyse_tweets(datei)
username = datei.split("_tweets.csv")[0]

#monate1 = {'2013-03': 33, '2012-12': 60, '2013-02': 61, '2012-05': 14, '2012-06': 48, '201
#2-10': 12, '2012-09': 4, '2012-08': 22, '2013-08': 81, '2013-09': 47, '2012-11':
# 37, '2013-04': 42, '2013-05': 90, '2013-06': 80, '2013-07': 31, '2012-07': 53,
#'2013-01': 5, '2013-11': 7, '2013-10': 34}

#monate1 muss noch bearbeitet werden damit man die daten auslesen kann.

months_percent = []

months_whole = sum(monate1.values())

for key, value in monate1.iteritems():
    value_percent = 100 * float(value)/float(months_whole)
    months_percent.append(value_percent)


plt.figure(1)
labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'white','red', 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue']

plt.subplot(121)
sizes=months_percent
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.title('Tweets per Month: '+username)
plt.axis('equal')


plt.subplot(122)
sizes=months_percent
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.title('Tweets per Month')
plt.axis('equal')

plt.show()

