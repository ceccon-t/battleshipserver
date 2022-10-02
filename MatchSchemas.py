from pydantic import BaseModel
from GameConstants import *

class MatchRequest(BaseModel):
    sessionKey: str 
    myId: str 
    turn: int 
    myLastAction: str 

class MatchResponse(BaseModel):
    sessionKey: str 
    turn: int 
    lastAction: str 
    lastActor: str 
    