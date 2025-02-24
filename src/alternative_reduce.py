#!/usr/bin/env python3

import json
import os
import re


import requests
import matplotlib.pyplot as plt
import os


# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

startDirLang = "/home/miba2020/twitter_coronavirus/src/langoutput"

datecounter = 0
datetweets = 0
rDictionaryDate = {}

for filename in os.listdir(startDirLang):
    f = os.path.join(startDirLang, filename)
    if os.path.splitext(filename)[1] == ".lang":
        with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            pattern = r"geoTwitter(.*?)[.]"
            date = re.search(pattern, filename).group(1)

            print("Reducing: " + str(f))
            
            datecounter += 1

            for item in add_dictionary.items():
                (tup, val) = item
                datetweets += val
                tup = eval(tup)
                ht = tup[0]
                iden = tup[1]
                if ht in rDictionaryDate.keys():
                    checkiden = rDictionaryDate[ht]
                    if date in checkiden.keys():
                        rDictionaryDate[ht][date] += val 
                    else:
                        rDictionaryDate[ht][date] = val
                else:
                    rDictionaryDate[ht] = {date: val}

                rDictionaryDate[ht] = dict(sorted(rDictionaryDate[ht].items())) 
                
        f2.close()

# imports
import os
import json
from collections import Counter,defaultdict

counts = rDictionaryDate

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)


#matplotlib

categories, values = zip(*items)

plt.figure(figsize=(6, 4))
plt.plot(categories, values)

plt.xticks(categories[::30], rotation=45)

plt.ylabel("Number of tweets")
plt.xlabel("Date")

plt.title("Tweets over time for: " + str(args.key))

plt.savefig("tweetsovertime"+str(args.key), dpi = 300)

