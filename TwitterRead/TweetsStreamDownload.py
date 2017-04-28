#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from couchdb import Server
import couchdb
import json

remote_server = Server()
db = remote_server['stream_tweets']

#Variables that contains the user credentials to access Twitter API 
access_token = "546643485-WaT1mm4EwJe2RrnxMk5xfNxiUxnvfHc3HQgk6jFO"
access_token_secret = "GbaChVqU98h8NpUQ1FzfSG2AonWFBVdtalv5d9LNDfUrU"
consumer_key = "Orgmlwvc3OVi8UtyB1Idk1ArM"
consumer_secret = "GItv17P5pNOqtf2eRnjpfTTyuveo4LoCHUw4OZz3HJtEOo7i7p"


class ReaderListener(StreamListener):


    def on_data(self, data):
        try:
           # with open(self.outfile, 'a') as f:
            #    f.write(data)
             #   print(data)
                
           
            doc = json.loads(data)
       
            nid = doc["id_str"]
     
            ntext = doc['text']
  
            ncoordinates = doc['coordinates']
            nuser = doc['user']
            ntime = doc['created_at']
            nplace = doc['place']
           # nid = content._json.u'id'
            ndoc={'_id':nid,'text':ntext, 'user':nuser, 'coordinates':ncoordinates, 'create_time':ntime,'place':nplace,'addressed':False}
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

#This handles Twitter authetification and the connection to Twitter Streaming API
    l = ReaderListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: '.', almost all tweets
    stream.filter(track=["Trump","Donald Trump","President Trump"],languages=["en"])