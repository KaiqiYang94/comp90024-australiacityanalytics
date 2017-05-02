function (doc) {
  var vulgarWords = ['asshole', 'badass','bastard','bitch','bullshit','cock','cunt','dick','dickhead','fag','faggot','fart','fatass',
  'fuck','fuck up','fucked','fucker','fucking','greek','holy shit','jackass','jerk off','kick ass','kike','nigga','nigger','piss','pissed','pissed off',
  'shit','shitty','son of a bitch','shittier','twat','wank'];
  
  if(doc.addressed){
    text = doc.text.toLowerCase();
    vulgarWords.forEach(function(vw){
      if(text.indexOf(vw)>-1){
        emit([doc.suburb, doc.sentiment], 1);
      }
    });
  }
}