#!/usr/bin/env python3

import json
import os
import re


import requests
import matplotlib.pyplot as plt
import os

from matplotlib import font_manager


# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_ht_path',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

startDirLang = "/home/miba2020/twitter_coronavirus/src/newmap/lang"


font_path = "/home/miba2020/twitter_coronavirus/src/newmap/fonts/fonts/NotoSansCJK-Regular.ttc"
font_prop = font_manager.FontProperties(fname=font_path)

datecounter = 0
datetweets = 0
rDictionaryDate = {}
l_dates = {}

for filename in os.listdir(startDirLang):
    f = os.path.join(startDirLang, filename)
    if os.path.splitext(filename)[1] == ".lang":
        with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            pattern = r"geoTwitter(.*?)[.]"
            date = re.search(pattern, filename).group(1)
            l_dates[date] = 0

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

filtereddict = {}
lHashtags = []

#open the input hashtags
with open(args.input_ht_path) as f:
    for line in f:
        addline = line.strip()
        addline = addline[1:]
        lHashtags.append(addline)


for ht in lHashtags:
    if ht in rDictionaryDate.keys():
        add_dict = {}
        for key, val in l_dates.items():
            if key in rDictionaryDate[ht].keys():
                add_dict[key] = rDictionaryDate[ht][key]
            else:
                add_dict[key] = 0
        filtereddict[ht] = add_dict
    else:
        print("Inputted hashtag not found: " + ht)

#print(counts)

# normalize the counts by the total values
#if args.percent:
#    for k in counts:
#        counts[k] /= counts['_all'][k]

# print the count values
#items = sorted(counts.items(), key=lambda item: item[0])
#for k,v in items:
#    print(k,':',v)


#matplotlib

#categories, values = zip(*items)

first_iter_keys = True

plt.clf()
for key, val in filtereddict.items():
    dates = dict(sorted(val.items(), key=lambda item: item[0]))
    plt.plot(list(dates.keys()), list(dates.values()), label=key)

    if first_iter_keys:
        key_labels = list(dates.keys())
        plt.xticks(key_labels[::30], rotation=45)
        first_iter_keys = False

plt.legend(prop=font_prop)
plt.xlabel("Date")
plt.ylabel("Number of tweets")
plt.tight_layout()

plt.title("Tweets over time for inputted hashtags")

plt.savefig("tweetsovertime"+''.join(map(str, lHashtags)), dpi = 300)

