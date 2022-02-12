from game.card import Card

import random


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
        Compares the cards and gives points compared to correct or incorrect answers.
        Relates the score and whether or not you are correct.
        Then it prints the total points. 

        '''
        self.card1.card = self.card2.card
        card1 = self.card1.card
        card2 = self.card2.draw()
        guess = self.guess
        print(f"The next card picked is {card2}")

        if guess.lower() == "h" and card2 > card1:
            print("Correct!, you won 100 more points.")
            self.points += 100
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                print("Thank you for playing")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if guess.lower() == "h" and card2 < card1:
            print("Wrong guess!, you lost 75 points")
            self.points -= 75
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                print("Thank you for playing")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if guess.lower() == "l" and card2 < card1:
            print("Correct!, you won 100 more points")
            self.points += 100
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                print("Thank you for playing")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if guess.lower() == "l" and card2 > card1:
            print("Wrong guess!, you lost 75 points")
            self.points -= 75
            print("Your score so far is", self.points)
            print()
            if self.points <= 0:
                print("Game Over!")
                print("Thank you for playing.")
                quit()
            if self.again() == "y":
                pass
            else:
                quit()

        if self.points <= 0:
            print("You ran out of points! Game Over!")
            print("Thank you for playing")
            quit()



def main():
    '''
    Calls the card and director function. Then draws the cards and makes sure the game is started. 
    '''
    card = Card()
    person = Director()
    card.draw()
    person.start_game()

if __name__ == "__main__":
    main()