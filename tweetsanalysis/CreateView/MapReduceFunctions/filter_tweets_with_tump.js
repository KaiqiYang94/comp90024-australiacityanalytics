//db: tweets
//design_doc: tweets_analysis
//view: filter_tweets_with_trump
//purpose: filter processed tweets with topic trump


function (doc) {
  if(doc.addressed){
    topics = ['trump', 'donald'];
    var hasTopics = findTopics(topics, doc);
    if(hasTopics){
      emit([doc.suburb, doc.sentiment], 1);
    }
  }
}

function findTopics(topics, doc){
  var hasTopic = false;
  //try to find from tweet text
  var tweet = doc.text.toLowerCase();
  tweet_words = tweet.split(" ")
	topics.forEach(function(t){
		if (tweet_words.indexOf(t) > -1){
			hasTopic = true;
		}
	});
	
	//try to find from meaningcloud topics
	if(doc.topics){
	  var tweet_topics = doc.topics;
	  tweet_topics.forEach(function(tt){
	    topics.forEach(function(t){
	      if (tt.toLowerCase() == t){
	        hasTopic = true;
	      }
	    })
	  });
  }
  
  //try to find from hashtags
  if(doc.entities){
    if(doc.entities.hashtags){
      doc.entities.hashtags.forEach(function(hashtag){
        topics.forEach(function(t){
          if((hashtag.text).toLowerCase() == t){
            hasTopic = true;
          }
        });
      });
    }
  }
  
  return hasTopic;
}