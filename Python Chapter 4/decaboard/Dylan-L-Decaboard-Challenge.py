#
# Dylan Le Voguer Decaboard Challenge
#

import decaboard


def angleIt(row, col, elapsed_seconds):

    # belly
    if 2 <= row <= 7 and 3 <= col <= 6:
        # the following are inside the belly allow them to overwrite their respective pixels
        
        if row == 3 and col == 4:
            decaboard.turtle.color("grey")
            return 45
        if row == 3 and col == 6:
            decaboard.turtle.color("grey")
            return 45

        # beak
        if row == 4 and col == 5:
            decaboard.turtle.color("orange")
            return 45

        # corners of belly
        if row == 7 and col == 3:
            decaboard.turtle.color("purple")
            return 0
        if row == 2 and col == 3:
            decaboard.turtle.color("purple")
            return 0
        if row == 7 and col == 6:
            decaboard.turtle.color("purple")
            return 0
        if row == 2 and col == 6:
            decaboard.turtle.color("purple")
            return 0
        decaboard.turtle.color("white")
        return 0

    if row == 3 and col == 4:
        decaboard.turtle.color("grey")
        return 45
    if row == 3 and col == 6:
        decaboard.turtle.color("grey")
        return 45

    # feet
    if row == 9 and 2 <= col <= 3:
        decaboard.turtle.color("orange")
        return 0
    if row == 9 and 6 <= col <= 7:
        decaboard.turtle.color("orange")
        return 0

    if row == 8 and col == 2:
        decaboard.turtle.color("orange")
        return 0
    if row == 8 and col == 7:
        decaboard.turtle.color("orange")
        return 0

    # body

    if 2 <= row <= 7 and col == 2:
        decaboard.turtle.color("purple")
        return 0
    if 2 <= row <= 7 and col == 7:
        decaboard.turtle.color("purple")
        return 0
    if row == 8 and 3 <= col <= 6:
        decaboard.turtle.color("purple")
        return 0
    if row == 1 and 3 <= col <= 6:
        decaboard.turtle.color("purple")
        return 0
    if row == 0 and 4 <= col <= 5:
        decaboard.turtle.color("purple")
        return 0

    # flippers
    if 4 <= row <= 6 and col == 1:
        decaboard.turtle.color("purple")
        return 0
    if row == 6 and col == 0:
        decaboard.turtle.color("purple")
        return 0
    if 4 <= row <= 6 and col == 8:
        decaboard.turtle.color("purple")
        return 0
    if row == 6 and col == 9:
        decaboard.turtle.color("purple")
        return 0

    # changes background color
    decaboard.turtle.color("black")


#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)



