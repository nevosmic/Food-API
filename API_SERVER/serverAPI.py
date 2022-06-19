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

data = response.json()

reviews = data['reviews']


def find_highest_user(reviews, max_rating):
	users_list =[]
	for x in reviews:
		if (x['rating'] == max_rating):
			users_list.append({x['profiles'][0]['displayName']:x['profiles'][0]['pictureUrl']})
	return users_list


def max_rating(reviews):
	max = -1
	for x in reviews:
		if(x['rating']>max):
			max = x['rating']
	return max

max=max_rating(reviews)

users_list = find_highest_user(reviews,max)
output_file = open('Users_Info.txt', 'a')
output_file.write(str(users_list))
output_file.write('\n')
output_file.write('AverageRating: {}'.format(data['averageRating']))
print(users_list)
print('AverageRating: {}'.format(data['averageRating']))

output_file.close()