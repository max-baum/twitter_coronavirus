# Coronavirus tweet analysis

**Overview**

In this project, I analyzed geotagged tweets in 2020 for the prevelance of the certain hashtags as tracked against other tweet metadata. Specifically, I looked at the prevalance of the hashtags related to coronavirus (see `./hashtags`) against tweet language, tweet origin country, and tweet date. To carry out this analysis, I used MapReduce to process and parse a dataset of one billion geotagged tweets.

Note that there are two subdirectories within `src`, one called `oldmap`, the other `newmap`. `oldmap` consists of initial analysis work that was case sensitive. `newmap` consists of case-insensitive results. The findings below are from `newmap`.

**Sample Findings** 

Below, I visualize the prevalence of certain hastags in tweets by country and by language, according to the analysis I conducted.

In my first visualization, we can see the prevalance of tweets in 2020 containing #coronavirus by country
![Prevalance of #coronavirus in tweets by country](src/newmap/plotcountrycoronavirus.png)

In my second visualization, we can see the prevalance of tweets in 2020 containing #코로나바이러스 by country
![Prevalance of #코로나바이러스 in tweets by country](src/newmap/plotcountry코로나바이러스.png)

In my third visualization, we can see the prevalance of tweets in 2020 containing #coronavirus by language
![Prevalance of #coronavirus in tweets by language](src/newmap/plotlangcoronavirus.png)

In my fourth visualization, we can see the prevalance of tweets in 2020 containing #코로나바이러스 by language
![Prevalance of #코로나바이러스 in tweets by language](src/newmap/plotlang코로나바이러스.png)
