 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
# import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from couchdb import Server
import json

# for local test
# server = Server()
# for run on vm
server = Server('http://admin:password@127.0.0.1:5984/')

try:
    db = server['tweets']
except:
    db = server.create('tweets')

# Variables that contains the user credentials to access Twitter API(Ziyuan)
access_token = "760698710393323522-B7ns3t8JIvMUynVvZauGjbwmCj0cNtq"
access_token_secret = "VuKvKaD41lzsNVEh1K0cI9gTOUn5r6J7f9znfge9teJOd"
consumer_key = "Kym8TFa2vzh9qrM3dIhGLykkt"
consumer_secret = "UyLmcO29KeWXwyoiuHH4FXOSydEmaIcGBNmXIWkjxpwpV4M2Ec"

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
                nentities = doc['entities']
                ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
                        'coordinates': ncoordinates, 'create_time': ntime,
                        'place': nplace, 'entities': nentities,
                        'addressed': False}
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
