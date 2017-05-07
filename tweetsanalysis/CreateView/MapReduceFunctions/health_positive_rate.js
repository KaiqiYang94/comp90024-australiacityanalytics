function (doc) {
  emit(doc.health_positive_rate, doc._id);
}