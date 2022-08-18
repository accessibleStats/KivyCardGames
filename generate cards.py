"""
Generating Deck of Cards
"""
import random


def deck():
    # create lists to be used for suits
    hearts = list(range(1,14))
    diamonds = list(range(1,14))
    clubs = list(range(1,14))
    spades = list(range(1,14))
    # replace numbers with face cards and ace card
    hearts = ['Ace' if x == 1 else x for x in hearts]
    hearts = ['King' if x == 13 else x for x in hearts]
    hearts = ['Queen' if x == 12 else x for x in hearts]
    hearts = ['Jack' if x == 11 else x for x in hearts]
    diamonds = ['Ace' if x == 1 else x for x in diamonds]
    diamonds = ['King' if x == 13 else x for x in diamonds]
    diamonds = ['Queen' if x == 12 else x for x in diamonds]
    diamonds = ['Jack' if x == 11 else x for x in diamonds]
    clubs = ['Ace' if x == 1 else x for x in clubs]
    clubs = ['King' if x == 13 else x for x in clubs]
    clubs = ['Queen' if x == 12 else x for x in clubs]
    clubs = ['Jack' if x == 11 else x for x in clubs]
    spades = ['Ace' if x == 1 else x for x in spades]
    spades = ['King' if x == 13 else x for x in spades]
    spades = ['Queen' if x == 12 else x for x in spades]
    spades = ['Jack' if x == 11 else x for x in spades]
    # add "of suit" to cards - define suits
    suitspade = 'of Spades'
    suitspade = 'of Clubs'
    suitspade = 'of Diamonds'
    suitspade = 'of Hearts'
    # change remaining integers to strings
    spades = map(str, spades)
    clubs = map(str, clubs)
    diamonds = map(str, diamonds)
    hearts = map(str, hearts)
    # complete card names
    spades = [card + " " + suitspade for card in spades]
    clubs = [card + " " + suitspade for card in clubs]
    diamonds = [card + " " + suitspade for card in diamonds]
    hearts = [card + " " + suitspade for card in hearts]
    # combine into deck
    deck = spades + clubs + diamonds + hearts

    print(deck)
    return deck


def shuffle(deck):
    playerone = []
    playertwo = []

    def shuffle():
        deck = random.shuffle()




deck()
