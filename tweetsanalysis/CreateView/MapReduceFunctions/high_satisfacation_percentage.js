//db: dataset_life_satisfaction
//design_doc name: life_satisfacation_summary
//view name: high_satisfacation_percentage
//purpose: return the percentage of high life satisfaction of each suburb

function (doc) {
  var percent = 
    doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_80_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_90_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_100_synthetic_estimates
    
    emit(percent, doc.properties.sa2_name11)
}