import json
import os


startDirLang = "/home/miba2020/twitter_coronavirus/src/newmap/lang"
startDirCountry = "/home/miba2020/twitter_coronavirus/src/newmap/country"

langcounter = 0
langtweets = 0
rDictionaryLang = {}

for filename in os.listdir(startDirLang):
    f = os.path.join(startDirLang, filename)
    if os.path.splitext(filename)[1] == ".lang":
        with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            print("Reducing: " + str(f))
            
            langcounter += 1

            for item in add_dictionary.items():
                (tup, val) = item
                langtweets += val
                tup = eval(tup)
                ht = tup[0]
                iden = tup[1]
                if ht in rDictionaryLang.keys():
                    checkiden = rDictionaryLang[ht]
                    if iden in checkiden.keys():
                        rDictionaryLang[ht][iden] += val 
                    else:
                        rDictionaryLang[ht][iden] = val
                else:
                    rDictionaryLang[ht] = {iden: val}
        f2.close()

print("Files read: " + str(langcounter))
print("Tweets read: " + str(langtweets))

with open("langreduce.lang", "w") as fout:
    fout.write(json.dumps(rDictionaryLang, ensure_ascii = False))

countrycounter = 0
countrytweets = 0
rDictionaryCountry = {}

for filename in os.listdir(startDirCountry):
    f = os.path.join(startDirCountry, filename)
    if os.path.splitext(filename)[1] == ".country":
        with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            print("Reducing: " + str(f))
            
            countrycounter += 1

            for item in add_dictionary.items():
                (tup, val) = item
                countrytweets += val
                tup = eval(tup)
                ht = tup[0]
                iden = tup[1]
                if ht in rDictionaryCountry.keys():
                    checkiden = rDictionaryCountry[ht]
                    if iden in checkiden.keys():
                        rDictionaryCountry[ht][iden] += val 
                    else:
                        rDictionaryCountry[ht][iden] = val
                else:
                    rDictionaryCountry[ht] = {iden: val}
        f2.close()

print("Files read: " + str(countrycounter))
print("Tweets read: " + str(countrytweets))

with open("countryreduce.country", "w") as fout:
    fout.write(json.dumps(rDictionaryCountry, ensure_ascii = False))


