//map function
function (doc) {
  if(doc.addressed){
    emit([doc.suburb, doc.sentiment], 1);
  }
}

//Reduce function
function (keys, value, reduce) {
  return sum(value)
}