#!/usr/bin/env python
# encoding: utf-8
# sort dictionary quelle: http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value
# remove punctuation: http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python

import csv, operator, stopwords, unicodedata, string

from datetime import datetime

exclude = "?!-.,;" # satzzeichen die weggefiltert werden sollen
table = string.maketrans("","")

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
    
    date_list1     = []
    hashtag_list1  = []
    woerter_list1  = []
    mentions_list1 = []
    client_list1   = []

    for tweetlist in all_tweets:
        feldindex=0
        for feld in tweetlist:
            feldindex+=1
            print feld
            if feldindex == 2: # das zweite feld in der csv enthält das datum
                date_list1.append(datetime.strptime(feld, date_format)) # liste mit datetime-objekten
            if feldindex == 3: # das dritte feld enthält den text (das vierte übrigens den client)
                for wort in feld.split():
                    if wort.lower() not in stopwords.stopwords_liste:
                        if wort.startswith("#"):
                            hashtag_list1.append(wort.lower().translate(table, exclude))
                        elif wort.startswith("@"):
                            if(wort.endswith(":")):
                                wort = wort[:-1] # viele mentions hören mit nem doppelpunkt auf, deshalb entfernen
                            if wort.lower() != "@"+csv_file.split("_tweets.csv")[0]: #eigenen namen nicht aufnehmen
                                mentions_list1.append(wort.lower().translate(table, exclude))
                        else:
                            woerter_list1.append(wort.lower().translate(table, exclude))
            if feldindex == 4:
                client_list1.append(feld)
                
        print "\n"

    # definiere jeweils ein dictionary und eine liste für jede angabe:
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
        tage1_list.append(d.weekday()) # füge tage zur liste hinzu
        monate1_list.append(d.strftime("%Y-%m")) # füge monate zur liste hinzu
        jahre1_list.append(d.strftime("%Y")) #füge jahre zur liste hinzu
        


    for j in jahre1:
        jahre1[j] = jahre1_list.count(j) # füge für jedes jahr die anzahl hinzu, wie oft das jahr vorkommt (die jahresliste wird gezählt)

    for m in monate1:
        monate1[m] = monate1_list.count(m) # vgl jahre
    
    for t in tage1:
        tage1[t] = tage1_list.count(t) # vgl jahre
    
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
        hashtag1[unicode(hashtag, "utf-8")] = hashtag_list1.count(hashtag) # ähnlich wie bei den datumsangaben: zähle auftreten in der liste und speicher wert in dict
    
    woerter1 = {}
    for wort in woerter_list1:
        woerter1[unicode(wort, "utf-8")] = woerter_list1.count(wort)
        
    
    mentions1 = {}
    for mention in mentions_list1:
        mentions1[unicode(mention, "utf8")] = mentions_list1.count(mention)
        
    clients1 = {}
    for client in client_list1:
        clients1[unicode(client, "utf8")] = client_list1.count(client)
    
    woerter1_sorted = sorted(woerter1.iteritems(), key=operator.itemgetter(1))
    hashtag1_sorted = sorted(hashtag1.iteritems(), key=operator.itemgetter(1))
    mentions1_sorted = sorted(mentions1.iteritems(), key=operator.itemgetter(1))
    clients1_sorted = sorted(clients1.iteritems(), key=operator.itemgetter(1))
    print "\n\n--- Hashtaganalyse der Tweets (Schwelle: mindestens 10 mal verwendet)  ---\n\n"


    for tup in hashtag1_sorted:
        if tup[1]>10:
            print tup[0] + ": " + str(tup[1]) + " mal"
    
    print "\n\n--- Wörteranalyse der Tweets (Schwelle: mindestens 10 mal verwendet)  ---\n\n"
    
            
    for wor in woerter1_sorted:
        if wor[1]>10:
            print wor[0] + ": " + str(wor[1]) + " mal"
            
            
    print "\n\n--- Mentionsanalyse der Tweets (Schwelle: mindestens 10 mal verwendet)  ---\n\n"
    
    for mention in mentions1_sorted:
        if mention[1]>10:
            print mention[0] + ": " + str(mention[1]) + " mal"
            
    print "\n\n--- Clientanalyse der Tweets (Schwelle: mindestens 10 mal verwendet)  ---\n\n"

    for client in clients1_sorted:
        if client[1]>0:
            print client[0] + ": " + str(client[1]) + " mal"
    
    
    return(hashtag1_sorted, mentions1_sorted, clients1_sorted, woerter1_sorted, jahre1, monate1, tage1) # return alle dicts

if __name__ == "__main__":

    analyse_tweets(csv_file)


 