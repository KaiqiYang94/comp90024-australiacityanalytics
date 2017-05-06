//db: tweets
//design_doc: tweets_analysis
//view: sentiment_summary
//purpose: return number of positive/negative stweets of each suburb

//Reduce function
function (keys, value, reduce) {
  return sum(value)
}