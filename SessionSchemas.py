from pydantic import BaseModel
from GameConstants import *

class SessionRequest(BaseModel):
    sessionKey: str 
    
class SessionResponse(BaseModel):
    granted: bool
    sessionKey: str 
    yourId: str

def getEmptySessionDict():
    s = dict()
    s[SESSION_KEY_FIELD] = ''
    s[PLAYER_1_ID] = PLAYER_VACANT
    s[PLAYER_2_ID] = PLAYER_VACANT
    s[PLAYER_1_PATROL_FIELD] = ""
    s[PLAYER_1_DESTROYER_FIELD] = ""
    s[PLAYER_1_BATTLESHIP_FIELD] = ""
    s[PLAYER_1_CARRIER_FIELD] = ""
    s[PLAYER_2_PATROL_FIELD] = ""
    s[PLAYER_2_DESTROYER_FIELD] = ""
    s[PLAYER_2_BATTLESHIP_FIELD] = ""
    s[PLAYER_2_CARRIER_FIELD] = ""
    s[TURN_FIELD] = 0
    s[LAST_ACTION_FIELD] = ""
    s[LAST_ACTOR_FIELD] = "player2"
    return s

