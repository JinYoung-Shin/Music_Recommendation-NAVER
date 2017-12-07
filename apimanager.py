import requests


class APIManager:

    def __init__(self, sentence):
        self.server = "http://tools.nozzle.naver.com:8080/hackday"
        self.sentence = sentence
        self.speech_analysis()


    # 발화 분석
    def speech_analysis(self):
        url = self.server + "/analysis"
        params = {'content':self.sentence}
        r = requests.get(url, params=params)
        self.data = r.json()


    def isin_artist(self):
        for seed in self.data['seeds']:
            if(seed['type'] == 'artist'):
                return True
        return False



    # 아티스트 검색(Search artist)
    def search_artist(self, artist):
        url = f"{self.server}/music/search__artist"
        params = {'query':artist}
        r = requests.get(url, params=params)
        return r.json()


    # 앨범 검색(Search album)
    # input can be either artist/album
    def search_album(self, artist):
        url = f"{self.server}/music/search__album"
        params = {'query':artist}
        r = requests.get(url, params=params)
        return r.json()


    # 트랙 검색(Search track)
    # input can be either track/artist/album
    def search_track(self, track):
        url = f"{self.server}/music/search__track"
        params = {'query':track}
        r = requests.get(url, params=params)
        return r.json()


    # 가사 검색
    def search_lyric(self, lyric):
        url = f"{self.server}/music/search__lyric"
        params = {'query':lyric}
        r = requests.get(url, params=params)
        return r.json()


    # 트랙 조회(get track by trackId)
    def get_track(self, trackId):
        url = f"{self.server}/music/tracks__{trackId}"
        r = requests.get(url)
        return r.json()


    # 앨범 조회(get album by albumId)
    def get_album(self, albumId):
        url = f"{self.server}/music/album__{albumId}"
        r = requests.get(url)
        return r.json()


    # 앨범의 트랙 조회(get tracks by albumId)
    def get_album_tracks(self, albumId):
        url = f"{self.server}/music/album__{albumId}__tracks"
        r = requests.get(url)
        return r.json()


    # 아티스트 조회(get artist by artistId)
    def get_artist(self, artistId):
        url = f"{self.server}/music/musician__artist__{artistId}"
        r = requests.get(url)
        return r.json()


    # 아티스트의 트랙 조회(Search track by artistId)
    def get_artist_tracks(self, artistId):
        url = f"{self.server}/music/musician__artist__{artistId}__tracks"
        r = requests.get(url)
        return r.json()


    # 아티스트의 앨범 조회(Search album by artistId)
    def get_artist_albums(self, artistId):
        url = f"{self.server}/music/musician__artist__{artistId}__albums"
        r = requests.get(url)
        return r.json()


    # 태그 검색
    def search_tag(self, tag):
        url = f"{self.server}/music/opentag__tags"
        params = {'name':tag}
        r = requests.get(url, params=params)
        return r.json()


    # 태그 id로 곡 조회
    def get_tag_track(self, tagId):
        url = f"{self.server}/music/opentag__tag__{tagId}__contentIds"
        r = requests.get(url)
        return r.json()


    # Top 100
    def get_chart_top100(self):
        url = f"{self.server}/music/chart__domain__domestic__top100__trackChart"
        r = requests.get(url)
        return r.json()


    # 최신곡
    def get_chart_new_release(self):
        url = f"{self.server}/music/chart__domain__domestic__newrelease__trackChart"
        r = requests.get(url)
        return r.json()


    # 여러곡 조회
    def get_multiple_tracks(self, trackIds):
        url = f"{self.server}/music/tracks__{trackIds}"
        r = requests.get(url)
        return r.json()


    # 장르별top100 조회
    # genre = " 발라드"/" 댄스"/...
    def get_genre_top100(self, genre):
        genre_dic = {" 발라드":"K01", " 댄스":"K02", " 랩/힙합":"K03", " 인디뮤직":"K04", " 트로트":"K05", " 팝":"P01", " 힙합":"P03"}
        url = f"{self.server}/music/chart__genre__{genre_dic[genre]}__top100__trackChart"
        r = requests.get(url)
        return r.json()

    # Map
    def map_type(self, key):
        for seed in self.data['seeds']:
            if seed['type'] == key:
                list = []
                for param in seed['params']:
                    list.append(param['value'])
                return list
        return []

    def get_tracks(self, track_ids):
        url = f"{self.server}/music/tracks__"
        query = url
        for track_id in track_ids:
            query += track_id + ','
        
        json = requests.get(query).json()

        result =''
        for track in json['tracks']:
            result += 'TITLE : ' + track['trackTitle'] + "|| ARTIST :"
            for artist in track['artists']:
                result += artist['artistName'] + " "
            result += '||'
            result += 'ALBUM : ' + track['album']['albumTitle']
            print(result)
            result = ''