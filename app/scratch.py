from tweets import tweets
import random

random_num = random.randrange(0,5) - 1
random_tweet = tweets[random_num]['tweet']

print((random_tweet))
