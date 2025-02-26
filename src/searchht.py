import json

path = "/home/miba2020/twitter_coronavirus/src/countryreduce.country"

with open(path, "r") as f:
    contents = f.read()
    if 'covid-19' in contents:
        print("yes")

dictprint = json.loads(contents)

for key, val in dictprint.items():
    if 'covid-19' in key:
        print(val)
