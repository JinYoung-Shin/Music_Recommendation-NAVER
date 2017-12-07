from apimanager import APIManager
from typesAPI import TypesAPI

import pytest


@pytest.fixture
def api_manager():
    return APIManager('')


def test_api_call(api_manager):
    assert api_manager.search_artist('아이유')
    assert api_manager.search_album('아이유 3집')
    assert api_manager.search_track('가을아침')
    assert api_manager.search_lyric('와리가리')
    assert api_manager.get_track(1)
    assert api_manager.get_album(1)
    assert api_manager.get_album_tracks(1)
    assert api_manager.get_artist(1)
    assert api_manager.get_artist_tracks(1)
    assert api_manager.get_artist_albums(1)
    assert api_manager.search_tag("신나는")
    assert api_manager.get_tag_track(13245)
    assert api_manager.get_chart_top100()
    assert api_manager.get_chart_new_release()
    assert api_manager.get_multiple_tracks("1,2,3,4")
    assert api_manager.get_genre_top100(" 발라드")
    assert api_manager.search_artist('너의 의미')


def test_types_api_artist():
    t = TypesAPI('아이유 노래')
    assert t.artist()
