import json
import os


startDirLang = "/home/miba2020/twitter_coronavirus/src/langoutput"
startDirCountry = "/home/miba2020/twitter_coronavirus/src/countryoutput"
startDirAudit = "/home/miba2020/twitter_coronavirus/src/auditoutput"

totalTweets = {}
langTweets = {}
countryTweets = {}

for filename in os.listdir(startDirAudit):
    f = os.path.join(startDirAudit, filename)
    if os.path.splitext(filename)[1] == ".audit":
       with open(f) as f2:
           add_data = f2.read()
           add_dictionary = json.loads(add_data)

           fname_brief = filename.split(".")[0]
           totalTweets[fname_brief] = add_dictionary[-1][0]

           f2.close()

for filename in os.listdir(startDirLang):
    f = os.path.join(startDirLang, filename)
    if os.path.splitext(filename)[1] == ".lang":
       with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            fname_brief = filename.split(".")[0]
            langTweets[fname_brief] = sum(add_dictionary.values())

            f2.close()

for filename in os.listdir(startDirCountry):
    f = os.path.join(startDirCountry, filename)
    if os.path.splitext(filename)[1] == ".country":
        with open(f) as f2:
            add_data = f2.read()
            add_dictionary = json.loads(add_data)
            
            fname_brief = filename.split(".")[0]
            countryTweets[fname_brief] = sum(add_dictionary.values())

with open("auditreduce.txt", "w") as fout:
    sorted_dict = {key: totalTweets[key] for key in sorted(totalTweets)}
    for key, value in sorted_dict.items():
        langVal = str(langTweets[key])
        countryVal = str(countryTweets[key])
        fout.write(key + "\t" + value + "\t" + langVal + "\t" + countryVal + "\n")
    fout.close()


