"""
Author: Brandon Luce, Megan Westover, Richard Asare, Camilo Camargo
Title: Hi-Lo Game
"""

import random

class Card:
    """
    Class that initiates a card.
    """
    def __init__(self):
        '''
        Initializes a card and sets the value to 0.
        '''
        self.card = 0
                

    def draw(self):
        '''
        Draws a random card/number.
        '''
        self.card = random.randint(1,13)
        return self.card

class Director:
    ''' 
    Initializes methods to play the game. Includes starting the game, inputs and updates.
    '''
    def __init__(self):
        '''
        This starts initializing thee points and starts the game.  
        '''
        self.points = 300

        self.is_playing = True

    def start_game(self):
        '''
        Ask the user to choose higher or lower(h/l) and use the 
        users input to decide the next move.
        '''
        self.card1 = Card()
        self.card2 = Card()
        self.card1.draw()
        self.card2.draw()
        print(f"The current card is: {self.card1.card}")
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            pass

    def get_inputs(self):
        '''
        This asks the user if they want to guess higher or lower for the next card.
        If another input is put in it asks again.
        '''
        self.guess = input("Guess Higher or Lower? [h/l] ")
        while len(self.guess) > 0:
            if self.guess.lower() in ["h", "l"]:
                return
            else: 
                self.guess.lower() != ["h", "l"]
                print("Not a valid entry, try again")
                self.guess = input("Guess Higher or Lower? [h/l] ")

    def again(self):
        '''
        Checks to see if user wants to play again.
        '''
        self.playAgain = input("Would you like to play again? [y/n] ")
        while len(self.playAgain) > 0:
            if self.playAgain.lower() in ["y","n"]:
                return self.playAgain
            else:
                self.playAgain.lower() != ["y", "n"]
                print("Not a valid entry, try again")
                self.playAgain = input("Would you like to play again? [y/n] ")
                
    def do_updates(self):
        '''
        Compares the cards and gives point compared to correct or incorrect answers.
        Relates the score and whether or not you are correct.
        Then it prints the total points. 

        '''
        self.card1.card = self.card2.card
        card1 = self.card1.card
        card2 = self.card2.draw()
        guess = self.guess
        print(f"The next card picked is {card2}")

        if guess.lower() == "h" and card2 > card1:
            print("Correct!")
            self.points += 100
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if guess.lower() == "h" and card2 < card1:
            print("Wrong!")
            self.points -= 75
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if guess.lower() == "l" and card2 < card1:
            print("Correct!")
            self.points += 100
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if guess.lower() == "l" and card2 > card1:
            print("Wrong!")
            self.points -= 75
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if self.points <= 0:
            print("Game Over!")
            print()
            quit()



def main():
    '''
    Calls the card and director function.  Then draws the cards and makes sure the game is started. 
    '''
    card = Card()
    person = Director()
    card.draw()
    person.start_game()

if __name__ == "__main__":
    main()
