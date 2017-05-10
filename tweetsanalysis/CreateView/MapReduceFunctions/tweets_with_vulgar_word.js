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
//view: tweets_with_vulgar_word
//purpose: return the numbr of tweets with vulgar_word of each suburb


function (doc) {
  var vulgarWords = ['asshole', 'badass','bastard','bitch','bullshit','cock','cunt','dick','dickhead','fag','faggot','fart','fatass',
  'fuck','fuck up','fucked','fucker','fucking','greek','holy shit','jackass','jerk off','kick ass','kike','nigga','nigger','piss','pissed','pissed off',
  'shit','shitty','son of a bitch','shittier','twat','wank'];
  
  if(doc.addressed){
    text = doc.text.toLowerCase();
    vulgarWords.forEach(function(vw){
      if(text.indexOf(vw)>-1){
        emit(doc.suburb, 1);
      }
    });
  }
}