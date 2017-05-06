//db: dataset_community_strength
//design_doc: voluntary_work_analysis
//view: voluntary_work_rate
//purpose: return the rate of doing voluntary work of each suburb

function (doc) {
  emit(doc.properties.volun_abs_3_percent_6_11_6_11, doc.properties.area_name);
}