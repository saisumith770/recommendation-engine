'''
An algorithm to retrieve the top content based on likes and views

def ratePercentile(array,rate):
	higher_rate_count = 0
	for i in array:
		if(i["avg_rate"] <= rate):
			higher_rate_count += 1

	return (higher_rate_count/ len(array))

def weighted_rating(array,vote_count,min_vote,rate):
	return (vote_count / (vote_count + min_vote))*rate + (min_vote / (vote_count + min_vote)) * ratePercentile(array,rate)
'''

import pandas as pd 

metaData = pd.DataFrame({
	"viewer_count" : [10,100,200,300,50,70,160,140,130,100],
	"likes" : [100000,70005,96545,6223,633,4123,54255,754,55,85]
})

mean_viewership_across_dataframe = metaData["viewer_count"].mean()
minimum_required_viewership = metaData["viewer_count"].quantile(0.75)
#metaData.copy().loc(metaData["viewer_count"] >= minimum_required_voting)
filtered_items = metaData[metaData["viewer_count"] >= minimum_required_viewership]

def weighted_rating(item):
	viewer_count = item["viewer_count"]
	likes = item["likes"]
	return (viewer_count/(viewer_count+minimum_required_viewership) * likes) + (minimum_required_viewership/(minimum_required_viewership+viewer_count) * mean_viewership_across_dataframe)

filtered_items['score'] = filtered_items.apply(weighted_rating,axis=1)
filtered_items = filtered_items.sort_values('score',ascending=True)

print(filtered_items)