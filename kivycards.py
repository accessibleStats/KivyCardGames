'''


                    - - - - Card Games on Kivy - - - -
                   Kivy app with multiple screens + nav
           * * * * * * * * * * Card Games * * * * * * * * * 


'''

from kivy.app import App
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random



# define variables:
playeronecard = StringProperty()
playertwocard = StringProperty()
playeronescorestring = StringProperty()
playertwoscorestring = StringProperty()
winner = StringProperty()
playeronescore: int = 0
playertwoscore:int = 0  

class OpeningScreen(Screen):
    pass

class BlackJackScreen(Screen): 
    pass    

class WarScreen(Screen):
# score increment 
    def increasescore(self,x:int):
        x += 1
        return x
# generate deck with jokers
    def newdeck(self):
        global deck
        global deckdictionary
        deck = []
        deckdictionary = dict()
        # create lists to be used for suits
        hearts: list = list(range(2,15))
        diamonds = list(range(2,15))
        clubs = list(range(2,15))
        spades = list(range(2,15))
        # replace numbers with face and ace card names
        hearts = ['ace' if x == 14 else x for x in hearts]
        hearts = ['king' if x == 13 else x for x in hearts]
        hearts = ['queen' if x == 12 else x for x in hearts]
        hearts = ['jack' if x == 11 else x for x in hearts]
        diamonds = ['ace' if x == 14 else x for x in diamonds]
        diamonds = ['king' if x == 13 else x for x in diamonds]
        diamonds = ['queen' if x == 12 else x for x in diamonds]
        diamonds = ['jack' if x == 11 else x for x in diamonds]
        clubs = ['ace' if x == 14 else x for x in clubs]
        clubs = ['king' if x == 13 else x for x in clubs]
        clubs = ['queen' if x == 12 else x for x in clubs]
        clubs = ['jack' if x == 11 else x for x in clubs]
        spades = ['ace' if x == 14 else x for x in spades]
        spades = ['king' if x == 13 else x for x in spades]
        spades = ['queen' if x == 12 else x for x in spades]
        spades = ['jack' if x == 11 else x for x in spades]
        # add "of suit.png" to cards - define suits
        ssuitspade = 'of spades.png'
        csuitspade = 'of clubs.png'
        dsuitspade = 'of diamonds.png'
        hsuitspade = 'of hearts.png'
        # change remaining integers to strings
        spades = map(str, spades)
        clubs = map(str, clubs)
        diamonds = map(str, diamonds)
        hearts = map(str, hearts)
        # complete card names
        spades = [card + " " + ssuitspade for card in spades]
        clubs = [card + " " + csuitspade for card in clubs]
        diamonds = [card + " " + dsuitspade for card in diamonds]
        hearts = [card + " " + hsuitspade for card in hearts]
        # combine into deck
        deck = spades + clubs + diamonds + hearts
        # add jokers
        deck.append('low joker.png')
        deck.append('high joker.png')
        # order deck and assign card values
        # transform deck into dictionary data type to assign appropriate values to cards for keeping score
        deckdictionary = {'2 of clubs.png':2, '2 of hearts.png':2, '2 of diamonds.png':2, '2 of spades.png':2, '3 of clubs.png':3, '3 of diamonds.png':3, '3 of hearts.png':3, '3 of spades.png':3, '4 of clubs.png':4, '4 of diamonds.png':4, '4 of hearts.png':4, '4 of spades.png':4, '5 of clubs.png':5, '5 of diamonds.png':5, '5 of hearts.png':5, '5 of spades.png':5, '6 of clubs.png':6, '6 of diamonds.png':6, '6 of hearts.png':6, '6 of spades.png':6, '7 of clubs.png':7, '7 of diamonds.png':7, '7 of hearts.png':7, '7 of spades.png':7, '8 of clubs.png':8, '8 of diamonds.png':8, '8 of hearts.png':8, '8 of spades.png':8, '9 of clubs.png':9, '9 of diamonds.png':9, '9 of hearts.png':9, '9 of spades.png':9, '10 of clubs.png':10, '10 of diamonds.png':10, '10 of hearts.png':10, '10 of spades.png':10, 'jack of clubs.png':11, 'jack of diamonds.png':11, 'jack of hearts.png':11, 'jack of spades.png':11, 'queen of clubs.png':12, 'queen of diamonds.png':12, 'queen of hearts.png':12, 'queen of spades.png':12, 'king of clubs.png':13, 'king of diamonds.png':13, 'king of hearts.png':13, 'king of spades.png':13, 'ace of clubs.png':14, 'ace of diamonds.png':14, 'ace of hearts.png':14, 'ace of spades.png':14, 'low joker.png':15, 'high joker.png':16}
        # return deck to be used for game play
        return deck, deckdictionary

