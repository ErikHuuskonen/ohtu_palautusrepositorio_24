from tennis_game import TennisGame

def print_score(game):
    print(game.get_score())

def main():
    game = TennisGame("player1", "player2")

    print_score(game)

    game.won_point("player1")
    print_score(game)

    game.won_point("player1")
    print_score(game)

    game.won_point("player2")
    print_score(game)

    game.won_point("player1")
    print_score(game)

    game.won_point("player1")
    print_score(game)

if __name__ == "__main__":
    main()
