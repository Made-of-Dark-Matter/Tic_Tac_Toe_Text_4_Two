from IPython.display import clear_output
import random
import os

def display_board(board):
    print(f' {board[7]} | {board[8]} | {board[9]} \n-----------\n {board[4]} | {board[5]} | {board[6]} \n-----------\n {board[1]} | {board[2]} | {board[3]} \n')


def player_input():
    player1=''

    while player1!='X' and player1!='O':
        player1=input("Choose 'X' or 'O' for Player 1: " )

        if player1=='X':
            player2='O'
        elif player1=='O':
            player2='X'

        print(f"Player 1 = '{player1}'\nPlayer 2 = '{player2}'")

    return (player1,player2)


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    win_list=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for n in win_list:
        check=[]
        for m in n:
            if board[m]==mark:
                check.append(1)
            else:
                check.append(0)
        if check == [1,1,1]:
            return True
    return False


def choose_first():
    return random.randint(1,2)


def space_check(board, position):
    if board[position] in ['',' ','#','1','2','3','4','5','6','7','8','9']:
        return False
    else :
        return True


def full_board_check(board):
    for pos in range(1,len(board)):

        if space_check(board, pos)==False:
            return False
    return True

def player_choice(board):
    check=True
    mark=0
    while check:
        mark = input('Choose your position: ')

        while (not mark.isdigit()) or (int(mark) not in range(1,10)):
            mark = input('Please choose valid position (1-9): ')

        mark=int(mark)
        check = space_check(board,mark)
        if check==True:
            print(f"Please choose an empty position. {mark} is not empty.")
    return mark


def replay():
    gameon=' '
    while gameon!='y' and gameon!='n':
        gameon = input("Enter 'y' to play again, 'n' to exit:  " )

    if gameon=='y':
        return True
    elif gameon=='n':
        return False

def Tic_Tac_Toe_Game():
    clear = lambda: os.system('cls')
    clear()
    while True:
        print('Welcome to Tic Tac Toe!\n')

        game_board1=['#','1','2','3','4','5','6','7','8','9']
        game_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

        #Game Set Up
        print('\nYour playing field positions on the game board are - \n')
        display_board(game_board1)
        print('\n')
        display_board(game_board)

        (player1,player2)=player_input()

        first=choose_first()

        print('\nTHE GAME IS ON!\n')
        print(f'Player {first} goes first')
        game_on=True
        winner = 0

        while game_on:
            #Player 1 Turn
            if first==1:
                print(f"Player 1 - Mark your '{player1}': ")
                mark=player_choice(game_board)
                game_board=place_marker(game_board, player1, mark)
                clear_output(wait=True)
                clear()
                print('Your playing field positions are - \n')
                display_board(game_board1)
                print('Current Game Board - \n')
                display_board(game_board)
                if win_check(game_board, player1):
                    winner=1
                    game_on=False
                    break
                if full_board_check(game_board):
                    game_on=False
                    break
                first=2

            # Player2's turn.
            if first==2:
                print(f'Player 2 - Mark your {player2}: ')
                mark=player_choice(game_board)
                game_board=place_marker(game_board, player2, mark)
                clear_output(wait=True)
                clear()
                print('Your playing field positions are - \n')
                display_board(game_board1)
                print('Current Game Board - \n')
                display_board(game_board)
                if win_check(game_board, player2):
                    winner=2
                    game_on=False
                    break
                if full_board_check(game_board):
                    game_on=False
                    break
                first=1

        if winner == 0:
            print('The Game tied!')
        elif winner == 1 or winner == 2:
            print(f'Congrats! Player {winner} won!')

        if not replay():
            break
        else:
            clear_output(wait=True)
            clear()
    clear_output(wait=True)
    clear()

if __name__ == '__main__':
    Tic_Tac_Toe_Game()
