//db: dataset_ier
//design_doc: ier_analysis
//view: wealth_score
//purpose: return the economic resources score of each suburb

function (doc) {
  emit(doc.properties.score, doc.properties.sa2_name);
}