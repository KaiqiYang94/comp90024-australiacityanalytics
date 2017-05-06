var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Australia City Analytics' });
});

router.get('/scenarios', function(req, res, next) {
  
  var content_url = 'http://admin:password@127.0.0.1:5984/dataset_ier/seifa_ier_aust_sa2.fid-6ec8c59a_15bc3c26fba_6344'
  
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


router.get('/mapdemo', function(req, res, next) {
  res.render('mapdemo', {title: 'IEO' });
});

module.exports = router;
 