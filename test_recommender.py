from recommender import hybrid_recommend, get_metadata

# test if number of each recommendation is less than or equal to the given count
def test_recommend_output():
    hybrid_recommend_output = hybrid_recommend(0, 5, True)
    for songs in hybrid_recommend_output.values():
        assert len(songs) <= 5

# test if metadata for each song includes the necessary keys
def test_metadata_output():
    get_metadata_output = get_metadata(0)
    assert {'track_name', 'track_artist', 'lyrics'}.issubset(get_metadata_output)
