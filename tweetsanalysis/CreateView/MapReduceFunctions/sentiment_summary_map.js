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
//purpose: return number of positive/negative stweets of each suburb


//map function
function (doc) {
  if(doc.addressed){
    emit([doc.suburb, doc.sentiment], 1);
  }
}