from apimanager import APIManager
import typesAPI

current_track_id = []
playlist_track_id = []
current_search_data = []



#album을 수행한 경우 : 해당 artist의 다른 앨범을 재생
#album + artist를 수행한 경우 : 해당 artist의 다른 앨범을 재생
def input_controller(t):
	seeds = t.apiManager.data['seeds']
	type_list = []
    
	for seed in seeds:
		type_list.append(seed['type'])
    
	type_list.sort()
	method_name = '_'.join(type_list)
	f = getattr(t, method_name)
	return f()

conversation_mode = input("0 : Conversation Mode \nDefault : Direct Service Mode ")

while True :
	text = input("Input Sentence(Empty Sentence Power Off) : ")
	api_m = APIManager(text)
	t = typesAPI.TypesAPI(api_m)

	if text == "" :
		break
	elif text == "다른 노래~~~" :
		if playlist_track_id == [] :
			print("input agiain")
			continue
		playlist_track_id = list.pop(0)
		list.append(playlist_track_id)
		api_m.get_tracks(list)
		current_track_id.append(list[0])
	list = input_controller(t)

	if list.pop(0) == 0: #list에 값이 없는경우
		print("error! no tracks")
		continue
	else : #list가 있는 경우
		api_m.get_tracks(list)
		current_track_id.append(list[0])
	    # 함수 썻을 때 케이스 별로 나누고
		# 여기서 재생한 목록만 playlistID에 넣어라...
		# playlist 추가해주는 알고리즘 !!!



			#else: # other case

			#if 트랙 빈경우
	
def input_controller2(t):
	seeds = t.apiManager.data['seeds']
	type_list = []
    
	for seed in seeds:
		type_list.append(seed['type'])
    
	type_list.sort()
	method_name = "exclude_artist_album"
	f = getattr(t, method_name)
	return f()
	
#text = input("input text : ")
text = ("아이유 1집 틀어줘")
print ("text : " ,text)

api_m = APIManager(text)
t = typesAPI.TypesAPI(api_m)
list = input_controller(t)

played_track_ids = list

if list.pop(0) == 0: #list에 값이 없는경우
	print("error! no tracks")
else : #list가 있는 경우
	api_m.get_tracks(list)
	current_track_id.append(list[0])
	#text = input("input text :")
	context = ("다음 추천")
	
	#while True:
	if context == "다른 노래":	
		_current_track_id = list.pop(0)
		list.append(_current_track_id)
		
		api_m.get_tracks(list)
		current_track_id.append(list[0])
		text = input("input text :")
			
	elif context == "다음 추천":
		print("여기서부터 다음 추천")
		api_m = APIManager(text)
		t = typesAPI.TypesAPI(api_m)
		list = input_controller2(t)
		api_m.get_tracks(list)
		#t.exclude_artist_album()
			
			
			
			
			
			
			
			
			
			
	
