import sys
import time
from pprint import pprint
from GameConnection import connection, send
from Game import action
from Game.player import Player

if __name__ == "__main__":
    game_conn, state = connection.start()

    melkMan = Player()
    # Main run loop is here!
    try:
        while state.connected:
            # Print out the bot state.
            if state.bot_state != None:
                print(state.bot_state)
                melkMan.update(state.bot_state)

            time.sleep(1)

            nextMove = melkMan.computeNextMove()

            send.send_action(game_conn, action.BotCommand(state.bot_id, nextMove))

    except KeyboardInterrupt:
        game_conn.stop()
        sys.exit(0)
