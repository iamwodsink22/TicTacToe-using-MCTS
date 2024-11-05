from fastapi import FastAPI
from mcts import MCTS
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from env import Env
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow only this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)
class BoardModel(BaseModel):
    state: list
    symbol:str

@app.post('/move')
def get_move(board:BoardModel):
    states=board.state
    
    for i in range(len(states)):
        if states[i]==0:
            states[i]=0
        elif states[i]==board.symbol:
            states[i]=-1
        else:
            states[i]=1
    z=np.array(states).reshape(3, 3)
    env = Env(z.T, 1)
    action = MCTS(env).simulate(1)
    index=action[1]*3+action[0]
    return {'action':int(index)}
    
