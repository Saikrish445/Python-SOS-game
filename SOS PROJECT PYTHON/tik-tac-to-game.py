import random


def display_board(board):
    print("   |   |")
    print(" " + board[9] + " | " + board[8] + " | " + board[7])
    print("   |   |")
    print("-----------")
    print(" " + board[6] + " | " + board[5] + " | " + board[4])
    print("-----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")


def player_input():
    marker = ""
    while marker not in ["X", "O"]:
        marker = input("Player 1: Which one do you want (X or O)? ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
        (board[9] == mark and board[8] == mark and board[7] == mark)
        or (board[6] == mark and board[5] == mark and board[4] == mark)
        or (board[1] == mark and board[2] == mark and board[3] == mark)
        or (board[9] == mark and board[6] == mark and board[1] == mark)
        or (board[8] == mark and board[5] == mark and board[2] == mark)
        or (board[7] == mark and board[4] == mark and board[3] == mark)
        or (board[1] == mark and board[5] == mark and board[9] == mark)
        or (board[7] == mark and board[5] == mark and board[3] == mark)
    )


def choose_first():
    return "Player 2" if random.randint(0, 1) == 0 else "Player 1"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    return all(space_check(board, i) == False for i in range(1, 10))


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your next position: (1-9) "))
    return position


def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")


print("Welcome to Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = input("Are you ready to play? Enter Yes or No. ").lower()
    game_on = play_game[0] == "y"

    while game_on:
        if turn == "Player 1":
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations! You have won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
