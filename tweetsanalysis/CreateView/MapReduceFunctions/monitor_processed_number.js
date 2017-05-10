function (doc) {
  if(doc.addressed){
    emit(doc._id, 1)
  }
}

