#!/usr/bin/env python
# encoding: utf-8
# sort dictionary quelle: http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value

import csv, operator

from datetime import datetime

if __name__ == "__main__":
    csv_file = raw_input("Welche Datei soll geöffnet werden?\nDateiname: ")
        
        
# all_tweets ist ne liste mit allen tweets, die gerade eingelesen wurden 
def analyse_tweets(csv_file):
    all_tweets = []
    with open(csv_file, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            all_tweets.append(row) #zweidimensionale liste
    
    date_format = "%Y-%m-%d %H:%M:%S"
    date_list1 = []
    hashtag_list1 = []

    for tweetlist in all_tweets:
        feldindex=0
        for feld in tweetlist:
            feldindex+=1
            print feld
            if feldindex == 2: # das zweite feld in der csv enthält das datum
                date_list1.append(datetime.strptime(feld, date_format)) # liste mit datetime-objekten
            if feldindex == 3: # das dritte feld enthaelt den text (das vierte uebrigens den client)
                for hashtag in feld.split():
                    if hashtag.startswith("#"):
                        hashtag_list1.append(hashtag)
        print "\n"

    # definiere jeweils ein dictionary und eine liste fuer jede angabe:
    tage1 = {}
    monate1 = {}
    jahre1 = {}
    tage1_list = []
    monate1_list = []
    jahre1_list = []

    print "\n\n--- Datumsanalyse der Tweets  ---\n\n"

    for d in date_list1: # gehe alle datetime-objekte durch
        tage1[d.weekday()]=''
    
        monate1[d.strftime("%Y-%m")]='' # dictionary mit monaten (wird evtl mehrmals auf einen leeren string gesetzt, aber das ist egal)
        jahre1[d.strftime("%Y")]='' #dictionary mit jahren
        tage1_list.append(d.weekday()) # fuege tage zur liste hinzu
        monate1_list.append(d.strftime("%Y-%m")) # fuege monate zur liste hinzu
        jahre1_list.append(d.strftime("%Y")) #fuege jahre zur liste hinzu
        


    for j in jahre1:
        jahre1[j] = jahre1_list.count(j) # fuege fuer jedes jahr die anzahl hinzu, wie oft das jahr vorkommt (die jahresliste wird gezaehlt)

    for m in monate1:
        monate1[m] = monate1_list.count(m) # vgl jahre
    
    for t in tage1:
        tage1[t] = tage1_list.count(t) vgl jahre
    
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

    hashtag1 = {}
    for hashtag in hashtag_list1:
        hashtag1[hashtag] = hashtag_list1.count(hashtag) # aehnlich wie bei den datumsangaben: zaehle auftreten in der liste und speicher wert in dict


    hashtag1_sorted = sorted(hashtag1.iteritems(), key=operator.itemgetter(1))

    print "\n\n--- Hashtaganalyse der Tweets (Schwelle: mindestens 10 mal verwendet)  ---\n\n"


    for tup in hashtag1_sorted:
        if tup[1]>10:
            print tup[0] + ": " + str(tup[1]) + " mal"
    
    return(hashtag1_sorted, jahre1, monate1, tage1) # return alle 4 dicts

if __name__ == "__main__":

    analyse_tweets(csv_file)


 