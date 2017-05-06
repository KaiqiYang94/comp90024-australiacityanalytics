var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Australia City Analytics' });
});

router.get('/scenarios', function(req, res, next) {
  
  //var content_url = 'http://admin:password@127.0.0.1:5984/dataset_ier/seifa_ier_aust_sa2.fid-6ec8c59a_15bc3c26fba_6344'
  var content_url = 'http://admin:password@127.0.0.1:5984/dataset_ieo/_design/ieo_analysis/_view/ieo_score?limit=10;descending=True'
  //res.render('scenarios', { title:'Content', msg: content});
  request(content_url, function(error, response, body){
        //Error Handling
     if(!error && response.statusCode == 200){
            console.log(body);
            
            res.render('scenarios', {title: 'scenarios', msg: body});
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
 