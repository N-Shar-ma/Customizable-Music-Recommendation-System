import streamlit as st
from  urllib import parse
from recommender import hybrid_recommend, get_metadata

st.set_page_config(page_title='Customizable Music Recommendation System', page_icon='🎶')

def change_song(index):
    st.session_state['current_song_index'] = index

if 'current_song_index' not in st.session_state:
    st.session_state['current_song_index'] = 11726

st.title('🎶 Customizable Music Recommendation System 🎶')

option1 = 'Keep up with what\'s trending'
option2 = 'Discover hidden gems'
mode = st.sidebar.selectbox('What kind of song recommendations would you like?', (option1, option2))
if(mode == option1):
    prioritisePopular = True
else:
    prioritisePopular = False

recommendations_count = st.sidebar.slider('Upto how many of each kind of recommendations would you like? (lesser means more accurate but more means more variety!)', min_value=1, max_value=10)

current_song_metadata = get_metadata(st.session_state['current_song_index'])

st.write('##', current_song_metadata['track_name'], ' - ', current_song_metadata['track_artist'])
st.write('[Search on Google to listen](' + 'https://google.com/search?q=' + parse.quote(current_song_metadata['track_name'] + ' ' + current_song_metadata['track_artist']) + ')')
with st.expander('Show lyrics'):
    st.write(current_song_metadata['lyrics'])

recommendations = hybrid_recommend(st.session_state['current_song_index'], recommendations_count , prioritisePopular=prioritisePopular)

for recommendation_type, songs in recommendations.items():
    if(len(songs) == 0):
        continue
    st.write('####', recommendation_type.upper())
    with st.container():
        for song in songs:
            st.write('- ', song['track_name'], ' - ', song['track_artist'])
            st.button("listen", key=str(song['index'])+recommendation_type, on_click=change_song, args=(song['index'],))