
from game.card import Card

import random


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        self.score = 300
        self.card_value = 0
        self.nextcard = 0

        self.card_value = random.randint(1, 13)
        print(f"The card is {self.card_value}")

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        self.draw_card = input("Higher or lower? [h/l] ")
        self.is_playing = (self.draw_card == "h" or self.draw_card == "l")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        nextcard = Card()
        self.nextcard = nextcard.draw()
        print("Next card is: ", self.nextcard)
        compare = 1 if self.card_value > self.nextcard else 2 if self.card_value < self.nextcard else 0
        # print(compare)
        newscore = 100 if (compare == 1 and self.draw_card == "l") or (
            compare == 2 and self.draw_card == "h") else -75
        # comment this line in order to have same display than example
        print("This shoot score is: ", newscore)
        self.score += newscore

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your accumulated score is: {self.score}")
        if self.score <= 0:
            print("Game over, your score is below cero!")
            self.is_playing = False
        else:
            again = input("Play again [y/n]: ")
            self.is_playing = (again == "y")
            if again == "y":
                print(f"\nThe card is: ", self.nextcard)
                self.card_value = self.nextcard
            else:
                print("Thanks for playing!")
