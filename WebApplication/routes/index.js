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
    var suburbs_avg = []
    var scores_avg = []
    var suburbs_high = []
    var scores_high = []
    var suburbs_low = []
    var scores_low = []
    var suburb_tweets = []
    var scores_tweets = []

    var aurin_avg_url = 'http://admin:password@127.0.0.1:5984/dataset_life_satisfaction/_design/life_satisfacation_summary/_view/avg_satisfacation?limit=10;descending=True'
    var aurin_high_url = 'http://admin:password@127.0.0.1:5984/dataset_life_satisfaction/_design/life_satisfacation_summary/_view/high_satisfacation_percentage?limit=10;descending=True'
    var aurin_low_url = 'http://admin:password@127.0.0.1:5984/dataset_life_satisfaction/_design/life_satisfacation_summary/_view/low_satisfacation_percentage?limit=10;descending=True'

    var tweets_url = 'http://admin:password@127.0.0.1:5984/tweets_summary/_design/tweets_summary/_view/positive_rate?limit=10;descending=True'

    // read 1
    rp(aurin_avg_url)
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburbs_avg.push(suburb);
                scores_avg.push(score);
            }
            // read 2
            return rp(aurin_high_url)
        })
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburbs_high.push(suburb);
                scores_high.push(score);
            }

            // read 3'
            return rp(aurin_low_url)
        })
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburbs_low.push(suburb);
                scores_low.push(score);
            }
            // read 4        
            return rp(tweets_url)
        })
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburb_tweets.push(suburb);
                scores_tweets.push(score);
            }
            res.render('scenarios', {
                chart1: 'AURIN- TOP 10 Cities of highest Life Satisfaction (Average)',
                suburbs_avg: JSON.stringify(suburbs_avg),
                scores_avg: JSON.stringify(scores_avg),
                chart2: 'AURIN- TOP 10 Cities with highest Life Satisfaction (High)',
                suburbs_high: JSON.stringify(suburbs_high),
                scores_high: JSON.stringify(scores_high),
                chart3: 'AURIN- TOP 10 Cities with highest Life Satisfaction (Low)',
                suburbs_low: JSON.stringify(suburbs_low),
                scores_low: JSON.stringify(scores_low),
                chart4: 'Tweets- TOP 10 Cities with positive tweets',
                suburb_tweets: JSON.stringify(suburb_tweets),
                scores_tweets: JSON.stringify(scores_tweets)
            });
            return Promise.resolve();

        }).catch(function(err) { console.log("error: " + err) });


});

//for IEO page
//data need: 1. aurin- 
//           2. tweets- semantic
router.get('/scenarios/ieo', function(req, res, next) {
    var suburbs_aurin = []
    var scores_aurin = []
    var suburb_tweets = []
    var scores_tweets = []

    var aurin_url = 'http://admin:password@127.0.0.1:5984/dataset_ieo/_design/ieo_analysis/_view/ieo_score?limit=10;descending=True'
    var tweets_url = 'http://admin:password@127.0.0.1:5984/tweets_summary/_design/tweets_summary/_view/positive_rate?limit=10;descending=True'

    // read 1
    rp(aurin_url)
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburbs_aurin.push(suburb);
                scores_aurin.push(score);
            }
            // read 2
            return rp(tweets_url)
        })
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburb_tweets.push(suburb);
                scores_tweets.push(score);
            }
            res.render('ieo', {
                chart1: 'AURIN- Top 10 suburbs with highest education/ocupation score',
                suburbs_aurin: JSON.stringify(suburbs_aurin),
                scores_aurin: JSON.stringify(scores_aurin),
                chart2: 'TWEETS- TOP 10 Cities with positive attitudes',
                suburb_tweets: JSON.stringify(suburb_tweets),
                scores_tweets: JSON.stringify(scores_tweets)
            });
            return Promise.resolve();

        }).catch(function(err) { console.log("error: " + err) });

});

//for IER(Wealth) page
//data need: 1. aurin- 
//           2. tweets- positive
//           3. tweets- negative
router.get('/scenarios/ier', function(req, res, next) {

    var suburbs_aurin = []
    var scores_aurin = []
    var suburb_pos_tweets = []
    var suburb_neg_tweets = []
    var scores_pos_tweets = []
    var scores_neg_tweets = []

    var aurin_url = 'http://admin:password@127.0.0.1:5984/dataset_ier/_design/ier_analysis/_view/wealth_score?limit=10;descending=True'
    var tweets_pos_url = 'http://admin:password@127.0.0.1:5984/tweets_summary/_design/tweets_summary/_view/positive_rate?limit=10;descending=True'
    var tweets_neg_url = 'http://admin:password@127.0.0.1:5984/tweets_summary/_design/tweets_summary/_view/negative_rate?limit=10;descending=True'

    // read 1
    rp(aurin_url)
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburbs_aurin.push(suburb);
                scores_aurin.push(score);
            }
            // read 2
            return rp(tweets_pos_url)
        })
        .then(function(response) {
            var obj = JSON.parse(response);
            for (var row in obj['rows']) {

                var score = obj['rows'][row]['key'];
                var suburb = obj['rows'][row]['value'];
                suburb_pos_tweets.push(suburb);
                scores_pos_tweets.push(score);
            }
            // read 2
            return rp(tweets_neg_url)
        })

    .then(function(response) {
        var obj = JSON.parse(response);
        for (var row in obj['rows']) {

            var score = obj['rows'][row]['key'];
            var suburb = obj['rows'][row]['value'];
            suburb_neg_tweets.push(suburb);
            scores_neg_tweets.push(score);
        }
        res.render('ier', {
            chart1: 'AURIN- Top 10 suburbs with highest wealth score',
            suburbs_aurin: JSON.stringify(suburbs_aurin),
            scores_aurin: JSON.stringify(scores_aurin),
            chart2: 'TWEETS- TOP 10 Cities with highest positive attitudes',
            suburb_pos_tweets: JSON.stringify(suburb_pos_tweets),
            scores_pos_tweets: JSON.stringify(scores_pos_tweets),
            chart3: 'TWEETS- TOP 10 Cities with highest negative attitudes',
            suburb_neg_tweets: JSON.stringify(suburb_neg_tweets),
            scores_neg_tweets: JSON.stringify(scores_neg_tweets)
        });
        return Promise.resolve();

    }).catch(function(err) { console.log("error: " + err) });

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

//for Trump page
//data need: 1. tweets- trump position
//           2. tweets- trump negative
router.get('/scenarios/trump', function(req, res, next) {

    res.render('trump', { title: 'trump' });
});

//Map
router.get('/mapdemo', function(req, res, next) {
    res.render('mapdemo', {});
});

module.exports = router;
