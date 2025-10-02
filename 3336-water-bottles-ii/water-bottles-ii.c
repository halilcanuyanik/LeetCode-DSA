int maxBottlesDrunk(int numBottles, int numExchange) {
    int fullBottles = numBottles;
    int emptyBottles = numBottles - fullBottles;
    int drinkCount = 0;
    while (fullBottles > 0) {
        int thisRound = 0;
        thisRound += fullBottles;
        drinkCount += thisRound;
        emptyBottles += fullBottles;
        fullBottles = 0;
        if (emptyBottles >= numExchange) {
            emptyBottles -= numExchange;
            fullBottles += 1;
            numExchange += 1;
        }
    }
    return drinkCount;
}