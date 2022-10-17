# Lab 4
# Author: Ravish Kamath
# Email: ravish96@my.yorku.ca
# Section B
# Student ID: 213893664

from random import randint

def getCardValue():
    cardValue = randint(2, 14)
    return cardValue

def getCardStr(cardValue):
    strCardValue = ""
    if cardValue >= 2 and cardValue <= 9:
        return str(cardValue)
    elif cardValue == 10:
        strCardValue = "T"
    elif cardValue == 11:
        strCardValue = "J"
    elif cardValue == 12:
        strCardValue = "Q"
    elif cardValue == 13:
        strCardValue = "K"
    elif cardValue == 14:
        strCardValue = "A"
    return strCardValue

def getHLGuess():
    prompt = input("High or Low (H/L)?: ")
    while ((prompt.upper() != "H") and (prompt.upper() != "L")):
        prompt = input("High or Low (H/L)?: ")
    if (prompt.upper() == "H"):
        return "HIGH"
    elif (prompt.upper() == "L"):
        return "LOW"

def getBetAmount(maximum):
    prompt = int(input("Input bet amount: "))
    while prompt < 1 or prompt > maximum:
        prompt = int(input("Input bet amount: "))
    return prompt

def playerGuessCorrect(card1, card2, betType):
    if ((betType == "HIGH") and (card1 >= card2)) or ((betType == "LOW") and (card1 <= card2)):
        value = False
        return value
    else:
        value = True
        return value

def updatePoints(card1, card2, betType, bet, points):
    x = playerGuessCorrect(card1, card2, betType)
    if x == True:
        points = points + bet
    elif x == False:
        points = points - bet
    return points

def main():
    #global points
    points = 100
    rounds = 1
    print("---Welcome to High Low---")
    print("Start with 100 points. Each round a card will be drawn and shown")
    print("Select whether you think the 2nd card will be Higher or Lower than the 1st card.")
    print("Then enter the amount you want to bet")
    print("If you are right, you win the amount you bet, otherwise you lose")
    print("Try to make it to 500 points within 10 tries")
    while (rounds < 11) and points < 500 and points > 0:
        print("-------------------------------------")
        print(f"OVERALL POINTS: {points} ROUND {rounds}/10")
        x = getCardValue()
        x1 = getCardStr(x)
        y = getCardValue()
        y1 = getCardStr(y)
        print(f"First card is a [{x1}]")
        #global betType
        betType = getHLGuess()
        #global bet
        bet = getBetAmount(points)
        global card1
        card1 = x
        global card2
        card2 = y
        points = updatePoints(card1, card2, betType, bet, points)
        print(points)
        print(f"Second card is a [{y1}]")
        if ((betType == "HIGH") and (card1 >= card2)) or ((betType == "LOW") and (card1 <= card2)):
            print(f"Card1 [{x1}] Card2 [{y1}] - You Bet '{betType}' for {bet} - YOU LOST")
        else:
            print(f"Card1 [{x1}] Card2 [{y1}] - You Bet '{betType}' for {bet} - YOU WON")
        rounds = rounds + 1
    if (rounds < 11) and points >= 500:
        print("---------------WIN--------------------")
        print(f"YOU MADE IT TO *{points}* POINTS IN {rounds} ROUNDS!")
    elif (rounds < 11) and points <= 0:
        print("-----------LOSE-------------")
        print(f"YOU HAVE *{points}* POINTS AFTER {rounds} ROUNDS!")
    elif (rounds >= 11):
        print("-----------LOSE-------------")
        print(f"ONLY *{points} IN 10 ROUNDS")
    input("Press enter to quit.")


if __name__ == "__main__":
    main()