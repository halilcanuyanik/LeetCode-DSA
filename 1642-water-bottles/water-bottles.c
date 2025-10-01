int numWaterBottles(int numBottles, int numExchange) {
    int drinkCount = 0;
    int fullBottle = numBottles;
    int emptyBottle = numBottles - fullBottle;
    while (fullBottle > 0) {
        int thisRound = 0;
        drinkCount += fullBottle;
        thisRound += fullBottle;
        emptyBottle += thisRound;
        fullBottle = emptyBottle / numExchange;
        emptyBottle %= numExchange;
    }
    return drinkCount;
}