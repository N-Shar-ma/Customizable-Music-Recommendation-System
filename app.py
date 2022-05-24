import streamlit as st
from recommender import hybrid_recommend, get_metadata
from youtubesearchpython import VideosSearch

st.set_page_config(
    page_title='Customizable Music Recommendation System', 
    page_icon='🎶',
    menu_items={
        'Get Help': None,
        'Report a bug': "https://github.com/N-Shar-ma/Customizable-Music-Recommendation-System/issues",
        'About': "### This project was made as part of Microsoft Engage'22!"
    }
)

def change_song(index):
    st.session_state['current_song_index'] = index

if 'current_song_index' not in st.session_state:
    st.session_state['current_song_index'] = 1255

st.title('🎶 Customizable Music Recommendation System 🎶')

st.sidebar.title('Choose:')

option1 = 'Keep up with what\'s trending'
option2 = 'Discover hidden gems'
mode = st.sidebar.selectbox('Your mode of recommendations', (option1, option2))
if(mode == option1):
    prioritisePopular = True
else:
    prioritisePopular = False

recommendations_count = st.sidebar.slider('Upto how many of each kind of recommendations would you like (lesser means more accurate but more means more variety!)', min_value=1, max_value=10, value=3)

st.sidebar.write('Which kinds of recommendations you\'d like')

current_song_metadata = get_metadata(st.session_state['current_song_index'])

st.write(f'## {current_song_metadata["track_name"]} - {current_song_metadata["track_artist"]}')

youtube_search = VideosSearch(f'## {current_song_metadata["track_name"]} - {current_song_metadata["track_artist"]}', limit = 1)
youtube_id = youtube_search.result()['result'][0]['id']
image_url = youtube_search.result()['result'][0]['thumbnails'][0]['url']

st.write(f'[![YouTube thumbnail]({image_url})](https://www.youtube.com/watch?v={youtube_id})')
st.write(f'[Hear on YouTube](https://www.youtube.com/watch?v={youtube_id})')

with st.expander('Show lyrics'):
    st.write(current_song_metadata['lyrics'])

recommendations = hybrid_recommend(st.session_state['current_song_index'], recommendations_count , prioritisePopular=prioritisePopular)

for recommendation_type, songs in recommendations.items():
    if not st.sidebar.checkbox(recommendation_type, value=True):
        continue
    if(len(songs) == 0):
        continue
    st.write(f'#### {recommendation_type.title()}')
    with st.container():
        for song in songs:
            st.write(f'- {song["track_name"]} - {song["track_artist"]}')
            st.button("listen", key=str(song['index'])+recommendation_type, on_click=change_song, args=(song['index'],))
