import time

import gym
from gym.spaces import Discrete, Box
from Game.action import Action
from GameConnection import send

class Environment(gym.Env):
    def __init__(self, player):
        # Set player as attribute for easy access to environment states
        self.player = player
        # Actions we can take
        self.action_space = Discrete(len(Action))
        # Hero window
        self.observation_space = spaces.Dict({
            'x': spaces.Discrete(10000),
            'y': spaces.Discrete(10000),
            'level': spaces.Discrete(5)
        })
        # Start state
        self.state = player._getHeroWindow()
        pass

    def step(self, action, state, game_conn):
        send.send_action(game_conn, action.BotCommand(state.bot_id, action))
        
        # Sleep until next tick updates hero state
        while(self.state == state.bot_state["heroWindow"]):
            time.sleep(0.5)
        
        # If passed level, positive reward

        # If touching hazard, negative reward

        # Placeholder for info
        info = {}
        # return state (heroWindow), reward (int), done (bool, terminate?), info(object of info)

        pass

    def reset(self):
        # Reset connection to runner, and execute constructor code
        # return state (heroWindow)
        pass

    def render(self):
        pass
