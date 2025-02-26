#filepath1 = '/data/Twitter dataset/geoTwitter20-03-20.zip'
#filepath3 = '/data/Twitter dataset/tweets-20220406.zip'
filepath2 = '/home/miba2020/twitter_coronavirus/hashtags'
#filepath4 = '/data/Twitter dataset/tweets-20230123.zip'

import json
from collections import Counter
import os
import sys


#if len(sys.argv) > 1:
 #   filepath = sys.argv[1]
  #  print('filepath' + filepath)
#else:
  #  print('Invalid filepath')
   # sys.exit(1)

#lang_counter = Counter()
#country_counter = Counter()

#import zipfile

hashtagsearch = []
match_audit = []
tweet_count = 0

hashtagfile = open(filepath2, 'r')

for line in hashtagfile:
    addline = line.strip()[1:]
    hashtagsearch.append(addline)
hashtagfile.close()

print(hashtagsearch)


