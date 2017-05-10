// -------------------------------
// Team 24
// Kaiqi Yang 729687
// Xing Hu 733203
// Ziyuan Wang 735953
// Chi Che 823488
// Yanqin Jin 787723
// -------------------------------

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