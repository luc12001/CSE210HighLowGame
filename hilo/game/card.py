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
