#
# Dylan Le Voguer constant rotating decaboard
#

import decaboard


def angleIt(row, col, elapsed_seconds):

    # belly
    if 2 <= row <= 7 and 3 <= col <= 6:

        # eyes, inside the belly color to allow the eye color to cover over the white
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
            return elapsed_seconds
        if row == 2 and col == 3:
            decaboard.turtle.color("purple")
            return elapsed_seconds
        if row == 7 and col == 6:
            decaboard.turtle.color("purple")
            return elapsed_seconds
        if row == 2 and col == 6:
            decaboard.turtle.color("purple")
            return elapsed_seconds
        decaboard.turtle.color("white")
        return elapsed_seconds

    if row == 3 and col == 4:
        decaboard.turtle.color("grey")
        return 45
    if row == 3 and col == 6:
        decaboard.turtle.color("grey")
        return 45

    # feet
    if row == 9 and 2 <= col <= 3:
        decaboard.turtle.color("orange")
        return elapsed_seconds
    if row == 9 and 6 <= col <= 7:
        decaboard.turtle.color("orange")
        return elapsed_seconds

    if row == 8 and col == 2:
        decaboard.turtle.color("orange")
        return elapsed_seconds
    if row == 8 and col == 7:
        decaboard.turtle.color("orange")
        return elapsed_seconds

    # body

    if 2 <= row <= 7 and col == 2:
        decaboard.turtle.color("purple")
        return elapsed_seconds
    if 2 <= row <= 7 and col == 7:
        decaboard.turtle.color("purple")
        return elapsed_seconds
    if row == 8 and 3 <= col <= 6:
        decaboard.turtle.color("purple")
        return elapsed_seconds
    if row == 1 and 3 <= col <= 6:
        decaboard.turtle.color("purple")
        return elapsed_seconds
    if row == 0 and 4 <= col <= 5:
        decaboard.turtle.color("purple")
        return elapsed_seconds

    # flippers
    if 4 <= row <= 6 and col == 1:
        decaboard.turtle.color("purple")
        return elapsed_seconds
    if row == 6 and col == 0:
        decaboard.turtle.color("purple")
        return elapsed_seconds
    if 4 <= row <= 6 and col == 8:
        decaboard.turtle.color("purple")
        return elapsed_seconds
    if row == 6 and col == 9:
        decaboard.turtle.color("purple")
        return elapsed_seconds

    # changes background color
    decaboard.turtle.color("black")

#
# (1200, 200) is the position of the window on the screen when the program
# starts: opens the window at a convenient location. Change it to fit your
# screen.
#
decaboard.run_board(angleIt, 1200, 200)

