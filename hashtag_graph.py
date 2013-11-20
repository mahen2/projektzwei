#!/usr/bin/env python
# encoding: utf-8
# a bar plot with errorbars
# quelle: http://matplotlib.org/examples/units/bar_unit_demo.html 
import numpy as np
import matplotlib.pyplot as plt
import read_tweets_from_csv

datei = raw_input("Dateinamen angeben: ")

(hashtag1_sorted, mentions1_sorted, clients1_sorted, woerter1_sorted, jahre1, monate1, tage1) = read_tweets_from_csv.analyse_tweets(datei)
username = datei.split("_tweets.csv")[0]


N = 10 

h_values = []
h_keys = []
for key, value in hashtag1_sorted:
    h_values.append(value)
    h_keys.append(key)


menMeans = h_values[-10:]

ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars

fig, ax = plt.subplots()
try:
    rects1 = ax.bar(ind, menMeans, width, color='#90ee90')
except AssertionError, e:
    exit("zu wenige Hashtags, bitte anderen User auswählen")
plt.subplots_adjust(top=0.85, bottom=0.27)
# add some
plt.xticks(rotation=50)
ax.set_ylabel('Anzahl')
ax.set_title(u"Top 10 Hashtags für " + username)
ax.set_xticks(ind+width-0.5)
ax.set_xticklabels( h_keys[-10:] )


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 0.65*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
dateiname = 'hashtags_'+username+'.png'
plt.savefig(dateiname)
try:
    import grafikupload
    grafikupload.hochladen_und_twittern(dateiname, username, "Hashtag", h_keys[-1])
except ImportError, e:
    pass
plt.show()
