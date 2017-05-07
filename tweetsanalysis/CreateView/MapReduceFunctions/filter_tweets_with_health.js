function (doc) {
  if(doc.addressed){
    topics = ['health', 'body', 'energy', 'fitness','ache','acne','aleve','ankle','allergy','anxiety','antibiotics',
              'appetite','aspirin','asthma','arthrities','backache','bedtime','benadryl','burised','burning','anxious',
              'caffeine','cancer','colds','cough','contagious','congestion','cure','cured','dealing','dehydrated','dental',
              'depression','diabetes','dieting','dizzy','dizziness','doctor','dose','drained','earache','elbow','emergency',
              'exercise','exhausted','excesdrin','faint','fatigue','fever','flu','fluids','h1n1','germs','heal','headaches',
              'heal','healed','hearthurn','hiccups','hives','hospital','hungover','hurtin','hurts','hurting','ibuprofen',
              'ick','ill','illness','infected','infection','inhaler','insomnia','intense','irritated','insurance','itch',
              'itching','jaw','kidney','killing','knee','lasik','limping','lump','lung','lungs','massage','medication','medicine',
              'meds','mri','muscles','nasal','neck','nose','nurse','nyquil','ouch','pain','painkiller','pains','panadol','paracetamol',
              'physical','physically','pill','pills','pneumonia','pollen','prescription','puffy','rash','recover','recovered',
              'recovering','rehab','remedies','remedy','respiratory','resting','rest','runny','scratchy','sick','sicker','sickness',
              'sneeze','sneezed','sniffles','snot','sore','spasms','spine','sprain','steroids','stomache','stomachache','strep',
              'stroke','stuffy','funburn','surgeon','surgery','swelling','swollen','symptoms','tension','throat','throats','throbbing',
              'thyroid','tiredness','tissues','tonsillitis','tonsils','tooth','toothache','torn','treatment','tumor','tylenol','ugh',
              'ulcer','unbearable','uncomfortable','unwell','vaccine','veins','vertigo','vicodin','viral','vision','vitamins','vomit',
              'vomiting','wheezing','wrist'];
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