# This is where you will copy and paste your full program
# ---------------------------------------------------------
# Project #1 - Punkin Chunkin
# ----------------------------------------------
# Coded by: Malika Iyer
# ----------------------------------------------

# Do Not delete these global constants
# Global Constants
import math
import cisc106
import matplotlib.pyplot as plt
import json
import pumpkin_chunkin_display as disp
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Add your global constants from Problem 1
PUMPKIN_X = 100
PUMPKIN_Y_MIN = 0
PUMPKIN_Y_MAX = SCREEN_HEIGHT // 4
PUMPKIN_ANGLE_MIN = 0
PUMPKIN_ANGLE_MAX = 80
PUMPKIN_v0_MIN = 10
PUMPKIN_v0_MAX = 100
GRAVITY = 9.81

# Problem 2
def get_valid_integer(min, max):
    """
    Repeatedly asks the user to enter values until a valid integer value between the minimum and maximum (both inclusive) is entered. The function should then return this value
    Parameters:
        min (int): the minimum value of the range in which the user's input can be
        max (int): the maximum value of the range in which the user's input can be
    Returns:
        user_input (int): the user's input within the given range
        message (str): a message to the user that displays the min and max values
    """
    print("The max value is", max, ", and the min value is", min)
    user_input = input("Please input a number:")
    while (
        user_input.isdigit() == False or int(user_input) < min or int(user_input) > max
    ):
        user_input = input("Please input a number:")
    return int(user_input)


# get_valid_integer(0, 100)

# Problem 3
def set_up_target():
    """
    Function that consumes no arguments are returns the x and y coordinates of the target
    Parameters:
        None
    Returns:
        x (int): x-coordiate of the target
        y (int): y-coordinate of the target
    """
    x = random.randint(400, 700)
    y = random.randint(100, 300)
    print("x =", x, "and y=", y)
    return x, y


# Problem 4
def get_init_pumpkin_height():
    """
    Asks the user to enter the pumpkin's iniitial height and get a response.
    Parameters:
        none
    Returns:
        initial_height (float): pumpkin's initial height
    """
    initial_height = get_valid_integer(PUMPKIN_Y_MIN, PUMPKIN_Y_MAX)
    return initial_height


def get_pumpkin_angle():
    """
    Asks the user to enter the pumpkin's  angle and get a response.
    Parameters:
        none
    Returns:
        initial_angle (float): pumpkin's initial angle
    """
    initial_angle = get_valid_integer(PUMPKIN_ANGLE_MIN, PUMPKIN_ANGLE_MAX)
    return initial_angle


def get_pumpkin_v0():
    """
    Asks the user to enter the pumpkin's iniitial speed and get a response.
    Parameters:
        none
    Returns:
        v0 (float): pumpkin's initial speed
    """
    v0 = get_valid_integer(PUMPKIN_v0_MIN, PUMPKIN_v0_MAX)
    return v0


# Problem 5
def compute_vx_vy(v0, initial_angle):
    """
    Consumes the pumpkin's initial speed and angle and returns the speed in the x direction (vx) and speed in the y direction (vy)
    Parameters:
        v0 (float): pumpkin's initial speed
        initial_angle: pumpkin's angle
    Returns:
        vx (float): speed in the x direction
        vy (float): speed in the y direction
    """
    initial_angle = math.radians(initial_angle)
    vx = math.cos(initial_angle)
    vx = v0 * vx
    vx = round(vx, 2)
    vy = math.sin(initial_angle)
    vy = v0 * vy
    vy = round(vy, 2)
    return vx, vy


cisc106.assert_equal(compute_vx_vy(30, 25), (27.19, 12.68))
cisc106.assert_equal(compute_vx_vy(80, 60), (40.00, 69.28))
cisc106.assert_equal(compute_vx_vy(40, 25), (36.25, 16.90))
cisc106.assert_equal(compute_vx_vy(20, 10), (19.70, 3.47))
cisc106.assert_equal(compute_vx_vy(10, 20), (9.40, 3.42))

