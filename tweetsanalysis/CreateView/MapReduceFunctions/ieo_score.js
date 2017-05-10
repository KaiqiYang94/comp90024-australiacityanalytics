// -------------------------------
// Team 24
// Kaiqi Yang 729687
// Xing Hu 733203
// Ziyuan Wang 735953
// Chi Che 823488
// Yanqin Jin 787723
// -------------------------------

//db: dataset_ieo
//design_doc: ieo_analysis
//view: ieo_score
//purpose: return the education/ocupation score of each suburb

function (doc) {
  emit(doc.properties.score, doc.properties.sa2_name);
}