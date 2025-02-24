filepath1 = '/data/Twitter dataset/geoTwitter20-03-20.zip'
filepath3 = '/data/Twitter dataset/tweets-20220406.zip'
filepath2 = '/home/miba2020/twitter_coronavirus/hashtags'
filepath4 = '/data/Twitter dataset/tweets-20230123.zip'

import json
from collections import Counter

lang_counter = Counter()
country_counter = Counter()

import zipfile

hashtagsearch = []
match_audit = []

hashtagfile = open(filepath2, 'r')

for line in hashtagfile:
    addline = line.strip()[1:]
    hashtagsearch.append(addline)
hashtagfile.close()

print(hashtagsearch)

with zipfile.ZipFile(filepath4, 'r') as zip_ref:
    for name in zip_ref.namelist():
        with zip_ref.open(name, 'r') as file:
            for i, line in enumerate(file):
                #print(line.decode('utf-8').strip())
                datum = json.loads(line)

                try:
                    tweet_id = datum['id']
                except KeyError:
                    try:
                        tweet_id = datum['data']['id']
                    except:
                        print("Other key error")
                except:
                    print("ID/Text Error")
                    print("Other error")
 

                if tweet_id == "1617643337434939397":
                    print("here")
                    #print(json.dumps(line.decode('utf-8').strip()))
                    
                    tweet_data = json.loads(line.decode('utf-8').strip())
                    print(json.dumps(tweet_data, indent=4)) 
                    break

                if i > 5000:
                    break
