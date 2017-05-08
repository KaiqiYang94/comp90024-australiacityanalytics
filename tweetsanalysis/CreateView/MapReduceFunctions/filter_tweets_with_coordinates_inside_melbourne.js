//db: tweets
//design_doc: tweets_analysis
//view: filter_tweets_with_coordinates_inside_melbourne
//purpose: filter tweets with coordinates inside melbourne


function (doc) {
  if(!doc.addressed && doc.coordinates){
    if(doc.coordinates.coordinates){
	  lon = doc.coordinates.coordinates[0];
	  lat = doc.coordinates.coordinates[1];
    }else{
      lon = doc.coordinates[0];
      lat = doc.coordinates[1];
    }
    if(insideMelbourne(lat,lon)){
      emit(doc._id, [[lon, lat], doc.text]);
    }
  }
}

function insideMelbourne(lat, lon){
  //melbourne bondingbox
  //[[[144.5937418,-38.4338593],[145.5125288,-38.4338593],[145.5125288,-37.5112737],[144.5937418,-37.5112737],[144.5937418,-38.4338593]]]
  if(lon>=144.5937418 && lon<=145.5125288
      &&lat>=-38.4338593 && lat<=-37.5112737){
      return true;
  }else{
    return false;
  }
}