from game.card import Card

import random








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