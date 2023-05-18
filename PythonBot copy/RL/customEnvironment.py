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
        pass

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

        self.state = state
        return state.bot_state["heroWindow"], reward, False, info

    def reset(self):
        # Reset connection to runner, and execute constructor code
        # return state (heroWindow)
        pass

    def render(self):
        # Constants
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 600
        BLOCK_SIZE = 40
        GRID_WIDTH = 10
        GRID_HEIGHT = 16

        # Initialize Pygame
        pygame.init()
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Melkman")

        # Game loop
        running = True
        # while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the window
            window.fill((255, 255, 255))

            # Render the grid
            for row in range(GRID_HEIGHT):
                for col in range(GRID_WIDTH):
                    # Calculate block position
                    x = col * BLOCK_SIZE
                    y = row * BLOCK_SIZE

                    # Get block color based on row number
                    if self.state.bot_state['heroWindow'] == '0':
                        pass
                    elif self.state.bot_state['heroWindow'] == '1':
                        # rgb for brown
                        block_color = 
                    elif self.state.bot_state['heroWindow'] == '2':
                        # rgb for gold
                        block_color = 
                    elif self.state.bot_state['heroWindow'] == '3':
                        block_color = (255,0,0)
                    elif self.state.bot_state['heroWindow'] == '4':
                        block_color = (0,255,0)
                    elif self.state.bot_state['heroWindow'] == '5':
                        block_color = (0,0,255)
                    elif self.state.bot_state['heroWindow'] == '6':
                        # orange
                        block_color = 
                    
                    # Draw block
                    pygame.draw.rect(
                        window, block_color, (x, y, BLOCK_SIZE, BLOCK_SIZE)
                    )

            # Update the display
            pygame.display.update()

        # Quit the game
        pygame.quit()
