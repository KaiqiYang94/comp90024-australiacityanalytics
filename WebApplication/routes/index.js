var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Australia City Analytics' });
});

router.get('/scenarios', function(req, res, next) {

	
  res.render('scenarios', { });
});

router.get('/mapdemo', function(req, res, next) {
  res.render('mapdemo', {title: 'IEO' });
});

module.exports = router;
