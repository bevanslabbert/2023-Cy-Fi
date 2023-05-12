package Enums;

import java.util.Arrays;
import java.util.Optional;

public enum Tile {
    AIR(0),
    SOLID(1),
    COLLECTIBLE(2),
    HAZARD(3),
    PLATFORM(4),
    LADDER(5),
    OPPONENT(6);

    private final int value;

    private Tile(int value) {
        this.value = value;
    }

    public static Optional<Tile> valueOf(int value) {
        return Arrays.stream(Tile.values()).filter(tile -> tile.value == value).findFirst();
    }

    public int getValue() {
        return this.value;
    }

    @Override
    public String toString() {
        return this.name() + "(" + value + ")";
    }
}
