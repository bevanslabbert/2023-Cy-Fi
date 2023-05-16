import time

import gym
from gym.spaces import Discrete, Box
from Game.action import Action
from GameConnection import send

class Environment(gym.Env):

    def __init__(self,state):

        self.payload = state

        # Actions we can take
        self.action_space = Discrete(len(Action))

        # Hero window
        self.observation_space = spaces.Dict({
            'x': spaces.Discrete(10000),
            'y': spaces.Discrete(10000),
            'level': spaces.Discrete(5)
        })
        
        # Start state
        self.state = state["heroWindow"]
        self.collected = state["collected"]
        pass

    def step(self, action, state, game_conn):
        send.send_action(game_conn, action.BotCommand(state.bot_id, action))
        
        # Sleep until next tick updates hero state
        while(self.state == state.bot_state["heroWindow"]):
            time.sleep(0.5)
        
        # If got a collectible, positive reward
        if(state.bot_state["collected"] > self.payload["collected"]):
            reward += 1

        # If passed level, positive reward
        if(state.bot_state["level"] > self.payload["level"]):
            reward += 100

        # If touching hazard, negative reward


        # Placeholder for info
        info = {}
        return state.bot_state["heroWindow"], reward, False, info


    def reset(self):
        # Reset connection to runner, and execute constructor code
        # return state (heroWindow)
        pass

    def render(self):
        pass