# Problem 6
def move_pumpkin(currentx, currenty, vx, vy):
    """
    Consumes the pumpkin's current location and speed and updates and returns the pumpkin’s new x and y location and the new speed in the y direction. This function represents how the pumpkin would move along its trajectory in one second of te. (t = 1)
    Parameters:
        currentx (float):current x coordinate of pumpkin
        currenty (float): current y coordinate of pumpkin
        vx (float): current speed in x direction of pumpkin
        vy (float): current speed in y direction of pumpkin
    Returns:
        (float): new x coordinate of pumpkin
        (float): new y coordinate of pumpkin
        (float): new velocity in y-direction of the pumpkin
    """
    # t = 1
    # h_dist = vx*t
    # v_dist = currenty + (vy*t) - ((g*(t**2))/2)
    currentx = currentx + vx
    currenty = currenty + vy - (0.5 * GRAVITY)
    vy -= GRAVITY
    return round(currentx, 2), round(currenty, 2), round(vy, 2)


cisc106.assert_equal(move_pumpkin(100, 150, 20, 25), (120, 170.09, 15.19))
cisc106.assert_equal(move_pumpkin(300, 10, 50, -15), (350, -9.91, -24.81))

cisc106.assert_equal(move_pumpkin(90, 170, 20, 25), (110.00, 190.09, 15.19))
cisc106.assert_equal(move_pumpkin(120, 70, 50, -15), (170.00, 50.09, -24.81))
cisc106.assert_equal(move_pumpkin(100, 90, -20, 15), (80.00, 100.09, 5.19))

# Problem 7
def is_target_hit(xpumpkin, ypumpkin, xtarget, ytarget):
    """
    Consumes the x coordinate of the pumpkin, the y coordinate of the pumpkin, the x coordinate of the target and the y coordinate of the target and returns a bool indicating whether the pumpkin hit the target.
    Parameters:
        xpumpkin (float): the x-coordinate of the pumpkin
        ypumpkin (float): the y-coordinate of the pumpkin
        xtarget (float): the x-coordinate of the target
        ytarget (float): the x-coordinate of the target
    Returns:
        is_target_hit (bool): Tells us with a true or false if the target is hit
    """
    if abs(xpumpkin - xtarget) <= 15 and abs(ypumpkin - ytarget) <= 15:
        return True
    else:
        return False


cisc106.assert_equal(is_target_hit(450, 100, 460, 105), True)
cisc106.assert_equal(is_target_hit(450, 100, 460, 125), False)

cisc106.assert_equal(is_target_hit(300, 200, 500, 600), False)
cisc106.assert_equal(is_target_hit(300, 200, 299, 199), True)
cisc106.assert_equal(is_target_hit(300, 200, 315, 185), True)

# Problem 8
def is_off_screen(xpumpkin, ypumpkin):
    """
    Consumes the x coordinate of the pumpkin and the y coordinate of the pumpkin and returns a bool indicating if the pumpkin is off the top, bottom or right side of the screen.
    Parameters:
        xpumpkin: the x coordinate of the pumpkin
        ypumpkin: the y coordinate of the pumpkin
    Returns:
        Bool indicating if the pumpkin is off the top, bottom or right side of the screen.
    """
    if (
        xpumpkin >= SCREEN_WIDTH
        or xpumpkin <= 0
        or ypumpkin >= SCREEN_HEIGHT
        or ypumpkin <= 0
    ):
        return True
    else:
        return False


cisc106.assert_equal(is_off_screen(100, -100), True)
cisc106.assert_equal(is_off_screen(800, 100), True)

cisc106.assert_equal(is_off_screen(200, 100), False)
cisc106.assert_equal(is_off_screen(1000, 200), True)
cisc106.assert_equal(is_off_screen(-100, 0), True)

