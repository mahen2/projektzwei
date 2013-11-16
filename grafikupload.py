# encoding: utf-8
# quelle: http://stackoverflow.com/questions/432385/sftp-in-python-platform-independent
import paramiko, geheim, tweepy
consumer_key = geheim.consumer_key
consumer_secret = geheim.consumer_secret
access_key = geheim.access_key
access_secret = geheim.access_secret


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def hochladen_und_twittern(dateiname, username, typ, topwert=None):
    print "lade " + dateiname + " hoch" 
    host = "columba.uberspace.de"                    
    port = 22
    transport = paramiko.Transport((host, port))

    password_sftp = geheim.password_sftp             
    username_sftp = geheim.username_sftp             
    transport.connect(username = username_sftp, password = password_sftp)

    sftp = paramiko.SFTPClient.from_transport(transport)

    import sys
    path = './html/' + dateiname   
    localpath = dateiname
    sftp.put(localpath, path)

    sftp.close()
    transport.close()
    print 'Upload done.'
    # man kann auch noch ein @ vor den usernamen setzen aber dann wird evtl. der account suspended:
    statusstring = typ+"-Auswertung von "+username+": "+topwert+" auf Platz 1. Mehr unter: http://projekt2.columba.uberspace.de/" + dateiname
    print statusstring
    api.update_status(statusstring)
    
