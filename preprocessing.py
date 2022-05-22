# Importing the installed libraries and their required modules

import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances


# Reading and preprocessing the music data 

data = pd.read_csv('spotify_songs.csv')
data = data[data['language'] == 'en']
data.drop(columns=['language', 'playlist_name', 'playlist_id'], inplace=True)
data = data.drop_duplicates(subset=['track_name', 'track_artist'])
data['track_album_release_date'] = pd.to_datetime(data['track_album_release_date'], infer_datetime_format=True)
data = data.sort_values(by=['track_album_release_date'])
data.reset_index(drop=True, inplace=True)


# Sectioning off data for recommendation subsystems

lyrics_data = data['lyrics']
energy_data = data[['danceability', 'tempo', 'acousticness']]
mood_data = data[['mode', 'key', 'valence']]


# Using cosine similarity and Tfidf for making lyrics comparable

lyrics_data = TfidfVectorizer(stop_words='english').fit_transform(lyrics_data)
lyric_similarity_matrix = cosine_similarity(lyrics_data)


# Using euclidean distance for making energy and mood comparable

energy_difference_matrix = euclidean_distances(energy_data)
mood_difference_matrix = euclidean_distances(mood_data)


# pickling all data needed for making recommendations

pickle.dump(data, open('data.pkl', 'wb'))
pickle.dump(lyric_similarity_matrix, open('lyric_similarity_matrix.pkl', 'wb'))
pickle.dump(energy_difference_matrix, open('energy_difference_matrix.pkl', 'wb'))
pickle.dump(mood_difference_matrix, open('mood_difference_matrix.pkl', 'wb'))

print('preprocessing done')