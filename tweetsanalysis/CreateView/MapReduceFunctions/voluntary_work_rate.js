// -------------------------------
// Team 24
// Kaiqi Yang 729687
// Xing Hu 733203
// Ziyuan Wang 735953
// Chi Che 823488
// Yanqin Jin 787723
// -------------------------------

//db: dataset_community_strength
//design_doc: voluntary_work_analysis
//view: voluntary_work_rate
//purpose: return the rate of doing voluntary work of each suburb

function (doc) {
  emit(doc.properties.volun_abs_3_percent_6_11_6_11, doc.properties.area_name);
}