from dataclasses import dataclass

class Action:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UPLEFT = 5
    UPRIGHT = 6
    DOWNLEFT = 7
    DOWNRIGHT = 8
    DIGDOWN = 9
    DIGLEFT = 10
    DIGRIGHT = 11

@dataclass 
class BotCommand:
    botId: str
    action: Action
