import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# The center of the turtle screen is considered x = 0, y = 0
# The x location to the far right would be the value X_OFFSET
# The x location to the far left would be the value -X_OFFSET
# The y location at the top of the screen would be Y_OFFSET
# The y location at the bottom of the screen would be -Y_OFFSET
X_OFFSET = SCREEN_WIDTH // 2
Y_OFFSET = SCREEN_HEIGHT // 2


def draw_star(a_pen, side_length):
    """
    Draws an equilateral star on the Screen
    Parameters:
        a_pen - turtle object
        side_length - int - length of one side of the star
    Returns:
        None
    """
    # accumulator for numbers of sides drawn
    sides_drawn = 0
    col = ["red", "green", "blue", "purple", "yellow"]
    # loop to draw 3 sides

    while sides_drawn < 5:
        # a_pen.pencolor(col[sides_drawn])
        a_pen.forward(200)
        a_pen.right(144)
        sides_drawn += 1


# ------------------------------------------------------
# Problem 18 A
# ------------------------------------------------------


def draw_target(x_location, y_location):
    """
    Draws the target on the Screen -
        target is a star
    Parameters:
        x_location - int - position along x axis for target
        y_location - int - position along y axis for target
    Returns:
        None
    """
    # Set Up a Turtle Pen
    my_pen = turtle.Turtle()
    # Lift pen off canvas
    my_pen.up()
    # Set up pen at specified location
    my_pen.setpos(x_location, y_location)
    # Put pen back onto Screen
    my_pen.down()
    """
    This is where you will develop your own code
    for a target
    """
    # Draw a star on the Screen
    draw_star(my_pen, 100)
    # Lift pen off canvas
    my_pen.up()
    my_pen.setpos(x_location, y_location)
    # Put pen back onto Canvas
    my_pen.down()


# ------------------------------------------------------
# Problem 18 B
# ------------------------------------------------------
def register_pumpkin_image(wn, image_file_name):
    """
    Changes the image of the turtle object to the image in the file
    Parameters:
        image_file_name - str - name of file containing image
                    must be a gif
                    must be located in the same folder as this code file
                    and cannot contain blank spaces in the name
    Returns:
        a turtle object
    """
    wn.register_shape(image_file_name)
    # Create a turtle object and set its shape to your image
    drawing_turtle = turtle.Turtle()
    drawing_turtle.shape(image_file_name)
    # return the turtle
    return drawing_turtle


# ------------------------------------------------------
# Problem 18 C
# ------------------------------------------------------
def set_up_canvas(x_pumpkin, y_pumpkin, x_target, y_target):
    """
    Get the Screen ready for your game
    Parameters:
        wn - str - name of file containing image
                    must be a gif
                    must be located in the same folder as this code file
                    and cannot contain blank spaces in the name
    Returns:
        a turtle object
    """
    # Set up the Screen
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    wn = turtle.Screen()
    # draw your target
    draw_target(x_target, y_target)
    # set up your drawing turtle with YOUR image
    pumpkin = register_pumpkin_image(wn, "pumpkin_image.gif")
    # Move pumpkin to initial location
    pumpkin.penup()
    pumpkin.goto(x_pumpkin, y_pumpkin)
    pumpkin.pendown()
    return pumpkin


# set_up_canvas(100, 200, 300, 200)

# Problem 19
def display_chunk(pumpkin_x_list, pumpkin_y_list, x_target, y_target):
    pumpkin = set_up_canvas(
        pumpkin_x_list[0] - X_OFFSET,
        pumpkin_y_list[0] - Y_OFFSET,
        x_target - X_OFFSET,
        y_target - Y_OFFSET,
    )
    for val in range(len(pumpkin_x_list)):
        # pumpkin.penup()
        pumpkin.goto(pumpkin_x_list[val] - X_OFFSET, pumpkin_y_list[val] - Y_OFFSET)
        # pumpkin.pendown()
    return pumpkin
