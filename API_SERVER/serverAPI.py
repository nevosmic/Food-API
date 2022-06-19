import requests
import pandas as pd
import json
'''
import http.client

conn = http.client.HTTPSConnection("yummly2.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "38fe48db78msha6986defdf1dc87p1f30e5jsn7d3b1929314d",
    'X-RapidAPI-Host': "yummly2.p.rapidapi.com"
    }

conn.request("GET", "/feeds/auto-complete?q=chicken%20soup", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
'''

url = "https://yummly2.p.rapidapi.com/reviews/list"

querystring = {"offset":"0","globalId":"a8d6747a-bfaa-46a7-92fb-892e3f76b264","limit":"20"}

headers = {
	"X-RapidAPI-Key": "38fe48db78msha6986defdf1dc87p1f30e5jsn7d3b1929314d",
	"X-RapidAPI-Host": "yummly2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())
data = response.json()
print(data.keys())
print(data['averageRating'])
reviewImages = data['reviewImages']
reviews = data['reviews']
for x in reviews:
	print(x)

def find_highest_user(reviews, max_rating):
	for x in reviews:
		if (x['rating'] == max_rating):
			print(x['displayName'])
			print(x['pictureUrl'])


def max_rating(reviews):
	max = -1
	for x in reviews:
		if(x['rating']>max):
			max = x['rating']
	return max

max=max_rating(reviews)

#find_highest_user(reviews,max)

#print(reviews['profiles'])


