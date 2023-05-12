import os
import sys
import time
from dataclasses import dataclass
from pprint import pprint
from typing import Any, Dict, List, Optional

from signalrcore.helpers import logging as LogLevel
from signalrcore.hub_connection_builder import HubConnectionBuilder

# Current Connection State
@dataclass
class State:
    connected: bool = False
    bot_id: Optional[str] = None
    bot_name: Optional[str] = None
    bot_state: Optional[Dict[str, Any]] = None

# Initialise state
state = State()

# When the connection starts
def on_open():
    state.connected = True
    print("Connection started")

# When the connection is closed
def on_close(reason):
    state.connected = False
    print("Connection closed with reason: ", reason)

# When the Disconnect command is sent from the runner.
def on_disconnect(reason):
    state.connected = False
    print("Server sent disconnect command with reason: ", reason)

# When the Registered command is sent from the runner.
def on_registered(params: List[str]):
    state.bot_id = params[0]
    print("Bot registered with ID: ", state.bot_id)

# When the ReceiveBotState commmand is sent from the runner.
def on_receive_bot_state(params: List[Any]):
    state.bot_state = params[0]

# Register websocket handlers
def register_handlers(connection):
    connection.on_open(on_open)
    connection.on_close(on_close)
    connection.on("Disconnect", on_disconnect)
    connection.on("Registered", on_registered)
    connection.on("ReceiveBotState", on_receive_bot_state)

# Build SignalR connection to Runner Hub
def build_connection(url):
    connection = (
        HubConnectionBuilder()
        .with_url(url)
        .configure_logging(LogLevel.DEBUG)
        .with_automatic_reconnect(
            {
                "keep_alive_interval": 10,
                "reconnect_interval": 5,
            }
        )
        .build()
    )
    
    return connection

def configure_url():
    runner_ip = os.getenv("RUNNER_IPV4") or "localhost"
    return runner_ip if runner_ip.startswith("http://") else f"http://{runner_ip}"

def start(PORT=5000):
    runner_ip = configure_url()

    # Create SignalR connection
    connection = build_connection(f"{runner_ip}:{PORT}/runnerhub")

    # Register event handlers
    register_handlers(connection)

    # Initiate connection with game server
    print("Starting connection...")
    connection.start()
    time.sleep(1)

    # Register the bot
    state.bot_name = os.getenv("BOT_NICKNAME") or "PyBot"
    print("Registering bot")
    connection.send("Register", [state.bot_name])

    return (connection, state)
    
