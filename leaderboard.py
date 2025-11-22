from datetime import datetime,timedelta

def init_leaderboard()->dict[str,timedelta]:
    return {}


def add_player(leaderboard:dict[str,timedelta],player_name:str)->bool:
    if player_name in leaderboard:
        return False
    leaderboard.update({player_name:None})
    return True

def add_run(leaderboard:dict[str,timedelta],player_name:str,time:timedelta)->int:
    if time.total_seconds()<0:
        return 1
    if player_name not in leaderboard:
        return 2
    
    if leaderboard[player_name]==None or leaderboard[player_name]> time:
        leaderboard.update({player_name:time})
    return 0
