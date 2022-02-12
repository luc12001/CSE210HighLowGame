import random

class Card:
    """Generates a random card number within 1 and 13.

    The responsibility of Card is to keep track of the card displayed and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Generates a new random card.
        
        Args:
            self(card): An instance of card
        
        """
        self.value = 0
        
    def draw(self):
        self.value = random.randint(1,13)
        return self.value
        
        