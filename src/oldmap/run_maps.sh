#!/bin/sh

for file in /data/Twitter\ dataset/geoTwitter20-*.zip; do 
    nohup python3 map.py "$file" &
done
