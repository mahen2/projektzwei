#!/usr/bin/env python
# encoding: utf-8
# quelle: http://matplotlib.org/examples/units/bar_unit_demo.html 
# quelle: vorlesung informetrie projektseminar

import numpy as np
import matplotlib.pyplot as plt
import read_tweets_from_csv, operator

#datei1 = raw_input("Dateinamen angeben: ")
#datei2 = raw_input("Dateinamen angeben: ")

datei1 = 'epidota2_tweets.csv'
datei2 = 'dota2rainbow_tweets.csv'

(hashtag1_sorted, mentions1_sorted, clients1_sorted, woerter1_sorted, jahre1, monate1, tage1) = read_tweets_from_csv.analyse_tweets(datei1)
(hashtag2_sorted, mentions2_sorted, clients2_sorted, woerter2_sorted, jahre2, monate2, tage2) = read_tweets_from_csv.analyse_tweets(datei2)

username1 = datei1.split("_tweets.csv")[0]
username2 = datei2.split("_tweets.csv")[0]


#Ueberprueft ob alle monate vorhanden sind, wenn nicht werden die fehlenden hinzugefuegt.
#to do: monate sortieren

#def check_months(monate):
    #for key, value in monate.iteritems():
        #key = int(key)
    #print monate
    #k = 1
    #while k < 13:
        #if monate.has_key(k):
            #print "YEEEESSSSSSSSSSSSSSSS"
        #else:
            #print "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        #k += 1


months_percent1 = []
months_percent2 = []

def calculate_percent(monate, months_percent):
    global months_percent1
    global months_percent2
    months_whole = sum(monate.values())
    for key, value in monate.iteritems():
        value_percent = 100 * float(value)/float(months_whole)
        months_percent.append(value_percent)

calculate_percent(monate1, months_percent1)
calculate_percent(monate2, months_percent2)


plt.figure(1)
labels='January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'white', 'red', 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue']

plt.subplot(121)
sizes=months_percent1
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.title('Tweets per Month: '+username1)
plt.axis('equal')


plt.subplot(122)
sizes=months_percent2
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.title('Tweets per Month: '+username2)
plt.axis('equal')

plt.show()

