#!/usr/bin/env python3

import requests
import matplotlib.pyplot as plt
import os


# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)


#matplotlib

topten = items[:10]
print(topten)
categories, values = zip(*topten)

plt.figure(figsize=(6, 4))
plt.bar(categories, values)

_, fileext = os.path.splitext(args.input_path)
fileext = fileext[1:]

plt.title("Prevelance of selected hashtag by: " + str(fileext))

plt.ylabel("Number of tweets")

plt.savefig("plot"+str(fileext)+str(args.key), dpi = 300)

