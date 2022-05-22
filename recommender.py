# Importing the needed installed libraries

import pickle
import pandas as pd
import numpy as np


# Loading all the pickled data for making recommendations 

data = pickle.load(open('data.pkl', 'rb'))
songs_count = data.shape[0]
lyric_similarity_matrix = pickle.load(open('lyric_similarity_matrix.pkl', 'rb'))
energy_difference_matrix = pickle.load(open('energy_difference_matrix.pkl', 'rb'))
mood_difference_matrix = pickle.load(open('mood_difference_matrix.pkl', 'rb'))


# Utility functions

def sort_by_popularity(songs, descending=True):
    if descending:
        return songs.sort_values(by=['track_popularity'])[::-1]
    else:
        return songs.sort_values(by=['track_popularity'])

def get_similar(track_index, count, comparison_matrix, select_smallest):
    similar_songs_indexes = np.argsort(np.array(comparison_matrix[track_index]))
    similar_songs_indexes = np.delete(similar_songs_indexes, np.where(similar_songs_indexes == track_index))
    similar_songs_indexes = similar_songs_indexes[:count] if select_smallest else similar_songs_indexes[::-1][:count]
    return data.iloc[similar_songs_indexes].copy()

def songs_as_dict(songs, include_fields):
    return songs[include_fields].to_dict(orient='index')

def get_closest_n(track_index, count):
    if track_index >= count//2 and track_index < songs_count-count//2:
        return pd.concat([data.iloc[track_index-count//2 : track_index], data.iloc[track_index+1 : track_index+count//2+1]])
    elif track_index < count//2:
        return data.head(count+1).drop(track_index)
    else:
        return data.tail(count+1).drop(track_index)


# Getters for recommendation subsystems

def get_by_same_artist(track_index, count):
    return data[data['track_artist'] == data.iloc[track_index]['track_artist']].drop(track_index)[:count]

def get_lyrically_similar(track_index, count):
    return get_similar(track_index, count, lyric_similarity_matrix, False)

def get_energy_similar(track_index, count):
    return get_similar(track_index, count, energy_difference_matrix, True)

def get_mood_similar(track_index, count):
    return get_similar(track_index, count, mood_difference_matrix, True)

def get_random(count):
    return data.sample(count)

def get_released_around_same_time(track_index, count):
    return get_closest_n(track_index, count)


# Recommendation subsytems

def recommend_by_same_artist(track_index, count, prioritisePopular):
    songs_by_same_artist = get_by_same_artist(track_index, count*2)
    songs_by_same_artist['recommendation_type'] = 'by same artist'
    return sort_by_popularity(songs_by_same_artist, prioritisePopular)[:count]

def recommend_lyrically_similar(track_index, count, prioritisePopular):
    similar_songs = get_lyrically_similar(track_index, count*2)
    similar_songs['recommendation_type'] = 'lyrically similar'
    return sort_by_popularity(similar_songs, prioritisePopular)[:count]

def recommend_energy_similar(track_index, count, prioritisePopular):
    similar_songs = get_energy_similar(track_index, count*2)
    similar_songs['recommendation_type'] = 'similar energy'
    return sort_by_popularity(similar_songs, prioritisePopular)[:count]

def recommend_mood_similar(track_index, count, prioritisePopular):
    similar_songs = get_mood_similar(track_index, count*2)
    similar_songs['recommendation_type'] = 'similar mood'
    return sort_by_popularity(similar_songs, prioritisePopular)[:count]

def recommend_released_around_same_time(track_index, count, prioritisePopular):
    contemporary_songs = get_released_around_same_time(track_index, count*2)
    contemporary_songs['recommendation_type'] = 'released around same time'
    return sort_by_popularity(contemporary_songs, prioritisePopular)[:count]

def recommend_random(count, prioritisePopular):
    random_songs = get_random(count*2)
    random_songs['recommendation_type'] = 'random'
    return sort_by_popularity(random_songs, prioritisePopular)[:count]


# Hybrid recommendation system

def hybrid_recommend(track_index, count=5, prioritisePopular=True):
    by_same_artist = recommend_by_same_artist(track_index, count, prioritisePopular)
    lyrically_similar = recommend_lyrically_similar(track_index, count, prioritisePopular)
    energy_similar = recommend_energy_similar(track_index, count, prioritisePopular)
    mood_similar = recommend_mood_similar(track_index, count, prioritisePopular)
    random = recommend_random(count, prioritisePopular)
    released_around_same_time = recommend_released_around_same_time(track_index, count, prioritisePopular)
    all_recommendations = pd.concat([by_same_artist, lyrically_similar, energy_similar, mood_similar, random, released_around_same_time])
    return songs_as_dict(all_recommendations, include_fields=['track_name', 'track_artist', 'recommendation_type'])
