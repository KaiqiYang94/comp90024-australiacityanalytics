//db: dataset_ieo
//design_doc: ieo_analysis
//view: ieo_score
//purpose: return the education/ocupation score of each suburb

function (doc) {
  emit(doc.properties.score, doc.properties.sa2_name);
}