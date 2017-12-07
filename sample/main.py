from apimanager import APIManager
import typesapi


api_m = APIManager('아이유 1집 틀어줘')
t = typesapi.TypesAPI(api_m)

#t.album_artist()

api_m = APIManager("아이유 틀어줘")
t = typesapi.TypesAPI(api_m)

#t.artist()

api_m.get_tracks(['2010362', '4234463'])

