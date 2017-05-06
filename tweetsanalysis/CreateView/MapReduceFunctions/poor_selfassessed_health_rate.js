//db: dataset_self_assessed_health
//design_doc: health_analysis
//view: poor_selfassessed_health_rate
//purpose: return the rate of poor self assessed health of each suburb


function (doc) {
  if(doc.properties.poor_hlth_me_3_rrmse_3_11_7_13){
    emit(doc.properties.poor_hlth_me_2_rate_3_11_7_13, doc.properties.area_name);
  }
}