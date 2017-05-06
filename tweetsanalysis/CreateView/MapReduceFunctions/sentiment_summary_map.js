//db: tweets
//design_doc: tweets_analysis
//view: sentiment_summary
//purpose: return number of positive/negative stweets of each suburb


//map function
function (doc) {
  if(doc.addressed){
    emit([doc.suburb, doc.sentiment], 1);
  }
}