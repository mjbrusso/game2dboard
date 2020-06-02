# This is a template for including classes


### class gui2darray.Board(nrows, ncols)
A graphic user interface for a 2d array (matrix)

Creates an App


* **Parameters**

    
    * **nrows** (*int*) – The number of rows.


    * **ncols** (*int*) – The number of columns.



#### property title()
Gets or sets the window title.


* **Type**

    str



#### property cursor()
Gets or sets the mouse cursor shape.


* **Type**

    str



#### property margin()
Gets or sets the board margin (px).


* **Type**

    int



#### property cell_spacing()
Gets or sets the space between cells (px).


* **Type**

    int



#### property margin_color()
Gets or sets the margin_color.


* **Type**

    str



#### property cell_color()
Gets or sets cells color


* **Type**

    str



#### property grid_color()
Gets or sets grid color


* **Type**

    str



#### property cell_size()
Gets or sets the cells dimension (width, height)


* **Type**

    int or (int, int)



#### property on_key_press()
Gets or sets the keyboard callback function


* **Type**

    function(key: str)



#### property on_mouse_click()
Gets or sets the mouse callback function


* **Type**

    function(button: str)



#### property on_timer()
Gets or sets the timer callback function


* **Type**

    function



#### show()
Create the GUI, display and enter the run loop.


#### start_timer(msecs)
Start a periodic timer that executes the a function every msecs milliseconds

The callback function must be registered using .on_timer property.


* **Parameters**

    **msecs** (*int*) – Time in milliseconds.



#### stop_timer()
Stops the current timer.


#### pause(msecs, change_cursor=True)
Delay the program execution for a given number of milliseconds.

Warning: long pause freezes the GUI!


* **Parameters**

    
    * **msecs** (*int*) – Time in milliseconds.


    * **change_cursor** (*bool*) – Change the cursor to “watch” during pause?



#### shuffle()
Random shuffle all values in the board


#### fill(value, row=None, col=None)
Fill the board (or a row, or a column) whith a value


* **Parameters**

    
    * **value** – The value to store


    * **row** (*int*) – Index of row to fill. Default=None (all rows)


    * **col** (*int*) – Index of column to fill. Default=None (all columns)



#### clear()
Clear the board, setting all values to None.


#### close()
Close the board, exiting the program.


#### create_output(\*\*kwargs)

#### print(\*objects, sep=' ', end='')
Return Home
