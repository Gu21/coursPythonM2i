from copy import deepcopy
from random import choice, randrange
import pickle

BOARD_SIZE = 10
HUMAN = True
IA = False
SHIP = 'O'
WATER = '-'
FOG = '*'
OLD_SHOT = 'X'
SMALL_SHIP_SIZE = 2
MEDIUM_SHIP_SIZE = 3
LARGE_SHIP_SIZE = 4
MISSED = 'Missed'
HIT = 'Ship hit'
SUNK = 'Ship sunk'
GAME_OVER = 'Fleet sunk'


def menu():
    while True:
        print("Battleship\n"
              "\n"
              "1) Player vs Player\n"
              "2) Player vs IA\n"
              "3) IA vs IA\n"
              "4) Load game\n"
              "5) Exit\n")
        while True:
            option = input('Select an option : ')
            match option:
                case '1':
                    game([HUMAN, HUMAN])
                    break
                case '2':
                    game([HUMAN, IA])
                    break
                case '3':
                    game([IA, IA])
                    break
                case '4':
                    boards, fleets, player, is_human, old_moves = load_game('save.pkl')
                    game(is_human, boards, fleets, player, old_moves)
                case '5':
                    exit(0)
                case other:
                    print('Incorrect input: Enter a number between 1 and 4')


def game(is_human, boards = [], fleets = [], player = 0, old_moves = []):
    opponent = 1 - player
    if not boards:
        old_moves = [[], []]
        boards = [spawn_board(BOARD_SIZE), spawn_board(BOARD_SIZE)]
        fleets = [{}, {}]
        spawn_fleet(boards[0], fleets[0])
        spawn_fleet(boards[1], fleets[1])
    # print_board_with_fleet(boards[0])
    # print_board_with_fleet(boards[1])
    while True:
        print_board(boards[opponent])
        # print_board_with_fleet(boards[opponent])
        # print(fleets[opponent])
        move = input_move(boards, fleets, player, is_human, old_moves)
        if move_is_valid(boards[opponent], move):
            outcome = carry_out_move(boards[opponent], fleets[opponent], move)
            print(outcome)
            if outcome == GAME_OVER:
                print(f'Player {player} wins the game')
                break
        player, opponent = opponent, player


def spawn_board(n):
    board = [[WATER for _ in range(n)] for _ in range(n)]
    return board


def spawn_fleet(board, fleet):
    spawn_ship(board, fleet, LARGE_SHIP_SIZE)
    spawn_ship(board, fleet, MEDIUM_SHIP_SIZE)
    spawn_ship(board, fleet, MEDIUM_SHIP_SIZE)
    spawn_ship(board, fleet, SMALL_SHIP_SIZE)


def spawn_ship(board, fleet, ship_size):
    n = len(board)
    while True:
        i, j = randrange(n), randrange(n)
        direction = choice(['left', 'up', 'right', 'down'])
        if not ship_is_legit(board, (i, j), ship_size, direction):
            continue
        set_ship(board, fleet, (i, j), ship_size, direction)
        return


def ship_is_legit(board, move, ship_size, direction):
    (i, j) = move
    n = len(board)
    for _ in range(ship_size):
        if i < 0 or j < 0 or i >= n or j >= n or board[i][j] != WATER:
            return False
        match direction:
            case 'left':
                i -= 1
            case 'up':
                j += 1
            case 'right':
                i += 1
            case 'down':
                j -= 1
    return True


def set_ship(board, fleet, move, ship_size, direction):
    (i, j) = move
    ship = []
    for _ in range(ship_size):
        board[i][j] = SHIP
        ship.append((i, j))
        match direction:
            case 'left':
                i -= 1
            case 'up':
                j += 1
            case 'right':
                i += 1
            case 'down':
                j -= 1
    for square in ship:
        copy = deepcopy(ship)
        copy.remove(square)
        fleet[square] = copy


def input_move(boards, fleets, player, is_human, old_moves):
    if is_human[player]:
        print("(Enter 'save' to save the game and exit)")
        input1 = input(f'Player {player} : Enter the first coordinate : ')
        if input1 == 'save':
            save_game(boards, fleets, player, is_human, old_moves)
            exit(0)
        i = int(input1)
        input2 = input(f'Player {player} : Enter the second coordinate : ')
        if input2 == 'save':
            save_game(boards, fleets, player, is_human, old_moves)
            exit(0)
        j = int(input2)
        return i, j
    else:
        while True:
            move = (randrange(10), randrange(10))
            if move in old_moves[player]:
                continue
            old_moves[player].append(move)
            print(f'Player {player} plays {move}')
            return move


def move_is_valid(board, move):
    (i, j) = move
    n = len(board)
    return i >= 0 and i < n and j >= 0 and j < n


def carry_out_move(board, fleet, move):
    (i, j) = move
    outcome = MISSED
    if board[i][j] == SHIP:
        outcome = HIT
        if fleet[(i, j)] == []:
            outcome = SUNK
        else:
            for square in fleet[(i, j)]:
                fleet[square].remove((i, j))
        del fleet[(i, j)]
        if not fleet:
            outcome = GAME_OVER
    board[i][j] = OLD_SHOT
    return outcome


def print_board_with_fleet(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(' ', board[i][j], end='')
        print()
    print()


def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] != OLD_SHOT:
                print(f' {FOG} ', end='')
            else:
                print(f' {board[i][j]} ', end='')
        print()
    print()


def load_game(file):
    file = open(file, 'rb')
    boards = pickle.load(file)
    fleets = pickle.load(file)
    player = pickle.load(file)
    is_human = pickle.load(file)
    old_moves = pickle.load(file)
    file.close()
    return boards, fleets, player, is_human, old_moves


def save_game(boards, fleets, player, is_human, old_moves):
    file = open('save.pkl', 'wb')
    pickle.dump(boards, file)
    pickle.dump(fleets, file)
    pickle.dump(player, file)
    pickle.dump(is_human, file)
    pickle.dump(old_moves, file)
    file.close()


menu()

