function (doc) {
  if(doc.addressed){
    topics = ['Trump', 'Donald'];
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
  
  //try to find from meaning cloud topics
  var tweet_topics = JSON.parse(doc.topics);
  topics.forEach(function(t){
    for(var tt : tweet_topics){
      if(tt.toLowerCase() === t){
        hasTopic = true;
      }
    }
  });
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
  
  return hasTopic;
}



function (doc) {
  if(doc.addressed){
    topics = ['Trump', 'Donald'];
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
	  //try to find from meaning cloud topics
  if(doc.topics){
    var tweet_topics = doc.topics;
    topics.forEach(function(t){
      for(var tt : tweet_topics){
        if(tt.toLowerCase() === t){
          hasTopic = true;
        }
      }
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
        
  return hasTopic;
}