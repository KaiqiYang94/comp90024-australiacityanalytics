function (doc) {
  if(!doc.addressed && doc.coordinates){
    lon = doc.coordinates.coordinates[0];
    lat = doc.coordinates.coordinates[1];
    if(insideMelbourne(lat,lon)){
      emit(doc._id, doc);
    }
  }
}

function insideMelbourne(lat, lon){
  //melbourne bondingbox
  //[[[144.5937418,-38.4338593],[145.5125288,-38.4338593],[145.5125288,-37.5112737],[144.5937418,-37.5112737],[144.5937418,-38.4338593]]]
  if(lon>=144.5937418 && lon<=145.5125288,-38.4338593
      &&lat>=-38.4338593 && lat<=-37.5112737){
      return true;
  }else{
    return false;
  }
}