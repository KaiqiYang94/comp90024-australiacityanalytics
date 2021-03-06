 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------

#need to run this under CreateView folder
python create_view_db_dataset_community_strength.py
python create_view_db_dataset_ieo.py
python create_view_db_dataset_ier.py
python create_view_db_dataset_life_satisfaction.py
python create_view_db_dataset_self_assessed_health.py
python create_view_db_tweets.py
python create_view_db_tweets_summary.py

cd ..
#need to run this under tweetsanalysis folder
pm2 start TweetsAnalysis.py --restart-delay 1800000 
# python TweetsAnalysis.py 

#need to run this under tweetsanalysis folder
pm2 start TweetsSummary.py --restart-delay 1800000 
# python TweetsSummary.py

#monitor the number of processed tweets
#curl -X GET "http://localhost:5984/tweets/_design/tweets_analysis/_view/monitor_processed_number"
# curl http://localhost:5984/tweets/_design/tweets_analysis/_view/monitor_processed_number?reduce=false&limit=10
