import random

class Player:
    # Pre defined variables for the locations of the snakes and ladders and where they lead to
    snakes = {16:6, 47:26, 49:11, 56:53, 62:19, 64:60, 87:24, 93:73, 95:75, 98:78}
    ladders = {1:38, 4:14, 9:31, 21:42, 28:84, 36:44, 51:67, 71:91, 80:100}

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        dice = input("Type 6 to use a dice with values 1 to 6 or type 10 to use a dice with values -4 to 10: ")
        while(dice != "6" and dice != "10"): #Validating user input
            dice = input("Please enter 6 or 10: ")
        if(dice == "6"):
            roll = random.randint(1,6)
        else:
            roll = random.randint(-4,10)

        print("You rolled a", roll)
        old = self.position
        self.position += roll
        print("You moved from", old, "to", self.position)

        if(self.position in self.snakes): #Check to see if player landed on a snake
            old = self.position
            self.position = self.snakes[old]
            print("Oh no! You hit a snake! You moved from", old, "down to", self.position)

        elif(self.position in self.ladders): # Check to see if a player landed on a ladder
            old = self.position
            self.position = self.ladders[old]
            print("Yay! You landed on a ladder! You moved from", old, "up to", self.position)

        elif(self.position > 100): # Check to see if a player went over 100
            self.position = old
            print("Oh no! You went over 100! You moved back to" , old)

        if(self.position == 100): # Check to see if a player reached 100 and won the game
            print("Congrats! You made it to 100! You win!")

class Game:

    def __init__(self,player1, player2):
        self.p1 = player1 #Player class
        self.p2 = player2 #Player class

    def play(self):
        print("Let the games begin!")
        while(self.p1.position != 100 and self.p2.position != 100):
            print(self.p1.name, "it is your turn")
            self.p1.move()

            print(self.p2.name, "it is your turn")
            self.p2.move()

        if(self.p1.position == 100):
            print(self.p1.name,"wins!")
        elif(self.p2.position == 100):
            print(self.p2.name,"wins!")
        

if __name__ == "__main__":
    print("Welcome to Snakes and Ladders!")
    name1 = input("Player one please enter your name: ")
    p1 = Player(name1)

    name2 = input("Player two please enter your name: ")
    p2 = Player(name2)

    g = Game(p1,p2)
    g.play()
    print("Game over")