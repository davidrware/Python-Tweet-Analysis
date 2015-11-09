import json
import pandas as pd
import matplotlib.pyplot as plt
import pprint

tweets_data_path = "./twitter_data_morning.dat"

tweets_data = []
tweets_file = open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print "Number of tweets:{0}".format(len(tweets_data))

# Needed to add index=... for the following reason:
# https://github.com/pydata/pandas/issues/2147
tweets = pd.DataFrame(index=range(len(tweets_data)))
tweets['text'] = map(lambda tweet: tweet['text'] if "text" in tweet else None,tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'] if "lang" in tweet else None,tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['name'] if "place" in tweet and tweet['place'] != None else None,tweets_data)

tweets_by_lang =  tweets['lang'].value_counts()
tweets_by_country = tweets['country'].value_counts()

print tweets_by_lang[:5]
print "-------------"
print tweets_by_country[:10]
