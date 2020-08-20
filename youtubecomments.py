#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import json
import urllib.request

#pytube is a python package for downloading from YouTube

from pytube import Youtube

apiKey = "ENTER_API_KEY"
videoId = ""
nextPageToken = ""

stop = False

count = 0

maxResults = 100


if maxResults > 100:
    maxResults = 100
    
#create an empty list where you will dumb all the comments 

dumb = []


while not stop:
    #go to the YouTube API and input your parameters in the request  as per the YouTube API specifications
    """ key={apiKey} snippet, videoId= {videoId}, maxResults={maxResults},pageToken={nextPageToken}"""
    
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={apiKey}&textFormat=plainText&part=snippet&videoId={videoId}&t&maxResults={maxResults}&pageToken={nextPageToken}"
    json_url = urllib.request.urlopen(url)
    data  = json.loads(json_url.read())
    nPT = 'nextPageToken'
    
    if nPT in data:
        nextPageToken = data['nextPageToken']
    else:
        stop = True
        
    nComments = len(data['items'])
    
    
    for i in range(nComments):
        print(f'Grabbed comment #{i + (count*maxResults)}')
        put = f"{data['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']}\t{data['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']}".replace('\n'," ").replace('\r'," ")
        dump.append(put)

        
    count += 1
    
    
with open("allComments.tsv", "w+", encoding = 'utf-8') as f:
    f.write("\n".join(dump))

    
        


# In[ ]:




