import streamlit as st
from recommender import hybrid_recommend, get_metadata

option1 = 'Keep up with what\'s trending'
option2 = 'Discover hidden gems'
mode = st.selectbox('What kind of song recommendations would you like?', (option1, option2))
if(mode == option1):
    prioritisePopular = True
else:
    prioritisePopular = False

current_song_index = 11726
current_song_metadata = get_metadata(current_song_index)

st.write('#', current_song_metadata['track_name'])
st.write('##', current_song_metadata['track_artist'])
st.write(current_song_metadata['lyrics'])

recommendations = hybrid_recommend(current_song_index, prioritisePopular=prioritisePopular)

for recommendation_type, songs in recommendations.items():
    st.write('###', recommendation_type.upper())
    for song in songs:
        st.write(song['track_name'], ' - ', song['track_artist'])
        new_song = st.button("listen", key=song['index'])
        # if new_song:
            # todo