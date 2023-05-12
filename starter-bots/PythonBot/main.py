import sys
import time
from pprint import pprint
from GameConnection import connection, send
from Game import action

if __name__ == "__main__":
    game_conn, state = connection.start()

    # Main run loop is here!
    try:
        while state.connected:
            # Print out the bot state.
            print(state.bot_state)

            time.sleep(2)
            
            # Just jumpiing continuously 
            send.send_action(
                game_conn, 
                action.BotCommand(state.bot_id, action.Action.UP)
            )

    except KeyboardInterrupt:
        game_conn.stop()
        sys.exit(0)
