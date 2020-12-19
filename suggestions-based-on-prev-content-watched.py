"""
An algorithm to suggest the content based on your watch list
"""

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.DataFrame({
	"description" : [
		"Led by Woody, Andy's toys live happily in his ...",
    	"When siblings Judy and Peter discover an encha...",
    	"When Pete discovers who he really is...",
    	"A family wedding reignites the ancient feud be...",
    	"Cheated on, mistreated and stepped on, the wom...",
    	"Just when George Banks has recovered from his ..."
	]
})

tfid = TfidfVectorizer(stop_words='english')

replaced_non_numbers = data["description"].fillna("")
tfid_matrix = tfid.fit_transform(data["description"])

cosine_similarity =  linear_kernel(tfid_matrix, tfid_matrix)

indices = pd.Series(data.index, index=data['description']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_similarity):
	index = indices[title]
	sim_scores = list(enumerate(cosine_sim[index]))
	sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

	sim_scores = sim_scores[:]

	movie_indices = [i[0] for i in sim_scores]

	return data['description'].iloc[movie_indices]

print(get_recommendations("When Pete discovers who he really is..."))