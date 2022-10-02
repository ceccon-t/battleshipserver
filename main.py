from fastapi import FastAPI
from GameConstants import *
from MatchSchemas import MatchRequest
from SessionSchemas import *
from SetupSchemas import *

app = FastAPI()

app.served = 0
app.matchSessions = dict()


@app.get("/")
async def root():
    return {"health": "Alive!"}

@app.get("/count")
async def c():
    app.served += 1
    return {"served": app.served}

@app.get("/allSessions")
async def allSessions():
    return app.matchSessions

@app.get("/resetSessions")
async def resetSessions():
    app.matchSessions = dict()
    return app.matchSessions

@app.post("/sessionRequest")
async def sessionReq(r: SessionRequest):
    sresp = dict()
    sresp['granted'] = False
    sresp['sessionKey'] = r.sessionKey
    sresp['yourId'] = ""
    if r.sessionKey == 'bat':
        return sresp

    requestedSession = getEmptySessionDict()
    if r.sessionKey not in app.matchSessions:
        requestedSession[PLAYER_1_ID] = PLAYER_JOINED
        sresp['yourId'] = PLAYER_1_ID
    else:
        requestedSession = app.matchSessions[r.sessionKey]
        if requestedSession[PLAYER_2_ID] != PLAYER_VACANT:
            return sresp
        requestedSession[PLAYER_2_ID] = PLAYER_JOINED
        sresp['yourId'] = PLAYER_2_ID
    
    requestedSession[SESSION_KEY_FIELD] = r.sessionKey
    app.matchSessions[r.sessionKey] = requestedSession

    sresp["granted"] = True 
    return sresp

@app.post("/setup")
async def setup(r: SetupRequest):
    if r.sessionKey not in app.matchSessions:
        return dict()
    thisSession = app.matchSessions[r.sessionKey]
    if thisSession[r.myId] == PLAYER_IS_SET:
        return thisSession
    if r.myId == PLAYER_1_ID:
        thisSession[PLAYER_1_PATROL_FIELD] = r.patrol
        thisSession[PLAYER_1_DESTROYER_FIELD] = r.destroyer
        thisSession[PLAYER_1_BATTLESHIP_FIELD] = r.battleship
        thisSession[PLAYER_1_CARRIER_FIELD] = r.carrier
        thisSession[PLAYER_1_ID] = PLAYER_IS_SET
    else:
        thisSession[PLAYER_2_PATROL_FIELD] = r.patrol
        thisSession[PLAYER_2_DESTROYER_FIELD] = r.destroyer
        thisSession[PLAYER_2_BATTLESHIP_FIELD] = r.battleship
        thisSession[PLAYER_2_CARRIER_FIELD] = r.carrier
        thisSession[PLAYER_2_ID] = PLAYER_IS_SET
    app.matchSessions[r.sessionKey] = thisSession
    return thisSession

@app.post("/match")
async def match(r: MatchRequest):
    if r.sessionKey not in app.matchSessions:
        return dict()
    thisSession = app.matchSessions[r.sessionKey]
    if (thisSession[TURN_FIELD] >= r.turn):
        return thisSession
    else:
        thisSession[TURN_FIELD] = r.turn
        thisSession[LAST_ACTOR_FIELD] = r.myId
        thisSession[LAST_ACTION_FIELD] = r.myLastAction
        app.matchSessions[r.sessionKey] = thisSession
    return thisSession

