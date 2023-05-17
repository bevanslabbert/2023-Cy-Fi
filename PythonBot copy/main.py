import sys
import time
from pprint import pprint
from GameConnection import connection, send
from Game import action
from Game.player import Player
from RL.customEnvironment import Environment

if __name__ == "__main__":
    game_conn, state = connection.start()
    while state.connected:
        if state.bot_state != None:
            # Environment with agent
            print(state)
            env = Environment(state)

            # Perform 10 runs
            runs = 10
            for run in range(1, runs + 1):
                # state = env.reset()
                done = False
                score = 0

                while not done:
                    # env.render()
                    time.sleep(1)
                    action = env.action_space.sample()
                    n_state, reward, done, info = env.step(action, state, game_conn)
                    score += reward

                print("Episode:{} Score:{}".format(run, score))

    # # Main run loop is here!
    # try:
    #     while state.connected:
    #         # Print out the bot state.
    #         if state.bot_state != None:
    #             print(state.bot_state)
    #             melkMan.update(state.bot_state)

    #         time.sleep(1)

    #         nextMove = melkMan.computeNextMove()

    #         send.send_action(game_conn, action.BotCommand(state.bot_id, nextMove))

    # except KeyboardInterrupt:
    #     game_conn.stop()
    #     sys.exit(0)
