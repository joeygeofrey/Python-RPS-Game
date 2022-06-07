import random


moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        humanMove = ''
        while humanMove not in moves:
            humanMove = input("Please enter a move:"
                              " Rock, Paper, Scissor or Quit: ").lower()
            if humanMove == 'quit':
                exit()
        return humanMove


class ReflectPlayer(Player):
    def __init__(self):
        self.lastMove = random.choice(moves)

    def move(self):
        return self.lastMove

    def learn(self, my_move, their_move):
        self.lastMove = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.moveIndex = random.randint(0, 2)

    def move(self):
        self.moveIndex = (self.moveIndex + 1) % 3
        return moves[self.moveIndex]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1Score = 0
        self.p2Score = 0

    def play_round(self, retryCount=0):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")

        if(beats(move1, move2)):
            self.p1Score += 1
            print("Player 1 wins this round!\n")
            print("Current Score:")
            print(f"Player 1: {self.p1Score}  Player 2: {self.p2Score}\n")

        elif(beats(move2, move1)):
            self.p2Score += 1
            print("Player 2 wins this round!\n")
            print("Current Score:")
            print(f"Player 1: {self.p1Score}  Player 2: {self.p2Score}\n")

        else:
            print("It's a tie! Let's have another go!\n")
            if (retryCount < 3):
                self.play_round(retryCount+1)
            else:
                print("It's going to be a tie!")
            return

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        for round in range(4):
            print(f"\nRound {round+1}:")
            self.play_round()
        print("Game over!\n")
        print("Final Score:")
        print(f"P1 Score: {self.p1Score}  P2 Score: {self.p2Score}\n")
        if(self.p1Score > self.p2Score):
            print("Player 1 wins the game!")
        elif(self.p2Score > self.p1Score):
            print("Player 2 wins the game!\n")
        else:
            print("It's a tie!\n")


if __name__ == '__main__':
    print("\nRock, Paper, Scissors.. GO!\n")
    strategies = {
                  "1": Player(),
                  "2": RandomPlayer(),
                  "3": CyclePlayer(),
                  "4": ReflectPlayer()
    }

    user_input = input("Please select a player strategy [#] "
                       "to play against:\n"
                       "[1] Rock Player\n"
                       "[2] Random Player\n"
                       "[3] Cycle Player\n"
                       "[4] Reflect Player\n")

    while (user_input != "1" and user_input != "2" and
           user_input != "3" and user_input != "4"):
        user_input = input("Please select a player strategy [#] "
                           "to play against:\n"
                           "[1] Rock Player\n"
                           "[2] Random Player\n"
                           "[3] Cycle Player\n"
                           "[4] Reflect Player\n")

    print(f"Looks like you've selected {strategies[user_input]} \nGood luck!\n")

    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
