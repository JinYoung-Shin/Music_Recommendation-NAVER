import re
import apimanager
import operator

class APIError(Exception):
    pass



def get_raw_text(text):
    q = re.sub('\([^()]+\)', '', text)
    q = re.sub('\-.*', '', q)
    return q.strip()

def tag_search(self, option):
    track_ids = []
    key = self.apiManager.map_type(option)
    search_result1 = self.apiManager.search_tag(key)['tags']
    tag_id = str(search_result1[0]['tagId'])
    search_result2 = self.apiManager.get_tag_track(tag_id)
    string = search_result2['contentIds'].split(',')
    for i in string:
        track_ids.append(i[6:])
    return track_ids


class TypesAPI:
	
    def __init__(self, apiManager):
        if isinstance(apiManager, str):
            apiManager = apimanager.APIManager(apiManager)
        assert isinstance(apiManager, apimanager.APIManager)
        self.apiManager = apiManager

    # album, artist, track
    def album(self):
        track_ids = []
        album = self.apiManager.map_type('album')
        search_result = self.apiManager.search_track(album)
        for obj in search_result['tracks']:
            track_ids.append(str(obj['trackId']))
        return track_ids

    def artist(self):
        track_ids = []
        artist = self.apiManager.map_type('artist')
        search_result = self.apiManager.search_track(artist)
        for obj in search_result['tracks']:
            track_ids.append(str(obj['trackId']))
        return track_ids

    def track(self):
        track = self.apiManager.map_type('track')
        search_result = self.apiManager.search_track(track)

        #titles = [get_raw_text(rep['trackTitle'])]
        rep = search_result['tracks'][0]
        artists = [get_raw_text(rep['artists'][0]['artistName'])]
        # 초기화
        track_ids = []

        for obj in search_result['tracks']:
            artist_name = obj['artists'][0]['artistName']
            track_title = obj['trackTitle']
            if artist_name not in artists and track_title.find('Inst') == -1 and track_title.find("mr") == -1:
                artists.append(artist_name)
                track_ids.append(str(obj['trackId']))

        return track_ids

    def album_artist(self):
        track_ids = []
        album = self.apiManager.map_type('album')[0]
        artist = self.apiManager.map_type('artist')[0]
        query = album + " " + artist
        print ("typesApi query: ", query)
        search_result = self.apiManager.search_track(query)

        for obj in search_result['tracks']:
            track_ids.append(str(obj['trackId']))
        return track_ids

    def album_track(self):
        album = self.apiManager.map_type('album')[0]
        track = self.apiManager.map_type('track')[0]
        query = album + " " + track
        search_result = self.apiManager.search_track(query)

        rep = search_result['tracks'][0]
        artists = [get_raw_text(rep['artists'][0]['artistName'])]
        # 초기화
        track_ids = []

        for obj in search_result['tracks']:
            artist_name = obj['artists'][0]['artistName']
            track_title = obj['trackTitle']
            if artist_name not in artists and track_title.find('Inst') == -1 and track_title.find("mr") == -1:
                artists.append(artist_name)
                track_ids.append(str(obj['trackId']))

        return track_ids

    def artist_track(self):
        artist = self.apiManager.map_type('artist')[0]
        track = self.apiManager.map_type('track')[0]
        query = artist + " " + track
        search_result = self.apiManager.search_track(query)

        rep = search_result['tracks'][0]
        artists = [get_raw_text(rep['artists'][0]['artistName'])]

        # 초기화
        track_ids = []

        for obj in search_result['tracks']:
            track_title = obj['trackTitle']
            artist_name = obj['artists'][0]['artistName']
            if artist_name not in artists and track_title.find('Inst') == -1 and track_title.find("MR") == -1:
                artists.append(artist_name)
                track_ids.append(str(obj['trackId']))

        print(track_ids)
        return track_ids

    def album_artist_track(self):
        album = self.apiManager.map_type('album')[0]
        artist = self.apiManager.map_type('artist')[0]
        track = self.apiManager.map_type('track')[0]
        query = album + " " + artist + " " + track
        search_result = self.apiManager.search_track(query)


        rep = search_result['tracks'][0]
        artists = [get_raw_text(rep['artists'][0]['artistName'])]
        # 초기화
        track_ids = []

        for obj in search_result['tracks']:
            artist_name = obj['artists'][0]['artistName']
            track_title = obj['trackTitle']
            if artist_name not in artists and track_title.find('Inst') == -1 and track_title.find("mr") == -1:
                artists.append(artist_name)
                track_ids.append(str(obj['trackId']))

        return track_ids

    # context 기본
    def artistGender(self):
        return tag_search(self, 'artistGender')

    def artistType(self):
        return tag_search(self, 'artistType')

    def context(self):
        return tag_search(self, 'context')

    def country(self):
        return tag_search(self, 'country')

    def genre(self):
        return tag_search(self, 'genre')

    def instrument(self):
        return tag_search(self, 'instrument')

    def language(self):
        return tag_search(self, 'language')

    def lyricist(self):
        return tag_search(self, 'lyricist')

    def movie(self):
        return tag_search(self, 'movie')

    def time(self):
        return tag_search(self, 'time')

    def tvProgram(self):
        return tag_search(self, 'tvProgram')

    # context 심화
    def album_context(self):
        return tag_search(self, 'context')

    def artist_context(self):
        # 방법 1 : context로 track_ids 가져온 후 각 id별로 artist 일치 여부 검사하는 방법
        artist = self.apiManager.map_type('artist')
        track_ids = tag_search(self, 'context')
        for i in track_ids:
            track_detail = self.apiManager.get_track(i)
            if(track_detail['tracks'][0]['artists'][0]['artistName'] == artist) :
                return i

        # 방법 2 : API가 부족하다 ...

        return False

    def artist_genre(self):
        return 1

    def artistType_context(self):
        return 1

    def context_track(self):
        return TypesAPI.track(self)




    def exclude_artist_album(self):
        track_ids = []
        album = self.apiManager.map_type('album')[0]
        artist = self.apiManager.map_type('artist')[0]

        album_result = self.apiManager.search_album(artist) # 앨범 리스트
 
        for _album_id in album_result['albums'] :
            album_id = _album_id['albumId']
            search_result = self.apiManager.get_album_tracks(album_id)
            for obj in search_result['tracks']:
                #if obj['trackId'] != played_track_ids
                track_ids.append(str(obj['trackId']))
				
        return track_ids

# 아티스트 재생했을때, 나온곡 말고 다른곡. -> 앨범을 돌면서 재생(나온 trackid 제외)
# 앨범 재생했을때 -> 다른 앨범 재생 (위에꺼와 병합 가능.) 
# 아티스트는 고정. 앨범만 순환(어떻게 순환하지? 랜덤? 순차적으로?)
# 앨범 돌면서 재생된 list에 있는 트랙은 제외함. (for문으로 모든 current_track_ids list 비교하면서 지나가게)



    def update_tracklist(self, playedlist):
        tracks = ','.join(playedlist)
        json_data = self.apiManager.get_multiple_tracks(tracks)
        genres = [track['album']['albumGenres'] for track in json_data['tracks']]

        genre_dic = {}
        for genre in genres:
            g = genre.split(',')
            for _g in g:
                genre_dic[_g] = genre_dic.get(_g, 0) + 1

        top_genre = sorted(genre_dic.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        top100_data = self.apiManager.get_genre_top100(top_genre)

        track_ids = [str(track['trackId']) for track in top100_data['chart']['tracks']]
        return track_ids

