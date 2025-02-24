import json
import os


startDirLang = "/home/miba2020/twitter_coronavirus/src/langoutput"
startDirCountry = "/home/miba2020/twitter_coronavirus/src/countryoutput"

langcounter = 0
rDictionaryLang = {}

for filename in os.listdir(startDirLang):
    f = os.path.join(startDirLang, filename)
    if os.path.splitext(filename)[1] == ".lang":
        with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            print("Reducing: " + str(f))
            
            langcounter += 1

            for item in add_dictionary.keys():
                if item in rDictionaryLang.keys():
                    rDictionaryLang[item] += add_dictionary[item]
                else:
                    rDictionaryLang[item] = add_dictionary[item]
        f2.close()

print(str(langcounter))
rDictLangFinal = {"hashtags": rDictionaryLang}

with open("langreduce.lang", "w") as fout:
    fout.write(json.dumps(rDictLangFinal, ensure_ascii = False))

countrycounter = 0
rDictionaryCountry = {}

for filename in os.listdir(startDirCountry):
    f = os.path.join(startDirCountry, filename)
    if os.path.splitext(filename)[1] == ".country":
        with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            print("Reducing: " + str(f))
            
            countrycounter += 1

            for item in add_dictionary.keys():
                if item in rDictionaryCountry.keys():
                    rDictionaryCountry[item] += add_dictionary[item]
                else:
                    rDictionaryCountry[item] = add_dictionary[item]
        f2.close()

print(str(countrycounter))

rDictCountryFinal = {"hashtags": rDictionaryCountry}

with open("countryreduce.country", "w") as fout:
    fout.write(json.dumps(rDictCountryFinal, ensure_ascii = False))

