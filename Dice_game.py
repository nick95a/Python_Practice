import random

class Game:

    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.switch_demo()
    def switch_demo(self,*arg):
        switcher = {
            1: "Roll the die",
            2: "Take a shot",
            3: "Curse at how badly this game is made",
            4: "Make a guess for your roll",
            5: "End the game"
        }
        print(switcher)
        decision = int(input("Make your choice\n"))
        if decision == 1:
            self.make_roll()
        elif decision == 2:
            self.take_shot()
        elif decision == 3:
            self.curse()
        elif decision == 4:
            self.guess(self)
        else:
            self.end_game()

    def make_roll(self):
        number = random.randint(1, 7)
        print(number)
        self.switch_demo(self)

    def take_shot(self):
        print("Feels good\n")
        self.switch_demo(self)

    def curse(self):
        options = ["You are f...ing stupid", "You will never become a programmer, always a monkey coder", "Please let me out"]
        choice = random.randint(0,3)
        print(options[choice])
        self.switch_demo(self)

    def guess(self, guess):
        check = guess
        roll = random.randint(1,7)
        if check == roll:
            print("You guessed right\n")
            self.switch_demo(self)
        else:
            print("Bad luck, try again\n")
            self.switch_demo()

    def end_game(self):
        print("Sad to see you leave, see ya\n")
        return 0

def intro():
    print("Welcome to the dice game")
    print("Please introduce yourself and present your name and your favourite programming language")
    name = input("Enter your name\n")
    language = input("Fav language\n")
    return name, language


name, language = intro()
game = Game(name, language)