# Problem 9
def compute_trajectory(
    x_target, y_target, x_pumpkin, y_pumpkin, angle_pumpkin, v_pumpkin
):
    """
    Function that computes the trajectory of the pumpkin based on the pumpkin's initial values and returns a list of the pumpkin's x coordinates and a list of the pumpkin's y coordinates (in that order) for each second that the pumpkin is in the air.
    Parameters:
        x_target (float): x coordinate of the target
        y_target (float): y coordinate of the target
        x_pumpkin (float): x coordinate of the pumpkin
        y_pumpkin (float): y coordinate of the pumpkin
        angle_pumpkin (float): angle of the pumpkin
        v_pumpkin (float): speed of the pumpkin
    Returns:
        xvalues: list of x-coordinates the pumpkin was for each second the pumpkin was in the air
        yvalues: list of y-coordinates the pumpkin was for each second the pumpkin was in the air
    """
    xvalues = [x_pumpkin]
    yvalues = [y_pumpkin]
    # vx, vy = compute_vx_vy(v_pumpkin, angle_pumpkin)
    vx, vy = compute_vx_vy(v_pumpkin, angle_pumpkin)
    while (
        is_off_screen(x_pumpkin, y_pumpkin) == False
        and is_target_hit(x_pumpkin, y_pumpkin, x_target, y_target) == False
    ):
        x_pumpkin, y_pumpkin, vy = move_pumpkin(x_pumpkin, y_pumpkin, vx, vy)
        xvalues.append(x_pumpkin)
        yvalues.append(y_pumpkin)
    if is_off_screen(x_pumpkin, y_pumpkin) == True:
        print("You missed!")
    elif is_target_hit(x_pumpkin, y_pumpkin, x_target, y_target) == True:
        print("You hit the target!")

    return xvalues, yvalues


# Problem 11
def play_punkin_chunkin(x_target, y_target):
    """
    Function that consumes no arguments and implements the following steps:
    1. describe the game to the user
    2. get the user's selections for the pumpkin's initial values of height, angle and speed
    3. compute the pumpkin’s trajectory
    4. return the list of the pumpkin's x values followed by the list of the pumpkin's y values

    Parameters:
        None
    Returns:
        The list of the pumpkin's x values (x_values) (str), the list of the pumpkin's y values (y_values)
        Whether the user hit or missed the target (str), initial height of pumpkin (y_height) (integer),
    """
    # print("In this game, you will enter values for your pumpkin's height, angle and speed, and try to hit the target this way. Good luck! ")
    # x_target, y_target = set_up_target()
    print("Please enter an integer value for the pumpkin height")
    y_pumpkin = get_init_pumpkin_height()
    print("Please enter an integer value for the pumpkin angle")
    angle_pumpkin = get_pumpkin_angle()
    print("Please enter an integer value for the pumpkin speed")
    v0 = get_pumpkin_v0()
    x_values, y_values = compute_trajectory(
        x_target, y_target, PUMPKIN_X, y_pumpkin, angle_pumpkin, v0
    )
    return x_values, y_values, y_pumpkin, angle_pumpkin, v0


# Problem 12
def store_trial_data(x_values, y_values, y_pumpkin, angle_pumpkin, v0):
    """
    Function that creates and returns a dictionary with pumpkin's trajectory x values, pumpkin's trajectory y values, initial height of pumpkin, angle of pumpkin, initial speed of pumpkin.
    Parameters:
        x_values (list, str): the list of x values for the pumpkin's trajectory
        y_values (list, str): the list of y values for the pumpkin's trajectory
        y_pumpkin (int): the pumpkin's initial y value
        angle_pumpkin (int): the pumpkin's initial angle
        v0 (int): the pumpkin's initial speed
    Returns:
        dict1 (dictionary): a dictionary with "x_vals", "y_vals", "init_height", "angle", and "v0"
    """
    trial_values = {
        "x_vals": x_values,
        "y_vals": y_values,
        "init_height": y_pumpkin,
        "angle": angle_pumpkin,
        "v0": v0,
    }
    return trial_values


# Problem 13 continued
def plot_trajectories(list_trial_values, x_target, y_target):
    """
    Function that for each dictionary in the list of trial data plots the trajectory paths using the x and y values, adds the
    height, speed and angle of the pumpkin in the legend, and adds a circle to represent the pumpkin's last location
    Parameters:
        list_trial_values (list):
        x_target (int): the x coordinate of the target
        y_target (int): the y coordinate of the target
    Returns:
        fig: the matplot figure
        ax: the matplot axes
    """

    # print("plot_trajectories under construction")
    fig, ax = plt.subplots()
    for trial_values in list_trial_values:
        x_values = trial_values["x_vals"]
        y_values = trial_values["y_vals"]
        ax.plot(x_values, y_values, color="g", label="Pumpkin")
        pumpkin_circle = plt.Circle((x_values[-1], y_values[-1]), 15, color="g")
        ax.add_artist(pumpkin_circle)
        ax.legend(
            [
                "Initial height:"
                + str(trial_values["init_height"])
                + "\nInitial angle: "
                + str(trial_values["angle"])
                + "\nInitial speed: "
                + str(trial_values["v0"])
            ]
        )
    plt.xlim([0, SCREEN_WIDTH - 100])
    plt.ylim([-100, SCREEN_HEIGHT - 100])
    ax.grid()
    plt.title("The trajectory of your pumpkin")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    target_circle = plt.Circle((x_target, y_target), 25, color="g")
    ax.add_artist(target_circle)
    plt.show()
    return fig, ax


