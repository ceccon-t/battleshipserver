from pydantic import BaseModel

class SetupRequest(BaseModel):
    sessionKey: str 
    myId: str 
    patrol: str 
    destroyer: str 
    battleship: str 
    carrier: str 

class SetupResponse(BaseModel):
    sessionKey: str 
    player1: str 
    player2: str 
    patrolPlayer1: str 
    destroyerPlayer1: str 
    battleshipPlayer1: str 
    carrierPlayer1: str 
    patrolPlayer2: str 
    destroyerPlayer2: str 
    carrierPlayer2: str 

