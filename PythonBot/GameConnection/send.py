from Game import action

def send_action(connection, payload: action.BotCommand, msg_type: str = 'SendPlayerCommand'):
    payload = {
        "Action": payload.action,
        "BotId": payload.botId
    }
    connection.send(msg_type, [payload])

