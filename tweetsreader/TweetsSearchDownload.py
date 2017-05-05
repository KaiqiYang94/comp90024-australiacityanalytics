# Import the necessary methods from tweepy library

import tweepy
import time
import json
from couchdb import Server

# for local test
# server = Server()
# for run on vm
server = Server('http://admin:password@127.0.0.1:5984/')

try:
    db_tweets = server['tweets']
except:
    db_tweets = server.create('tweets')

# Variables that contains the user credentials to access Twitter API (Yanqin)
access_token = "856673412072091648-3B7tkrrsmMARPyGFD25H31uVR2P5naq"
access_token_secret = "rDE3att6LX6vDAAdsAbc5e7toE3G2a6w18aA7DMDQ385y"
consumer_key = "ktJymnkvujzf0rMeQlqLNnY0H"
consumer_secret = "dMMSrwi2Us179Ta80e9KOrs7LGwQ17P3LwM9Jx4KCPgCnPXNuv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Geobox of Melbourne, AU. Source: http://boundingbox.klokantech.com/
GEOBOX_MEL = [144.5937, -38.4339, 145.5125, -37.5113]

# Put your search term
# searchquery = "*"

contents = tweepy.Cursor(api.search, q="*",
                         geocode="-37.9726,145.0531,66km", lang="en").items()

count = 0
errorCount = 0


while True:
    try:
        content = next(contents)
        count += 1
        # use count-break during dev to avoid twitter restrictions
        # if (count>10):
        #    break
    except tweepy.TweepError:
        # catches TweepError when rate limiting occurs, sleeps, then restarts.
        # nominally 15 minnutes, make a bit longer to avoid attention.
        print "sleeping...."
        time.sleep(60 * 16)
        content = next(contents)
    except StopIteration:
        break
    try:
        print "Writing to JSON tweet number:" + str(count)
        # json.dump(content._json,file,sort_keys = True,indent = 4)

        njson = json.dumps(content._json, ensure_ascii=False)
        doc = json.loads(njson)
        nid = doc['id_str']

        if nid in db_tweets:
            print('--------already have----------------')

        else:
            ntext = doc['text']
            ncoordinates = doc['coordinates']
            nuser = doc['user']
            ntime = doc['created_at']
            nplace = doc['place']
            nentities = doc['entities']
            ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
                    'coordinates': ncoordinates, 'create_time': ntime,
                    'place': nplace, 'entities': nentities,
                    'addressed': False}
            db_tweets.save(ndoc)
            print(nid)
            print('-------------------------------------')

    except UnicodeEncodeError:
        errorCount += 1
        print "UnicodeEncodeError,errorCount =" + str(errorCount)
