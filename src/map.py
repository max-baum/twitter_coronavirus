#filepath1 = '/data/Twitter dataset/geoTwitter20-03-20.zip'
#filepath3 = '/data/Twitter dataset/tweets-20220406.zip'
filepath2 = '/home/miba2020/twitter_coronavirus/hashtags'
#filepath4 = '/data/Twitter dataset/tweets-20230123.zip'

import json
from collections import Counter
import os
import sys


if len(sys.argv) > 1:
    filepath = sys.argv[1]
    print('filepath' + filepath)
else:
    print('Invalid filepath')
    sys.exit(1)

lang_counter = Counter()
country_counter = Counter()

import zipfile

hashtagsearch = []
match_audit = []
tweet_count = 0

hashtagfile = open(filepath2, 'r')

for line in hashtagfile:
    addline = line.strip()[1:]
    hashtagsearch.append(addline)
hashtagfile.close()

print(hashtagsearch)
print(filepath)

with zipfile.ZipFile(filepath, 'r') as zip_ref:
    for name in zip_ref.namelist():
        with zip_ref.open(name, 'r') as file:
            for i, line in enumerate(file):
                #print(line.decode('utf-8').strip())
                datum = json.loads(line)
                

                tweet_count += 1

                try:
                    tweet_id = datum['id']
                    tweet_text = datum['text']
                except KeyError:
                    try:
                        tweet_id = datum['data']['id']
                        tweet_text = datum['data']['text']
                    except:
                        #print("Other key error")
                        pass
                except:
                    #print("ID/Text Error")
                    #print("Other error")
                    pass
                try:
                    lang = datum['lang']
                except KeyError:
                    try:
                        lang = datum['data']['lang']
                    except:
                        #print("Other key error")
                        pass
                except:
                    #print("Lang Error")
                    #print("Other error")
                    pass
                try:
                    place = datum['place']['country_code']
                except KeyError:
                    try: 
                        place = datum['data']['place']['country_code']
                    except:
                        place = "und"
                        #print("Other key error")
                except:
                    place = "und"
                    #print("Country Error")
                    #print("Other error")

                hashtag = []

                try:
                    hashtag = datum['entities']['hashtags']
                except KeyError:
                    try:
                        hashtag = datum['data']['entities']['hashtags']
                    except:
                        #print("Other key error")
                        pass
                except:
                    #print("Hashtag Error")
                    #print("Other error")
                    pass

                if len(hashtag) > 0:
                    if "text" in hashtag[0].keys():
                        for item in hashtag:
                            if item["text"] in hashtagsearch:
                                lang_counter[(item['text'], lang)] += 1
                                country_counter[(item['text'], place)] += 1
                                audit = (tweet_id,tweet_text,item['text'], lang, place) 
                                match_audit.append(audit)
                    elif "tag" in hashtag[0].keys():
                        for item in hashtag:
                            if item["tag"] in hashtagsearch:
                                lang_counter[(item['tag'], lang)] += 1
                                country_counter[(item['tag'], place)] += 1
                                audit = (tweet_id,tweet_text,item['tag'], lang, place)
                                match_audit.append(audit)

                #if i > 5000:
                #break

finalaudit = (str(tweet_count),'tweets read in file','', '', '')
match_audit.append(finalaudit)

filename = os.path.basename(filepath)
filename_nozip = os.path.splitext(filename)[0]

filenamelang = 'langoutput/' + filename_nozip + '.lang'
filenamecountry = 'countryoutput/' + filename_nozip + '.country'
filenameaudit = 'auditoutput/' + filename + '.audit'

json_dict_lang = {str(k): v for k, v in lang_counter.items()}
json_dict_country = {str(k): v for k, v in country_counter.items()}

with open(filenamelang, 'w') as fout:
    fout.write(json.dumps(json_dict_lang, ensure_ascii=False))

with open(filenamecountry, 'w') as fout:
    fout.write(json.dumps(json_dict_country, ensure_ascii=False))

with open(filenameaudit, 'w') as fout:
    fout.write(json.dumps(match_audit, ensure_ascii=False))
