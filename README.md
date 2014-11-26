Training kit for NLP 100 Drill Exercises
========

To challenge [NLP 100 Drill Exercises](http://www.cl.ecei.tohoku.ac.jp/index.php?NLP%20100%20Drill%20Exercises).

## 0. Create environment
You need `virtualenv` and `pip`.

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 1. Prepare the data
Run the below programs in `prepare` folder.

* address.py
* tweets.py
* medline.py
* inflection_table.py
* japanese.py

When you run the `tweets.py`, you have to prepare `twitter_config.ini` in same folder.  

```
[consumer]
key = xxx
secret = xxx
[access]
token = xxx
secret = xxx
```

This file is used to get access keys for [Twitter Streaming Api](https://dev.twitter.com/streaming/public).  
So please make your twitter application and get these keys (you can create application from [here](https://apps.twitter.com/)).
