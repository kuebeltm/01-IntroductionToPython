"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Todd Kuebelbeck.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
import math

window = rg.TurtleWindow()

one = rg.SimpleTurtle()
one.Pen = rg.Pen('cyan', 10)
two = rg.SimpleTurtle('turtle')
two.Pen = rg.Pen('purple',10)

one.left(45)
two.left(45)


for k in range(5):
    one.pen_down()
    one.draw_square(20)
    two.forward(math.sqrt(800))
    two.pen_down()
    two.draw_circle(20)
    one.pen_up()
    one.forward(20)

window.close_on_mouse_click()
