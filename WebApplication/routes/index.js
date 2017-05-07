var express = require('express');
var router = express.Router();
var request = require('request');
var rp = require('request-promise');


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Australia City Analytics' });
});

//for life satisfaction page
//data need: 1. aurin- average
//           2. aurin - high
//           3. aurin - low
//           4. tweets- semantic
router.get('/scenarios', function(req, res, next) {
  var suburbs = []
  var scores = []
  var content_url = 'http://admin:password@127.0.0.1:5984/dataset_life_satisfaction/_design/life_satisfacation_summary/_view/avg_satisfacation?limit=10;descending=True'
  //res.render('scenarios', { title:'Content', msg: content});
  request(content_url, function(error, response, body){
        //Error Handling
     if(!error && response.statusCode == 200){
            
            var obj = JSON.parse(body)
            
            for(var row in obj['rows']){
              var score = obj['rows'][row]['key'];
              var suburb = obj['rows'][row]['value'];
              suburbs.push(suburb);
              scores.push(score.toFixed(2));

            }
            res.render('scenarios', {title: 'Tweet map', suburbs: JSON.stringify(suburbs), scores: JSON.stringify(scores)});

         } else {
            res.render('scenarios', {title: JSON.stringify(error)});
            console.log("wrong");
        }
    });



 
});

//for IEO page
//data need: 1. aurin- 
//           2. tweets- semantic
router.get('/scenarios/ieo', function(req, res, next) {
  
 res.render('ieo', { title: 'IEO' });
});

//for IER(Wealth) page
//data need: 1. aurin- 
//           2. tweets- positive
//           3. tweets- negative
router.get('/scenarios/ier', function(req, res, next) {
  
 res.render('ier', { title: 'IER' });
});

//for health page
//data need: 1. aurin- 
//           2. tweets- topic
router.get('/scenarios/health', function(req, res, next) {
  
 res.render('health', { title: 'Health' });
});

//for Volunteer page
//data need: 1. aurin- 
//           2. tweets- semantic
router.get('/scenarios/volunteer', function(req, res, next) {
  
 res.render('volunteer', { title: 'volunteer' });
});

router.get('/mapdemo', function(req, res, next) {
  res.render('mapdemo', {});
});

module.exports = router;
 