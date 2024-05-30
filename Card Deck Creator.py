# Elizabeth Connolly
# 12 November 2023
# This program displays a deck of cards and the hand associated with it

import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.__index = 0
        self.__cardDeck = []
        
        ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        for suit in suits:
            for rank in ranks:
                if rank == "Ace":
                    value = 1
                elif rank == "Jack":
                    value = 11
                elif rank == "Queen":
                    value = 12
                elif rank == "King":
                    value = 13
                else:
                    value = rank
                card = Card(suit, rank, value)
                self.__cardDeck.append(card)

    #shuffles the deck
    def shuffle(self):
        random.shuffle(self.__cardDeck)

    #removes one card from the deck and returns the card
    def dealCard(self):
        newCard = self.__cardDeck.pop()
        if newCard not in self.__cardDeck:
            return newCard
        else:
            return None

    #counts the length of the deck
    def countDeck(self):
        return len(self.__cardDeck)
    
    #allows for use in a loop
    def __iter__(self):
        self.__index = -1
        return self

    #allows for use in a loop
    def __next__(self):
        if self.__index >= len(self.__cardDeck):
            self.__index = 0
            raise StopIteration()
        item = self.__cardDeck[self.__index]
        self.__index += 1
        return item

        

class Hand:
    def __init__(self):
        self.__index = 0
        self.__cards = []

    #adds a card to the hand
    def addCard(self, card):
        self.__cards.append(card)

    #removes the card at the index value of the cards attribute and returns the card object
    def playCard(index):
        return self.__cards.pop(index) if index < len(self.__cards) else None

    #counts the number of cards in the hand
    def countHand(self):
        return len(self.__cards)

    #counts the total value of the cards in the hand
    def totalPoints(self):
        sum = 0
        for card in self.__cards:
            sum += int(card.value)
        return sum
    
    #allows for use in a loop
    def __iter__(self):
        return self

    #allows for use in a loop
    def __next__(self):
        if self.__index >= len(self.__cards):
            self.__index = 0
            raise StopIteration()
        item = self.__cards[self.__index]
        self.__index += 1
        return item


def main():
    print("Card Deck and Hand Creator\n")
    
    #print out deck
    print("DECK")
    deck = Deck()
    for card in deck:
        print(card)
    print()

    #shuffles the deck and prints the count
    deck.shuffle()
    print("Shuffled Deck Count: ", deck.countDeck())
    print()

    #print out deal (5 cards)
    print("HAND")
    hand = Hand()
    for c in range(5):
        card = deck.dealCard()
        hand.addCard(card)

    for card in hand:
        print(card)
    print()
    
    #print hand points
    print("Hand Points:", hand.totalPoints())
    #print hand count
    print("Hand Count:", hand.countHand())
    #print deck count
    print("Deck Count:", deck.countDeck())

    print()
    print("Process finished with exit code 0")

if __name__ == "__main__":
    main()

