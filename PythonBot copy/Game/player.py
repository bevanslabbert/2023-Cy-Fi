from GameConnection import connection, send
from Game.action import Action


class Player:
    def __init__(self, state):
        self.heroWindow = payload["heroWindow"]
        self.x = payload["x"]
        self.y = payload["y"]
        self.collected = payload["collected"]

    def update(self, payload):
        self.heroWindow = payload["heroWindow"]
        self.x = payload["x"]
        self.y = payload["y"]
        self.collected = payload["collected"]
        self.printGame()
        return

    def printGame(self):
        # Function to print game in window
        pass

    def computeNextMove(self):
        return Action.LEFT
    
    def _getHeroWindow(self):
        return self.heroWindow

    def _getCollected(self):
        return self.collected
    
    def _getX(self):
        return self.x

    def _getY(self):
        return self.y