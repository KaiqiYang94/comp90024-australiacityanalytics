function (doc) {
  if(doc.properties.poor_hlth_me_3_rrmse_3_11_7_13){
    emit(doc.properties.area_name, doc.properties.poor_hlth_me_2_rate_3_11_7_13);
  }
}