# method to deal cards and update score with each button push
    def warplay(self):
        # use of global to re-assign player one and two score
        global playeronescore
        global playertwoscore    
        #player one's card
        playeronecard = random.choice(deck)
        # find card's index to use in card removal from deck
        playeronecardindex = deck.index(playeronecard)
        del deck[playeronecardindex]
        # player two's card
        playertwocard = random.choice(deck)
        # find card's index to use in card removal from deck
        playertwocardindex = deck.index(playertwocard)
        del deck[playertwocardindex]
        # update the image file source to be displayed
        self.ids.player1card.source = f'{playeronecard}'
        self.ids.player2card.source = f'{playertwocard}'
        # update score - explicit variable definition
        playeronecardvalue: int = 1
        playertwocardvalue: int = 1
        playeronecardvalue = deckdictionary[playeronecard]
        playertwocardvalue = deckdictionary[playertwocard]
        # if statemwnt to update score conditional on card values
        if playeronecardvalue > playertwocardvalue:
            playeronescore = self.increasescore(playeronescore)
            playeronescorestring = f'{playeronescore}'
            playertwoscorestring = f'{playertwoscore}'
            self.ids.player1score.text = playeronescorestring
            self.ids.player2score.text = playertwoscorestring
                    # if statment for final screen declaring winner/loser
            if len(deck) < 2:
                WarPopup.declarewinner(self,playeronescore,playertwoscore)
                WarPopup.ids.gamewinner.source = f'{winner}'
                popup = WarPopup()
                popup.open()
            else:
                pass
            return playeronescore, playertwoscore, deck, playeronecard, playertwocard, playeronescorestring, playertwoscorestring

        elif playeronecardvalue == playertwocardvalue:
            # if statment for final screen declaring winner/loser
            if len(deck) < 2:
                WarPopup.declarewinner(self,playeronescore,playertwoscore)
                WarPopup.ids.gamewinner.source = f'{winner}'
                popup = WarPopup()
                popup.open()
            else:
                pass
            return playeronescore, playertwoscore, deck, playeronecard, playertwocard
        else: 
            playertwoscore = self.increasescore(playertwoscore)
            playeronescorestring = f'{playeronescore}'
            playertwoscorestring = f'{playertwoscore}'
            self.ids.player2score.text = playertwoscorestring
            self.ids.player1score.text = playeronescorestring
            # if statment for final screen declaring winner/loser
            if len(deck) < 2:
                WarPopup.declarewinner(self,playeronescore,playertwoscore)
                WarPopup.ids.gamewinner.source = f'{winner}'
                popup = WarPopup()
                popup.open()
            else:
                pass
            return playertwoscore, playeronescore, deck, playeronecard, playertwocard, playeronescorestring, playertwoscorestring

class WarPopup(Popup):
    global winner
    winner = StringProperty()
    def declarewinner(self, playeronescore, playertwoscore):
        if playeronescore>playertwoscore: 
            print(f'player one scored - {playeronescore}')
            print(f'player two scored - {playertwoscore}')
            winner = 'playerone.png'
            print(winner)
            return winner
        elif playeronescore<playertwoscore:
            print(f'player one scored - {playeronescore}')
            print(f'player two scored - {playertwoscore}')
            winner = 'playertwo.png'
            print(winner)   
            return winner
        else:
            print(f'player one scored - {playeronescore}')
            print(f'player two scored - {playertwoscore}')
            winner = 'tied.png'
            print(winner)
            return winner


class ScreenManagement(ScreenManager):
    pass

# points to associated kv file - another option is to name your "App" with the same name as your kv file.
kvfile = Builder.load_file('kivycardsKV.kv')

# creating the App class
class CardGamesApp(App):       
    # returning the instance of root class
    def build(self):
        return kvfile

if __name__ == '__main__':
    CardGamesApp().run()