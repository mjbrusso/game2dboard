from game2dboard import Board

previous_row = previous_col = reversed_cards = match_count = attempts_count = 0
MSG = "ESC: Close    F2: Restart"


def fnkbd(key):
    if key == "Escape":
        game.close()
    elif key == "F2":
        newgame()


def fnmouse(btn, r, c):
    global previous_row, previous_col, reversed_cards, match_count, attempts_count
    if game[r][c] < 10:             # The card isn't flipped
        game[r][c] += 10            # Flip it
        reversed_cards += 1
        if reversed_cards == 2:
            attempts_count += 1
            game.print(MSG, "   #", attempts_count)
            # if two cards are equals.
            if game[r][c] == game[previous_row][previous_col]:
                match_count += 1
                if match_count == 8:             # Game end
                    game.print("You won!  Total: ", attempts_count,
                               " attempts!\tF2: Play again")
            else:                                     # Not match: "un"flip both cards
                game.pause(500)
                game[r][c] -= 10
                game[previous_row][previous_col] -= 10
            reversed_cards = 0
        previous_row = r                                # Save last position
        previous_col = c


def newgame():
    global previous_row, previous_col, reversed_cards, match_count, attempts_count
    previous_row = previous_col = reversed_cards = match_count = attempts_count = 0
    game[0][0] = game[0][1] = 1 ;     game[0][2] = game[0][3] = 2
    game[1][0] = game[1][1] = 3 ;     game[1][2] = game[1][3] = 4
    game[2][0] = game[2][1] = 5 ;     game[2][2] = game[2][3] = 6
    game[3][0] = game[3][1] = 7 ;     game[3][2] = game[3][3] = 8
    game.shuffle()
    game.print(MSG)


game = Board(4, 4)
game.cell_size = 130
game.margin_color = game.grid_color = "wheat1"
game.cell_color = "wheat3"
game.cell_spacing = 2
game.title = "Memory Game"
game.create_output(background_color="wheat4", color="white")
game.on_mouse_click = fnmouse
game.on_key_press = fnkbd
newgame()
game.show()
