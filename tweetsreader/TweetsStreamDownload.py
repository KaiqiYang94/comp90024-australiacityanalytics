# import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from couchdb import Server
import json

# for local test
#server = Server()
# for run on vm
server = Server('http://admin:password@127.0.0.1:5984/')

try:
    db = server['tweets']
except:
    db = server.create('tweets')

# Variables that contains the user credentials to access Twitter API
access_token = "546643485-WaT1mm4EwJe2RrnxMk5xfNxiUxnvfHc3HQgk6jFO"
access_token_secret = "GbaChVqU98h8NpUQ1FzfSG2AonWFBVdtalv5d9LNDfUrU"
consumer_key = "Orgmlwvc3OVi8UtyB1Idk1ArM"
consumer_secret = "GItv17P5pNOqtf2eRnjpfTTyuveo4LoCHUw4OZz3HJtEOo7i7p"

# Geobox of Melbourne, AU. Source: http://boundingbox.klokantech.com/
GEOBOX_MEL = [144.5937, -38.4339, 145.5125, -37.5113]


class ReaderListener(StreamListener):

    def on_data(self, data):
        try:

            doc = json.loads(data)
            nid = doc["id_str"]

            if nid in db:
                print('--------already have----------------')
                return True
            else:
                ntext = doc['text']
                ncoordinates = doc['coordinates']
                nuser = doc['user']
                ntime = doc['created_at']
                nplace = doc['place']
                ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
                        'coordinates': ncoordinates, 'create_time': ntime,
                        'place': nplace, 'addressed': False}
                db.save(ndoc)
                print(nid)
                print('-------------------------------------')
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))

        return True

    def on_error(self, status):
        print(status)
        return True


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter
    # Streaming API
    listener = ReaderListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    # This line filter Twitter Streams to capture data by the keywords: '.',
    # almost all tweets
    stream.filter(locations=GEOBOX_MEL, languages=["en"])
