from game2dboard import Board
from tkinter import messagebox
import random

# Global consts
FIELD_WIDTH = 25
FIELD_HEIGHT = 20
BLOCK_SIZE = 25

# Global vars
snake = []
lastkey = ""


def kbd_fn(key):
    global lastkey
    if key == "F2":
        setup()
    elif key == "Escape":
        field.close()
    elif key in ["Left", "Right", "Up", "Down"]:
        lastkey = key


def timer_fn():
    head_row, head_col = snake[0]
    if lastkey == "Left":
        head_col -= 1
    elif lastkey == "Right":
        head_col += 1
    elif lastkey == "Up":
        head_row -= 1
    elif lastkey == "Down":
        head_row += 1
    caught = False
    if head_col < 0 or head_col >= FIELD_WIDTH or head_row < 0 or head_row >= FIELD_HEIGHT or [head_row, head_col] in snake:
        field.stop_timer()
        if messagebox.askyesno("Snake game", "Game over!\nRestart?"):
            setup()
            return
        else:
            field.close()
    elif field[head_row][head_col] == "fruit":
        fruit_random_position()
        caught = True
    field[head_row][head_col] = 'body'
    snake.insert(0, (head_row, head_col))
    last_row, last_col = snake[-1]
    if not caught:
        field[last_row][last_col] = None
        snake.pop()


def fruit_random_position():
    while True:
        r = random.randint(0, FIELD_HEIGHT-1)   # Random row
        c = random.randint(0, FIELD_WIDTH-1)    # Random collumn
        if field[r][c] is None:                 # It must be an empty place
            field[r][c] = "fruit"
            break


def setup():
    global snake, lastkey
    w2 = FIELD_WIDTH // 2      # field center
    h2 = FIELD_HEIGHT // 2
    field.fill(None)
    snake = [(h2, w2), (h2, w2+1)]      # Initial snake position
    for pos in snake:
        field[pos[0]][pos[1]] = 'body'  # Draw the snake
    fruit_random_position()
    lastkey = "Left"                    # starts moving to the left
    field.start_timer(300)              # 300 ms


field = Board(FIELD_HEIGHT, FIELD_WIDTH)
field.cell_size = BLOCK_SIZE
field.title = "Snake game"
field.cursor = None                         # Hide the cursor
field.margin = 10
field.grid_color = "dark sea green"
field.margin_color = "dark sea green"
field.cell_color = "PaleGreen4"
field.on_key_press = kbd_fn
field.on_timer = timer_fn
setup()
field.show()
