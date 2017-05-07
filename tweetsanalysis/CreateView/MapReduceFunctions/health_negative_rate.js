function (doc) {
  emit(doc.health_negative_rate, doc._id);
}