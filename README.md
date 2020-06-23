# game2dboard

A quick and easy way to create board games using 2d arrays in Python. 
This Python GUI package provides a graphical user interface (GUI) for 2d arrays (matrix). 

- What is the aim of this library?<br>
I created this project to help my students from an introductory course on computer programming at the University of Passo Fundo (Brazil) to write programs with two-dimensional arrays in an easy and fun way. I think it can be useful for others.

- What types of games can be created?<br>
Any that can be modeled on a two-dimensional array, such as checkers, life, tic-tac-toe, chess, 2048, minefield, among many others.

## Installation

You can use the `pip` to install **game2dboard**:

```
pip3 install game2dboard
```


Or install the latest release by cloning the repository:

```bash
git clone https://github.com/mjbrusso/game2dboard.git 
cd game2dboard
python3 setup.py install --user
```


## Usage

The API is documented [bellow](#API) and within the docstrings. 

This simple code only provides an overview. See the examples for more details. 

Before running, copy [this](https://github.com/mjbrusso/game2dboard/blob/master/examples/basic/img/0.png) and [this](https://github.com/mjbrusso/game2dboard/blob/master/examples/basic/img/1.png) files into a `img/` folder [(credits)](https://publicdomainvectors.org).

```python
from game2dboard import Board


def mouse_fn(btn, row, col):    # mouse calback function
    b[row][col] = 1 if not b[row][col] else 0

b = Board(3, 4)         # 3 rows, 4 columns, filled w/ None
b[0][0] = 1
b.title = "Click me!"
b.cell_size = 120       
b.cell_color = "bisque"
b.on_mouse_click = mouse_fn
b.show()
```

#### Result

![Screnshot](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/images/basic.gif)

## Galery

Some screenshots from examples.

| | |
| :------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------: |
| ![memory game](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/images/memory.png) <br> **Memory Game**<br>58 SLOC<br>[View source](https://github.com/mjbrusso/game2dboard/tree/master/examples/memorygame) | ![snake](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/images/snake.png) <br> **Snake**<br>86 SLOC<br>[View source](https://github.com/mjbrusso/game2dboard/tree/master/examples/snake) |
| ![kill the mosquito](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/images/killthemosquito.png) <br> **Kill the mosquito**<br>75 SLOC w/ Background image and Sounds<br>[View source](https://github.com/mjbrusso/game2dboard/tree/master/examples/KillTheMosquito)     |         &nbsp;          |
| | |



## API

### Creation

- `game2dboard.Board(nrows, ncols)`<br>
Creates a Board.
  - `nrows` : *int* – The number of rows.
  - `ncols` : *int* – The number of columns.

### Indexer

- `self[i][j]`<br>
  Gets/sets the value at row `i`, column `j`. 
  
  When assigning a value, the GUI will be updated. If there is an **.png** file in the `img/` folder whose name is the same as the new value, it will be drawn at position `[i][j]` of the board. Otherwise, the value will be displayed as text.

  Example:
  ```python
    b[1][0] = 100            # draw 'img/100.png' @ row 1, column 0
    b[0][2] = "correct"      # draw 'img/correct.png'
    b[3][0] = "wait.png"     # draw 'img/wait.png'
  ```

### Properties

Use properties to access board attributes like public fields.<br>Example:
  ```python
    b.title = "Hello"       # Sets the window title
    sz = b.size             # Gets the total number of elements
  ```
#### Board properties

- `size` : *int* (readonly)<br> 
Number of elements in the array  


- `nrows` : *int* (readonly)<br> 
Number of rows in the array.


- `ncols` : *int* (readonly)<br> 
Number of columns in the array.


- `width` : *int* (readonly)<br> 
Board width, in px. Only available after .show()


- `height` : *int* (readonly)<br> 
Board height, in px. Only available after .show()


- `title` : *str*<br> 
Gets or sets the window title.


- `cursor` : *str*<br> 
Gets or sets the mouse cursor shape. Setting to `None` hides the cursor.<br>
See avaliable cursor names in https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html

- `background_image` : *str*<br> 
Gets or sets the background image file name. The **.png** file must be in the folder `img/`<br>
Setting this property forces `grid_color`, `margin_color` and `cell_color` to `None`.


- `margin` : *int*<br> 
Gets or sets the board margin (px).


- `cell_spacing` : *int*<br> 
Gets or sets the space between cells (px).


- `margin_color` : *str*<br> 
Gets or sets the margin color.


- `cell_color` : *str*<br> 
Gets or sets cells color<br>
See available color names in https://htmlcolorcodes.com/color-names/


- `grid_color` : *str*<br> 
Gets or sets grid color.


- `cell_size` : *int | (int, int)*<br> 
Gets or sets the cells dimension (*width*, *height*).

##### Event properties

- `on_start` : *function()*<br>
Gets or sets the game started callback function.<br>
The GUI is ready and the program is going to enter the main loop.

- `on_key_press` : *function(key: str)*<br>
Gets or sets the keyboard callback function.<br>
See key names in https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html 

- `on_mouse_click` : *function(button: int, row: int, column: int)*<br>
Gets or sets the mouse callback function.


- `on_timer` :  *function()*<br>
Gets or sets the timer callback function.

### Methods

- `show()`<br>
Create the GUI, display and enter the run loop.


- `clear()`<br>
Clear the board, setting all values to `None`.


- `close()`<br>
Close the board, exiting the program.


- `shuffle()`<br>
Random shuffle all values in the board.


- `fill(value, row=None, col=None)`<br>
Fill the board (or a row, or a column) with a value.
    - `value` – The value to store
    - `row` (*int*) – Index of row to fill. Default=`None` (all rows)
    - `col` (*int*) – Index of column to fill. Default=`None` (all columns)

- `copy()`<br>
Returns a shallow copy of the array (only data, not the GUI). 

- `create_output(**kwargs)`<br>
Create a output message bar.
    - `kwargs`:
      - `color` = *str*
      - `background_color` = *str*
      - `font_size` = *int*

- `print(*objects, sep=' ', end='')`<br>
Print message to output bar. <br>
Use like built-in `print()` function.


- `start_timer(msecs)`<br>
Start a periodic timer that executes the a function every `msecs` milliseconds<br>
The callback function must be registered using `.on_timer` property.
    - `msecs` (*int*) – Time in milliseconds.


- `stop_timer()`<br>
Stops the current timer.


- `pause(msecs, change_cursor=True)`<br>
Delay the program execution for a given number of milliseconds.<br>
**Warning:** long pause freezes the GUI!
    - `msecs` (*int*) – Time in milliseconds.
    - `change_cursor` (*bool*) – Change the cursor to “watch” during pause?

## What about Sound?

To play sounds in the game, use my [audioplayer package](https://github.com/mjbrusso/AudioPlayer).

**audioplayer** is a cross platform Python 3 package for playing sounds (mp3, wav, ...). It provides the key features of an player, such as opening a media file, playing (loop/block), pausing, resuming, stopping, and setting the playback volume.

```python
from audioplayer import AudioPlayer
import os

# Background music 
bgm_file = os.path.join(os.path.dirname(__file__), 'background.mp3')
bgm = AudioPlayer(bgm_file)
bgm.volume = 50         # 50% volume
bgm.play(loop=True)     # start playing

# Audio player is lazy loaded (resources loading is delayed until the first time the song is played)
explosion = AudioPlayer(os.path.join(os.path.dirname(__file__), 'explosion.mp3'))

def timer_callback():
    if collides(enemy, bullet):
        explosion.play()
```

For a full example using AudioPlayer, see [Kill the Mosquito](https://github.com/mjbrusso/game2dboard/tree/master/examples/KillTheMosquito)

## What's in the roadmap? 

- `redim(new_ncols, new_nrows)` : Useful to grow or shrink the board, for example, on level up.


## How to Contribute

### Submitting an issue

Use the [issue tracker](https://github.com/mjbrusso/game2dboard/issues) to submit bug reports and features or enhancements requests.


### Translating

You can contribute by translating this document into other languages ​​(except *en* and *pt_br*).

### Submitting a pull request

If you can improve anything in this project, feel free to add a [pull request](https://github.com/mjbrusso/game2dboard/pulls).


## License

game2dboard is under [MIT license](https://github.com/mjbrusso/game2dboard/blob/master/LICENSE). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
