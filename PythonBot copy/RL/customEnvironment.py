import time
import gym
from gym.spaces import Discrete, Box
from Game.action import Action, BotCommand
from GameConnection import send
import numpy as np
import pygame


class Environment(gym.Env):
    def __init__(self, state):
        self.observation_shape = (10, 16)

        # Define the lower and upper bounds for the integer values
        self.low = 0
        self.high = 6

        self.init = False

        # Create a custom observation space
        self.observation_space = Box(
            low=self.low, high=self.high, shape=self.observation_shape, dtype=np.int32
        )
        self.payload = state

        # Actions we can take
        self.action_space = Discrete(12)

        # Start state
        self.state = state.bot_state["heroWindow"]
        self.collected = state.bot_state["collected"]
        
        # Constants
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 600
        self.BLOCK_SIZE = 40
        self.GRID_WIDTH = len(self.state)
        self.GRID_HEIGHT = len(self.state[0])

        # Initialize Pygame
        self.init = True
        pygame.init()
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Melkman")

        self.window.fill((255, 255, 255))


    def step(self, action, state, game_conn):
        send.send_action(game_conn, BotCommand(state.bot_id, action))
        reward = 0
        # Sleep until next tick updates hero state
        while self.state == state.bot_state["heroWindow"]:
            time.sleep(0.5)

        # If got a collectible, positive reward
        if state.bot_state["collected"] > self.payload.bot_state["collected"]:
            reward += 1

        # If passed level, positive reward
        if state.bot_state["currentLevel"] > self.payload.bot_state["currentLevel"]:
            reward += 100

        # If touching hazard, negative reward

        # Placeholder for info
        info = {}

        self.state = state.bot_state['heroWindow']
        self.payload = state
        return state.bot_state["heroWindow"], reward, False, info

    def reset(self):
        # Reset connection to runner, and execute constructor code
        # return state (heroWindow)
        pass

    def render(self):
        if self.payload != None:
            
            # Game loop
            running = True
            # while running:
                # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the window
            # self.window.fill(0, 0, 0)

            # Render the grid
            for row in range(self.GRID_WIDTH):
                for col in range(self.GRID_HEIGHT):
                    # Calculate block position
                    x = col * self.BLOCK_SIZE
                    y = row * self.BLOCK_SIZE
                    val =  self.payload.bot_state['heroWindow'][row][col]
                    # Get block color based on row number
                    if val == 0:
                        block_color = (255, 255, 255)
                    elif val == 1:
                        # rgb for brown
                        block_color = (150, 75, 0)
                    elif val == 2:
                        # rgb for gold
                        block_color = (225,215,0)
                    elif val == 3:
                        # red
                        block_color = (255,0,0)
                    elif val == 4:
                        # green
                        block_color = (0,255,0)
                    elif val == 5:
                        # blue
                        block_color = (0,0,255)
                    elif val == 6:
                        # orange
                        block_color = (255,165,0)
                    else:
                        block_color = (0,0,0)
                        
                    # Draw block
                    pygame.draw.rect(
                        self.window, block_color, (x, y, self.BLOCK_SIZE, self.BLOCK_SIZE)
                    )

            # Update the display
            pygame.display.update()

            # Quit the game
            # pygame.quit()
