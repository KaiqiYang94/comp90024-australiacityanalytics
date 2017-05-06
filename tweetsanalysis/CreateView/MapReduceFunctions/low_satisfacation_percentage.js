//db: dataset_life_satisfaction
//design_doc name: life_satisfacation_summary
//view name: low_satisfacation_percentage
//purpose: return the percentage of low life satisfaction of each suburb


function (doc) {
  var percent = 
    doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_0_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_10_synthetic_estimates
    +doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_20_synthetic_estimates
    
    emit(percent, doc.properties.sa2_name11)
}