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


days_percent = []

days_whole = sum(tage1.values())

#### das hab ich mal eingefügt um den besten tag zu ermitteln, könnte man bestimmt auch irgendwie einfacher machen:
tage_sorted = sorted(tage1.iteritems(), key=operator.itemgetter(1))
h_values = []
h_keys = []
for key, value in tage_sorted:
    h_values.append(value)
    if key==0:
        key_s="Monday"
    if key==1:
        key_s="Tuesday"
    if key==2:
        key_s="Wednesday"
    if key==3:
        key_s="Thursday"
    if key==4:
        key_s="Friday"
    if key==5:
        key_s="Saturday"
    if key==6:
        key_s="Sunday"
    
    h_keys.append(key_s)
####


for key, value in tage1.iteritems():
    value_percent = 100 * float(value)/float(days_whole)
    days_percent.append(value_percent)


labels='Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
sizes=days_percent
colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'white','red']
explode=(0, 0, 0, 0, 0, 0, 0) # explode nothing for now
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.axis('equal')
dateiname = 'weekdays_'+username+'.png'
plt.savefig(dateiname)
try:
    import grafikupload
    grafikupload.hochladen_und_twittern(dateiname, username, "Wochentag", h_keys[-1])
except ImportError, e:
    pass

plt.show()
