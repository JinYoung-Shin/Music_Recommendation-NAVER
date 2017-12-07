import time
from apimanager import APIManager
import typesAPI

def input_controller(t):
    seeds = t.apiManager.data['seeds']
    type_list = []
    
    for seed in seeds:
        type_list.append(seed['type'])
    
    type_list.sort()
    method_name = '_'.join(type_list)
    f = getattr(t, method_name)

    return f()
	
	
def input_controller2(t):
	seeds = t.apiManager.data['seeds']
	type_list = []
    
	for seed in seeds:
		type_list.append(seed['type'])
    
	type_list.sort()
	method_name = "exclude_artist_album"
	f = getattr(t, method_name)
	return f()

playedlist = []
play = True

print('test')
#usr_input = input("# Clovia # ")
while play:
    usr_input = '거짓말 틀어줘'
    api_m = APIManager(usr_input)
    t = typesAPI.TypesAPI(api_m)
    track_ids = input_controller(t)
    print('test')
    print(type(api_m.isin_artist()))
    if(api_m.isin_artist()):
        print('artist')
        api_m = APIManager(usr_input)
        t = typesAPI.TypesAPI(api_m)
        list = input_controller2(t)
        api_m.get_tracks(list)
    else:
        while len(track_ids) > 0 :
            current_track = track_ids.pop(0)
            playedlist.append(current_track)
            api_m.get_tracks([current_track])
            time.sleep(1)
            if len(track_ids) < 3 :
                similar = t.update_tracklist(playedlist)

                track_ids.extend(similar)
        
        #play_continue = input("다른 곡을 틀어드릴까요?")




    if len(track_ids) == 0:
        play = False
    

playedlist = []
play = True
