 // -------------------------------
 // Team 24
 // Kaiqi Yang 729687
 // Xing Hu 733203
 // Ziyuan Wang 735953
 // Chi Che 823488
 // Yanqin Jin 787723
 // -------------------------------

var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

module.exports = router;
