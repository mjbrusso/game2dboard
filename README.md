# game2dboard

A quick and easy way to create board games using 2d arrays in Python. 
This Python GUI package provides a graphical user interface (GUI) for 2d arrays (matrix). 

- What is the aim of this library?<br>
The aim of the game2dboard is to offer an easy and fun way for students who are new to programming to learn and code programs using arrays.

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

|![memory game](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/images/memory.png) |  ![snake](https://raw.githubusercontent.com/mjbrusso/game2dboard/master/images/snake.png) |
|:---:|:---:|
| **Memory Game**<br>58 SLOC<br>[View source](https://github.com/mjbrusso/game2dboard/tree/master/examples/memorygame)| **Snake**<br>86 SLOC<br>[View source](https://github.com/mjbrusso/game2dboard/tree/master/examples/snake) | 



## API

### Creation

- `game2dboard.Board(nrows, ncols)`<br>
Creates a Board.
  - `nrows` : *int* – The number of rows.
  - `ncols` : *int* – The number of columns.

### Indexer

- `self[i][j]`<br>
  Gets/sets the value at row `i`, column `j`. 
  
  When assigning a value, the GUI will be updated. If there is an **.png** file in the `img/` folder whose name is the same as the new value, it will be drawn in position `[i][j]` of the board. Otherwise, the value will be displayed as text.

  Example:
  ```python
    b[1][0] = 100            # draw 'img/100.png' @ row 1, column 0
    b[0][2] = "correct"      # draw 'img/correct.png'
    b[3][0] = "wait.png"     # draw 'img/wait.png'
  ```

### Properties

Use properties as class attributes or public fields.<br>Example:
  ```python
    b.title = "Hello"       # Sets the window title
    mc = b.margin_color     # Gets the board margin_color
  ```
#### Board properties


- `size` : *int* (readonly)<br> 
Number of elements in the array  


- `nrows` : *int* (readonly)<br> 
Number of rows in the array.


- `ncols` : *int* (readonly)<br> 
Number of columns in the array.


- `title` : *str*<br> 
Gets or sets the window title.


- `cursor` : *str*<br> 
Gets or sets the mouse cursor shape. Setting to `None` hides the cursor.<br>
See avaliable cursor names in https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html


- `margin` : *int*<br> 
Gets or sets the board margin (px).


- `cell_spacing` : *int*<br> 
Gets or sets the space between cells (px).


- `margin_color` : *str*<br> 
Gets or sets the margin color.


- `cell_color` : *str*<br> 
Gets or sets cells color<br>
See available color names in http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter


- `grid_color` : *str*<br> 
Gets or sets grid color


- `cell_size` : *int | (int, int)*<br> 
Gets or sets the cells dimension (*width*, *height*)


- `on_key_press` : *function(key: str)*<br>
Gets or sets the keyboard callback function


- `on_mouse_click` : *function(button: str, row: int, col: int)*<br>
Gets or sets the mouse callback function


- `on_timer` :  *function()*<br>
Gets or sets the timer callback function

### Methods

- `show()`<br>
Create the GUI, display and enter the run loop.


- `clear()`<br>
Clear the board, setting all values to `None`.


- `close()`<br>
Close the board, exiting the program.


- `shuffle()`<br>
Random shuffle all values in the board


- `fill(value, row=None, col=None)`<br>
Fill the board (or a row, or a column) with a value
    - `value` – The value to store
    - `row` (*int*) – Index of row to fill. Default=`None` (all rows)
    - `col` (*int*) – Index of column to fill. Default=`None` (all columns)


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
Warning: long pause freezes the GUI!
    - `msecs` (*int*) – Time in milliseconds.
    - `change_cursor` (*bool*) – Change the cursor to “watch” during pause?


## TO DO 
To do.... ;-)


## How to Contribute

### Submitting an issue

Use the [issue tracker](https://github.com/mjbrusso/game2dboard/issues) to submit bug reports and features or enhancements requests.


### Translating

You can contribute by translating this document into other languages ​​(except *en* and *pt_br*).

### Submitting a pull request

If you can improve anything in this project, feel free to add a [pull request](https://github.com/mjbrusso/game2dboard/pulls).


## License

game2dboard is under [MIT license](https://github.com/mjbrusso/game2dboard/blob/master/LICENSE). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
