// -------------------------------
// Team 24
// Kaiqi Yang 729687
// Xing Hu 733203
// Ziyuan Wang 735953
// Chi Che 823488
// Yanqin Jin 787723
// -------------------------------

//db: dataset_ier
//design_doc: ier_analysis
//view: wealth_score
//purpose: return the economic resources score of each suburb

function (doc) {
  emit(doc.properties.score, doc.properties.sa2_name);
}