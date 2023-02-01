import copy

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["video_game"]

def insert_player(player_obj, check_for_duplicate=True):
    if check_for_duplicate:
        duplicate_player = db.players.find_one({"name": player_obj.name})
        if duplicate_player != None:
            return duplicate_player["_id"]

    player_dict = copy.deepcopy(vars(player_obj))
    item_dict_list = []

    for item_obj in player_dict["items"]:
        item_dict = vars(item_obj)
        item_dict_list.append(item_dict)

    player_dict["items"] = item_dict_list

    return db.players.insert_one(player_dict).inserted_id
