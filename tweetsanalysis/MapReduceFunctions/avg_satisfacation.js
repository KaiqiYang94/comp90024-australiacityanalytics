function (doc) {
  var avg_satisfacation = 
    doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_10_synthetic_estimates * 0.01 * 10
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_20_synthetic_estimates * 0.01 * 20
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_30_synthetic_estimates * 0.01 * 30
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_40_synthetic_estimates * 0.01 * 40
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_50_synthetic_estimates * 0.01 * 50
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_60_synthetic_estimates * 0.01 * 60
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_70_synthetic_estimates * 0.01 * 70
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_80_synthetic_estimates * 0.01 * 80
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_90_synthetic_estimates * 0.01 * 90
    + doc.properties.proportion_percent_among_aged_17plus_on_life_satisfaction_scale_at_100_synthetic_estimates * 0.01 * 100
    
    emit(doc.properties.sa2_name11, avg_satisfacation);
}