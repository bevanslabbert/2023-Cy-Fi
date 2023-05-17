import time
import gym
from gym.spaces import Discrete, Box
from Game.action import Action
from GameConnection import send


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
        self.action_space = Discrete(len(Action))

        # Start state
        self.state = state["heroWindow"]
        self.collected = state["collected"]
        pass

    def step(self, action, state, game_conn):
        send.send_action(game_conn, action.BotCommand(state.bot_id, action))

        # Sleep until next tick updates hero state
        while self.state == state.bot_state["heroWindow"]:
            time.sleep(0.5)

        # If got a collectible, positive reward
        if state.bot_state["collected"] > self.payload["collected"]:
            reward += 1

        # If passed level, positive reward
        if state.bot_state["level"] > self.payload["level"]:
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
        # Constants
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 600
        BLOCK_SIZE = 40
        GRID_WIDTH = 10
        GRID_HEIGHT = 16

        # Initialize Pygame
        pygame.init()
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Block Renderer")

        for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            # Calculate block position
            x = col * BLOCK_SIZE
            y = row * BLOCK_SIZE

            # Get block color based on row number
            if col % 2 == 0:
                if row % 2 == 0:
                    block_color = (255, 0, 0)
                else:
                    block_color = (0, 255, 0)
            else:
                if row % 2 == 0:
                    block_color = (0, 255, 0)
                else:
                    block_color = (255, 0, 0)

            # Draw block
            pygame.draw.rect(window, block_color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

            # Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((255, 255, 255))

    # Render the grid
    render_grid()

    # Update the display
    pygame.display.update()

    # Quit the game
    pygame.quit()

        pass
