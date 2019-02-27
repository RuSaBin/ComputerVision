# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:50:39 2019

@author: rutab
"""
import json
from requests.adapters import HTTPAdapter
import requests_cache
import config
import os


clear = False

if clear == True:
    os.remove("cache.sqlite")
    print('Cache is cleared')
    
url = 'http://api.themoviedb.org'
key = config.KEY

with  requests_cache.CachedSession() as s:
    
    s.mount(url, HTTPAdapter(max_retries=5))

    try:
 
        response = s.get("%s/3/genre/movie/list?language=en-US&api_key=%s" % (url, key)).json() 
   
    except Exception as e:
        
        print(e.message)

    
 
    ### List of Movies of genre horror from 2000 to 2019 ###
    try:
 
        response = s.get("%s/3/discover/movie?page=1&include_video=false&with_genres=27&primary_release_date.gte=2000-01-01&primary_release_date.lte=2019-01-01&api_key=%s" % (url, key)).json()
        name = os.path.join('data',str(1) + '.json')
        with open(name, 'w', encoding='utf8') as outfile: 
                    json.dump(response, outfile, ensure_ascii = False, indent = 2)
       
    except Exception as e:
            
        print(e.message) 
        
    pages = response['total_pages']
    results = response['total_results']
    response['results'][1].keys()
    
    for i in range(pages+1):
    
        page = i
        print(i)
    
     
    
        response = s.get("%s/3/discover/movie?page=%s&include_video=false&with_genres=27&primary_release_date.gte=2000-01-01&primary_release_date.lte=2019-01-01&api_key=%s" % (url, page, key))
        name = os.path.join('data',str(i) + '.json')
        
        if not response.from_cache:
           try:
                response.raise_for_status()    
                response = response.json()

                with open(name, 'w', encoding='utf8') as outfile: 
                    json.dump(response, outfile, ensure_ascii = False, indent = 2)
                
           except Exception as e :
                print(e)
        else :
            print('Retrieved from cache') 

     
            
    
  