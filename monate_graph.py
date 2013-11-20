#!/usr/bin/env python
# encoding: utf-8
# quelle: http://matplotlib.org/examples/units/bar_unit_demo.html 
# quelle: vorlesung informetrie projektseminar

import numpy as np
import matplotlib.pyplot as plt
import read_tweets_from_csv, operator

#datei1 = raw_input("Dateinamen angeben: ")
#datei2 = raw_input("Dateinamen angeben: ")

datei1 = 'ladygaga_tweets.csv'
datei2 = 'justinbieber_tweets.csv'

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
    monate_liste_v=[]
    for value in monate1_sorted: #an listen anpassen
        monate_liste_v.append(value[1])
    months_whole = sum(monate_liste_v)
    for element in monate:
        value_percent = 100 * float(element[1])/float(months_whole)
        months_percent.append(value_percent)




# fehlende monate werden mit 0 ersetzt (schrecklich programmiert, aber das ist glaub ich am einfachsten):

for i in xrange(12):
    if i < 9:
        if '0'+str(i+1) in monate1:
            pass
        else:
            monate1['0'+str(i+1)]=0
    else:
        if str(i+1) in monate1:
            pass
        else:
            monate1[str(i+1)]=0


for i in xrange(12):
    if i < 9:
        if '0'+str(i+1) in monate2:
            pass
        else:
            monate2['0'+str(i+1)]=0
    else:
        if str(i+1) in monate2:
            pass
        else:
            monate2[str(i+1)]=0


monate1_sorted = sorted(monate1.iteritems(), key=operator.itemgetter(0))
monate2_sorted = sorted(monate2.iteritems(), key=operator.itemgetter(0))

calculate_percent(monate1_sorted, months_percent1)
calculate_percent(monate2_sorted, months_percent2)


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

