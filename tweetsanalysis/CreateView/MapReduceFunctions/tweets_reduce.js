// -------------------------------
// Team 24
// Kaiqi Yang 729687
// Xing Hu 733203
// Ziyuan Wang 735953
// Chi Che 823488
// Yanqin Jin 787723
// -------------------------------

//db: tweets
//design_doc: tweets_analysis
//view: sentiment_summary
//purpose: reduce method for sentiment_summary, vulgar_words, trump_topic

//Reduce function
function (keys, value, reduce) {
  return sum(value)
}