# Problem 14
def play_trial_rounds(x_target, y_target):
    """
    Function that will give the user three trial turns by calling play_punkin_chunkin three times
    Parameters:
        x_target (int): the x coordinate of the target
        y_target (int): the y coordinate of the target
    Returns:
        None
    """
    count = 0
    list_trial_values = []
    while count < 3:
        x_values, y_values, y_pumpkin, angle_pumpkin, v0 = play_punkin_chunkin(
            x_target, y_target
        )
        trial_values = store_trial_data(
            x_values, y_values, y_pumpkin, angle_pumpkin, v0
        )
        list_trial_values.append(trial_values)
        plot_trajectories(list_trial_values, x_target, y_target)
        count += 1


# Problem 15
def get_global_values(filename):
    """
    function that opens and reads the variable data from a json file
    Parameters:
        filename (str): name of the json file
    Returns:
        json_dict (dictionary): a dictionary with all the loaded data from the json file.
    """
    globalvar = open(filename, "r")
    data = globalvar.read()
    json_data = json.loads(data)
    json_dict = {}
    for key, value in json_data.items():
        json_dict[key] = value
    return json_dict
    globalvar.close()


# Problem 16
def set_global_values(globalval_dict):
    """
    Function that assigns the values mapped to each key to the corresponding global constant.
    Parameters:
        globalval_dict: A dictionary with the
    Returns:
        None
    """
    global PUMPKIN_X
    PUMPKIN_X = globalval_dict.get("PUMPKIN_X")
    global PUMPKIN_Y_MIN
    PUMPKIN_Y_MIN = globalval_dict.get("PUMPKIN_Y_MIN")
    global PUMPKIN_Y_MAX
    PUMPKIN_Y_MAX = globalval_dict.get("PUMPKIN_Y_MAX")
    global PUMPKIN_ANGLE_MIN
    PUMPKIN_ANGLE_MIN = globalval_dict.get("PUMPKIN_ANGLE_MIN")
    global PUMPKIN_ANGLE_MAX
    PUMPKIN_ANGLE_MAX = globalval_dict.get("PUMPKIN_ANGLE_MAX")
    global PUMPKIN_v0_MIN
    PUMPKIN_v0_MIN = globalval_dict.get("PUMPKIN_v0_MIN")
    global PUMPKIN_v0_MAX
    PUMPKIN_v0_MAX = globalval_dict.get("PUMPKIN_v0_MAX")


# Problem 17
def play_game(file_global_val):
    """
    Function that
    1. Describes the game to the used
    2.Sets the global constant values
    3. Sets the target location
    4. Lets the user know they will play their 3 trial rounds
    5. Lets the user know that they are launching their pumpkin
    6. Calls play_punkin_chunkin() one last time
    7. Calls display_chunk method from your pumpkin_chunkin_display.py file to display the final pumpkin trajectory to the user
    Parameters:
        file_global_val(file): name of the file that contains the global values
    Returns:
        None
    """
    print(
        "In this game, you will try to hit the target with the pumpkin by entering values for the pumpkin's height, angle and speed. You will get three trial rounds before the final competition. "
    )
    global_val_dict = get_global_values(file_global_val)
    set_global_values(global_val_dict)
    x_target, y_target = set_up_target()
    print("Now we will start your 3 trial rounds before the final competition")
    play_trial_rounds(x_target, y_target)
    print("You will now launch your pumpkin for the competition")
    x_values, y_values, y_pumpkin, angle_pumpkin, v0 = play_punkin_chunkin(
        x_target, y_target
    )
    disp.display_chunk(x_values, y_values, x_target, y_target)


play_game("initial_values_2.json")
