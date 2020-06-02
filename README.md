# game2dboard

Python GUI library to easily create board games using 2d arrays.

## Installation

Install the latest release by cloning the repository and use `setuptools`:

```bash
git clone https://github.com/mjbrusso/game2dboard.git 
cd game2dboard
python3 setup.py install --user
```


## Usage

The API is documented within the docstrings and in documentation folder. 
This simple example only provides an overview. See the examples provided for more details.

```python
from game2dboard import Board

def mouse_fn(btn, row, col):
    if btn==1 or btn==4:
        b[row][col] += 1
    else:
        b[row][col] -= 1

b = Board(4, 4)
b.cell_size = 100
b.fill(0)
b.cell_color = "white"
b.grid_color = "black"
b[1][0] = 10
b.on_mouse_click = mouse_fn
b.create_output()
b.print("<left-button>: ++    <right button>: --")
b.show()
```
## TODO
