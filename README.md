# 🎶 Customizable Music Recommendation System 🎶

This web app is the prototype for a music recommendation system unlike any other. Most traditional systems are not very transparent about why a recommendation is made, and seem like magical black boxes. What sets apart this customizable music recommendation system from the rest, is that it aims to clearly convey the reason behind each recommendation, and put all the control in the hands of the user so that they can pick and choose what kind of recommendations they'd like, and hence personalize the system just as they want.

## Features
### Core features
- 2 modes of recommendations between which the user can toggle anytime:
  - Keep up with what's trending (suggests more popular songs)
  - Discover hidden gems (suggests less popular songs)
- A total of 6 types of recommendations:
  - by same artist
  - lyrically similar (not seen in most popular music streaming services)
  - similar energy
  - similar mood
  - released around the same time
  - random
- User can choose to see any, all, or none of the aforementioned recommendation types
- User can set the number of recommendations of each chosen type between the range of 1 to 10
### UX related features
- Ability to show or hide the lyrics for each song
- Youtube video linked for each song
- Each recommended song can be viewed via a listen button, where this song's recommendations can then be seen and so on
- Ability to switch the width of the main content area
- Ability to choose between a custom (pastel), light and dark theme.
- Handy hamburger menu with options to report a bug, share the web app, view source code, read about it, see credits, etc

## Use Case Examples:
- Suppose user A has been out of the loop and wants to get up to speed with the most popular music. They can use the (default) "keep up with what's trending mode". If another user B already knows most of the popular songs and would rather listen to lesser known tracks, the "discover hidden gems" mode is for them. These modes are clearly differentiated based on the songs' popularity.
- If user C doesn't care much about the lyrics to a song but only their overall energy and mood, they can turn off the "lyrically similar" recommendations, while if user D treats songs like poetry and primarily focuses on just the lyrics, they can do the opposite.
- User E is interested in songs of a particular era, so they can turn on just the "released around the same time" recommendations" to explore contemporary songs
- User F has just discovered their new favourite artist and wants to explore their discography, be it their popular hits or underrated songs, so they can turn on the "by same artist" recommendations alone.
- User G knows that they get easily distracted when faced with too many choices of recommendations to choose from, so they can reduce the number of recommendations shown down to 1, while if User H likes variety they can turn up the number of recommendations of each type to up to 10!
- User H is feeling adventurous and would like to stumble upon music without any relation to their usual taste. The random recommendations are perfect for them!

## Technologies Used

Python was used throughout along with the following modules:
- Pandas
- Numpy
- Scikit Learn
- Streamlit (for frontend)

## Local Set Up

After cloning the repository and firing up a virtual environment, run the following commands:
```
pip install -r requirements.txt    # installs dependencies
streamlit run app.py    # runs the frontend locally in browser
```

## Folder Organization
    
    ├── .streamlit
    │   └── config.toml                   # Custom theming for frontend
    ├── pickles                           # Data used to make recommendations 
    │   ├── data.pkl                     
    │   ├── energy_similarity_mapping.pkl 
    │   ├── lyric_similarity_mapping.pkl
    │   └── mood_similarity_mapping.pkl
    ├── app.py                            # frontend using streamlit
    ├── preprocessing.py                  # cleans data and generates pickles
    ├── recommender.py                    # code for core recommendation system
    ├── recommender.ipynb                 # initial testing of system
    ├── requirements.txt 
    └── spotify_songs.csv                 # raw sourced data

The 3 main files of interest (with relevant code) are `preprocessing.py`, `app.py` and `recommender.py`