#!/usr/bin/env python
# encoding: utf-8

import csv

from datetime import datetime

csv_file = raw_input("Welche Datei soll geöffnet werden?\nDateiname: ")
all_tweets = []
with open(csv_file, 'rb') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        all_tweets.append(row)
        
        
# all_tweets ist ne liste mit allen tweets, die gerade eingelesen wurden 

date_format = "%Y-%m-%d %H:%M:%S"
date_list1 = []

for tweetlist in all_tweets:
    feldindex=0
    for feld in tweetlist:
        feldindex+=1
        print feld
        if feldindex == 2: # das zweite feld in der csv enthält das datum
            date_list1.append(datetime.strptime(feld, date_format)) # liste mit datetime-objekten
    print "\n"

tage1 = {}
monate1 = {}
jahre1 = {}
tage1_list = []
monate1_list = []
jahre1_list = []

for d in date_list1:
    tage1[d.weekday()]=''
    
    monate1[d.strftime("%Y-%m")]=''
    jahre1[d.strftime("%Y")]=''
    tage1_list.append(d.weekday())
    monate1_list.append(d.strftime("%Y-%m"))
    jahre1_list.append(d.strftime("%Y"))
        


for j in jahre1:
    jahre1[j] = jahre1_list.count(j)

for m in monate1:
    monate1[m] = monate1_list.count(m)
    
for t in tage1:
    tage1[t] = tage1_list.count(t)
    
print "\n"

for key in jahre1:
    print "Im Jahr " + str(key) + ": " + str(jahre1[key]) + " Tweets"

print "\n"

for key in monate1:
    print "Im Monat " + str(key) + ": " + str(monate1[key]) + " Tweets"
    
print "\n"

for key in tage1:
    if key==0:
        print "montags: "  + str(tage1[key]) + " Tweets"
    if key==1:
        print "dienstags: "  + str(tage1[key]) + " Tweets"
    if key==2:
        print "mittwochs: "  + str(tage1[key]) + " Tweets"
    if key==3:
        print "donnerstags: "  + str(tage1[key]) + " Tweets"
    if key==4:
        print "freitags: "  + str(tage1[key]) + " Tweets"
    if key==5:
        print "samstags: "  + str(tage1[key]) + " Tweets"
    if key==6:
        print "sonntags: "  + str(tage1[key]) + " Tweets"
        