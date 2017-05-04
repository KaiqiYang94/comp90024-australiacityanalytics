function (doc) {
  var percent = 
    doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_80_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_90_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_100_synthetic_estimates
    
    emit(doc.properties.sa2_name11, percent)
}