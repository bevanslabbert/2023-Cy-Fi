package Services;

import Enums.*;
import Models.*;
import Models.Dtos.*;

import java.util.*;

public class BotService {
    int i = 0;
    Boolean shouldQuit = false;
    Boolean receivedBotState = false;
    private BotStateDto botState;
    private UUID botId;

    public BotService() {
    }

    public Boolean getReceivedBotState() {
        return receivedBotState;
    }

    public void setReceivedBotState(Boolean receivedBotState) {
        this.receivedBotState = receivedBotState;
    }

    public Boolean getShouldQuit() {
        return shouldQuit;
    }

    public void setShouldQuit(Boolean shouldQuit) {
        this.shouldQuit = shouldQuit;
    }

    public BotStateDto getBotState() {
        return botState;
    }

    public void setBotState(BotStateDto botState) {
        this.botState = botState;
    }

    public void setBotId(UUID botId) {
        this.botId = botId;
    }

    public UUID getBotId() {
        return botId;
    }

    public BotCommand computeNextPlayerAction() {
        // TODO: Replace this with your bot's logic.
        int x = this.botState.getX();
        int y = this.botState.getY();
        if (botState.getHeroWindow()[x + 1][y] == Tile.LADDER.getValue()) {
            System.out.println("Ladder to your right");
            return new BotCommand(botId, InputCommand.RIGHT);
        } else if (botState.getHeroWindow()[x][y] == Tile.LADDER.getValue()) {
            System.out.println("On a ladder");
            return new BotCommand(botId, InputCommand.UP);
        } else if (botState.getHeroWindow()[x + 1][y] == Tile.AIR.getValue()) {
            System.out.println("Air to your right");
        } else {
            return new BotCommand(botId, InputCommand.RIGHT);
        }
        return new BotCommand(botId, null);
    }
}
