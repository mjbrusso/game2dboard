from game2dboard import *

total = 0
killed = 0
level = 1
time = 1000

def mousefn(btn, lin, col):
    global killed, level, total, time
    if game[lin][col] == "mosquito":
        game[lin][col] = "injured"
        killed += 1
        if killed == 1:  # Level up
            level += 1
            killed = 0
            total = 0
            time -= 100
            if time == 0:
                game.stop_timer()
                game.print("You win!  [R]: Restart")
            else:
                game.start_timer(time)


def timer():
    global total
    game.clear()
    game[0][0] = "mosquito"
    game.shuffle()
    total += 1
    game.print("Level {}        Killed {}/{}     [R]: Restart"
               .format(level, killed, total))


def tecladofn(key):
    global killed, level, total, time
    if key == "r":
        start()


def start():
    global total, killed, level, time
    total = 0
    killed = 0
    level = 1
    time = 1000
    game.start_timer(time)
    timer()


game = Board(10, 10)
game.title = "Kill the mosquito"
game.cursor = "crosshair"
game.cell_size = 50
game.cell_color = "black"
game.grid_color = "#303030"
game.margin_color = "#303030"
game.on_mouse_click = mousefn
game.on_key_press = tecladofn
game.on_start = start
game.on_timer = timer
game.create_output(background_color="#606060",
                   color="white",
                   font_size=12)
game.show()
