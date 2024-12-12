def initialize_board():
    """
    Inicializē tukšu spēles laukumu.
    """
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    """
    Izdrukā pašreizējo spēles laukuma stāvokli.
    """
    print("\n  0   1   2")
    for idx, row in enumerate(board):
        print(f"{idx} " + " | ".join(row))
        if idx < 2:
            print("  ---+---+---")
    print()


def is_valid_move(board, row, col):
    """
    Pārbauda, vai gājiens ir pareizs.
    """
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "


def check_winner(board, player):
    """
    Pārbauda, vai pašreizējais spēlētājs ir uzvarējis.
    """
    # Pārbauda rindās
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Pārbauda kolonnās
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Pārbauda diagonālēs
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    """
    Pārbauda, vai spēle ir neizšķirts.
    """
    return all(cell != " " for row in board for cell in row)


def play_game():
    """
    Galvenā spēles funkcija, kas realizē spēles loģiku.
    """
    print("Sveicināti spēlē 'Krusta un nulles'!")
    print("Divu spēlētāju spēle: spēlētājs 1 ir 'X', spēlētājs 2 ir 'O'.\n")

    board = initialize_board()
    current_player = "X"  # Spēlētājs 1 sāk
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Spēlētāja {current_player} gājiens.")

        try:
        # Ievadiet rindas un kolonnas numurus
            row = int(input("Ievadiet rindas numuru (0, 1 vai 2): "))
            col = int(input("Ievadiet kolonnas numuru (0, 1 vai 2): "))

            # Pārbaudiet, vai gājiens ir derīgs
            if not is_valid_move(board, row, col):
                print("Nederīgs gājiens! Lūdzu, mēģiniet vēlreiz.")
                continue

            # Veiciet gājienu
            board[row][col] = current_player

            # Pārbaudiet, vai pašreizējais spēlētājs ir uzvarējis
            if check_winner(board, current_player):
                print_board(board)
                print(f"Spēlētājs {current_player} uzvar! Apsveicam!")
                game_over = True
            elif is_draw(board):  # Pārbaudiet, vai spēle ir neizšķirts
                print_board(board)
                print("Neizšķirts! Spēle beigusies.")
                game_over = True
            else:
                # Mainiet spēlētāju
                current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Lūdzu, ievadiet derīgus skaitļus!")

if __name__ == "__main__":
    play_game()

