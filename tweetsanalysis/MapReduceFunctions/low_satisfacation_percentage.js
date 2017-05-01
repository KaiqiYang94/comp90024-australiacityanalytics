function (doc) {
  var percent = 
    doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_0_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_10_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_20_synthetic_estimates
    
    emit(doc.properties.sa2_name11, percent)
}