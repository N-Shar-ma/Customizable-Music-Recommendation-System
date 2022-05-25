# 🎶 Customizable Music Recommendation System 🎶

This web app is the prototype for a music recommendation system unlike any other. Most traditional systems are not very transparent about why a recommendation is made, and seem like magical black boxes. What sets apart this customizable music recommendation system from the rest is that it aims to clearly convey the reason behind each recommendation, and put all the control in the hands of the user so that they can pick and choose what kind of recommendations they like, and hence personalize the system just like they want.

## Use Case Examples:
- Suppose user A has been out of the loop and wants to get up to speed with the most popular music, so they can use the (default) "keep up with what's trending mode". If another user B already knows most of the popular songs and would rather listen to lesser known underrated tracks, the "discover hidden gems" mode is for them. These modes are clearly differentiated based on the songs' popularity.
- Alternatively, suppose user C doesn't care much about the lyrics to a song but only their overall energy and vibe, so they can turn off the "Lyrically similar" recommendations, while is user D treats songs like poetry and primarily focuses on just that, they can do the opposite.
- User E is interested in songs of a particular era, so they can turn on just the "Released around the same time" recommendations" to explore contemporary songs
- User F has just discovered their new favourite artist and wants to explore their discography, whether it be their popular hits or underrated songs, they can turn on the "By same artist" recommendations alone.
- User G knows that they get easily distracted when faced with too many choices of recommendations to choose from, so they can reduce the number of recommendations shown down to 1, while if User H likes variety they can turn up the number of recommendations of each type to up to 10!

## Technologies Used

Python was used throughout along with the following modules:
- Pandas
- Numpy
- Scikit Learn
- Streamlit (for frontend)

## Local Set Up

After cloning the repository and firing up a virtual environment and run the following commands:
```
pip install -r requirements.txt    # installs dependencies
streamlit run app.py    # runs the frontend locally in browser
```

## Folder Organization
    
    ├── .streamlit
    │   └── config.toml                   # Theming for frontend
    ├── pickles                           # Data used to make recommendations 
    │   ├── data.pkl                     
    │   ├── energy_similarity_mapping.pkl 
    │   ├── lyric_similarity_mapping.pkl
    │   └──mood_similarity_mapping.pkl
    ├── app.py                            # frontend using streamlit
    ├── preprocessing.py                  # cleans data and generates pickles
    ├── recommender.py                    # code for core recommendation system
    ├── recommender.ipynb                 # initial testing of system
    ├── requirements.txt 
    └── spotify_songs.csv                 # raw sourced data

Tthe 2 main files (run dynamically) are `app.py` and `recommender.py`