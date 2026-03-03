def board():
    print("1|2|3")
    print("------")
    print("4|5|6")
    print("------")
    print("7|8|9")
    print()
    print("------------")


def print_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("------")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("------")
    print(f"{board[6]}|{board[7]}|{board[8]}")


def win_checker(present_board, symbol):
    if present_board[0] == symbol and present_board[1] == symbol and present_board[2] == symbol:
        return True
    elif present_board[3] == symbol and present_board[4] == symbol and present_board[5] == symbol:
        return True
    elif present_board[6] == symbol and present_board[7] == symbol and present_board[8] == symbol:
        return True
    elif present_board[0] == symbol and present_board[3] == symbol and present_board[6] == symbol:
        return True
    elif present_board[1] == symbol and present_board[4] == symbol and present_board[7] == symbol:
        return True
    elif present_board[2] == symbol and present_board[5] == symbol and present_board[8] == symbol:
        return True
    elif present_board[0] == symbol and present_board[4] == symbol and present_board[8] == symbol:
        return True
    elif present_board[2] == symbol and present_board[4] == symbol and present_board[6] == symbol:
        return True
    else:
        return False


myboard = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
isFilled = []

player_one = input("Enter the player 1 name: ")
player_two = input("Enter the player 2 name: ")
print(f"{player_one} symbol is O")
print(f"{player_two} symbol is X")

present = "O"

for i in range(9):
    board()
    print()
    print_board(myboard)
    print()

    if present == "O":
        print(f"{player_one} turn")
    else:
        print(f"{player_two} turn")
    print()

    index = int(input("Enter the index: "))
    if index < 1 or index > 9:
        print("Invalid index")
        continue

    if index in isFilled:
        print("Index already filled")
        continue
    isFilled.append(index)

    myboard[index - 1] = present
    if win_checker(myboard, present):
        print_board(myboard)
        print()
        if present == "O":
            print(f"{player_one} won")
        elif present == "X":
            print(f"{player_two} won")
        break

    if present == "O":
        present = "X"
    else:
        present = "O"

if not win_checker(myboard, present):
    print_board(myboard)
    print()
    print("Match Draw")