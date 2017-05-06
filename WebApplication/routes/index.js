var express = require('express');
var router = express.Router();
var request = require('request');


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Australia City Analytics' });
});

router.get('/scenarios', function(req, res, next) {
  var suburbs = []
  var scores = []
  var content_url1 = 'http://admin:password@127.0.0.1:5984/dataset_life_satisfaction/_design/life_satisfacation_summary/_view/avg_satisfacation?limit=10;descending=True'
  //res.render('scenarios', { title:'Content', msg: content});
  request(content_url1, function(error, response, body){
        //Error Handling
     if(!error && response.statusCode == 200){
            
            console.log("-----------")
            var obj = JSON.parse(body)
            
            for(var row in obj['rows']){
              var score = obj['rows'][row]['key'];
             
              var suburb = obj['rows'][row]['value'];
              scores.push(score);
              suburbs.push(suburb);

            }
            res.render('scenarios', {title: 'scenarios', suburbs: JSON.stringify(suburbs), scores: JSON.stringify(scores)});
        } else {
            res.render('scenarios', {title: JSON.stringify(error)});
            console.log("wrong");
        }
    });



 
});

router.get('/scenarios/ieo', function(req, res, next) {
  
 res.render('ieo', { title: 'IEO' });
});


router.get('/scenarios/ier', function(req, res, next) {
  
 res.render('ier', { title: 'IER' });
});


router.get('/scenarios/health', function(req, res, next) {
  
 res.render('health', { title: 'Health' });
});


router.get('/scenarios/volunteer', function(req, res, next) {
  
 res.render('volunteer', { title: 'volunteer' });
});

router.get('/mapdemo', function(req, res, next) {
  res.render('mapdemo', {});
});

module.exports = router;
 