from game2dboard import *
from audioplayer import AudioPlayer
import os

total = killed = 0
level = 1
time = 1000


def mousefn(btn, lin, col):
    global killed, level, total, time
    if game[lin][col] == "mosquito":
        attack_sound.play()
        game[lin][col] = "injured"
        killed += 1
        if killed == 5:  # Level up
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
    total =  killed = 0
    level = 1
    time = 1000
    game.start_timer(time)
    timer()
    mosquito_sound.play(loop=True)
    mosquito_sound.volume = 30


game = Board(10, 10)
game.title = "Kill the mosquito"
game.cursor = "crosshair"
game.cell_size = 50
game.margin = 0
# From: https://opengameart.org/content/good-night
game.background_image = "mountains at night.png"
game.on_mouse_click = mousefn
game.on_key_press = tecladofn
game.on_start = start
game.on_timer = timer
game.create_output(background_color="#606163",
                   color="pink",
                   font_size=12)

sounds_dir = os.path.join(os.path.dirname(__file__), 'sounds')
mosquito_sound = AudioPlayer(os.path.join(
    sounds_dir, 'salamisound-2276970-mosquito-or-similar-in.mp3'))  # From https://www.salamisound.com/2276970-mosquito-or-similar-in
# From https://opengameart.org/content/95-sfx-pack-beats-warrior-nian
attack_sound = AudioPlayer(os.path.join(sounds_dir, 'snd_boss_attack_t2.mp3'))
game.show()
