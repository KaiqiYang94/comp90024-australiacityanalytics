//db: tweets
//design_doc: tweets_analysis
//view: sentiment_summary
//purpose: reduce method for sentiment_summary, vulgar_words, trump_topic

//Reduce function
function (keys, value, reduce) {
  return sum(value)
}