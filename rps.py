import random
import sys


class RPS:
    def __init__(self) -> None:
        print("Welcome to Rock, Paper, Scissors!")

        self.moves: dict = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
        self.valid: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move = input("Enter your move: ").lower()

        if user_move == "exit":
            print("Thanks for playing!")
            sys.exit()

        if user_move not in self.valid:
            print("Invalid move. Please try again.")
            return self.play_game()

        ai_move = random.choice(self.valid)

        self.display_move(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_move(self, user_move, ai_move):
        print("--------------------\n")
        print(f"Your move: {self.moves[user_move]} \n")
        print(f"AI move: {self.moves[ai_move]} \n")
        print("--------------------\n")

    def check_move(self, user_move, ai_move):
        if user_move == ai_move:
            print("It's a tie!")
        elif user_move == "rock" and ai_move == "scissors":
            print("You win!")
        elif user_move == "paper" and ai_move == "rock":
            print("You win!")
        elif user_move == "scissors" and ai_move == "paper":
            print("You win!")
        else:
            print("You lose!")


if __name__ == "__main__":
    rps = RPS()
    while True:
        rps.play_game()
