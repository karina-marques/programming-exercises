# Write a program to accept a coordinate point in a XY coordinate system 
# and determine in which quadrant the coordinate point lies. 
# Quadrants are defined like this.                
#                ^ y
#                |
#  Quadrant 2    |      Quadrant 1
#                |
#                |
#                |
#----------------------------------> x
#                |
#                |
#                |
#  Quadrant 3    |      Quadrant 4
#                |
#                v
# The point A with coordinates 3, 5 is in the first quadrant
# The point B with coordinates -5, 2 is in the second quadrant
# The point C with coordinates -5, -10 is in the third quadrant
# The point D with coordinates 5, -10 is in the fourth quadrant
# Point on the axes (i.e. with one or both coordinates equal to zero) are a special case
# The program ALSO needs to tell if the point specified by the user is on the X axis,
# on the Y axis or in the point 0,0 (origin of the axis system)
# The point E with coordinates 0, -10 is on the negative part of the Y axis
# The point F with coordinates 0, 10 is on the positive part of the Y axis
# The point G with coordinates -10, 0 is on the negative part of the X axis
# The point H with coordinates 10, 0 is on the positive part of the X axis
# The point D with coordinates 0, 0 is on the axis origin.

x = float(input('Insert the X coordinate: '))
y = float(input('Insert the Y coordinate: '))

x_positive = x > 0 
x_zero = x == 0
y_positive = y > 0
y_zero = y == 0

# x_positive will be either True or False
# y_positive will be either True or False
# x_zero will be either True or False
# y_zero will be either True or False


if x_zero:
    # In this code block, we are sure that x == 0
    if y_zero:
        print("Origin of the axis")
    elif y_positive:
        print("Positive Y axis")
    else: # y is negative
        print("Negative Y axis")
else:
    # In this code block, we are sure that x != 0
    if y_zero:
        if x_positive:
            print("Positive X axis")
        else:
            print("Negative X axis")
    else:
        # In this code block we are sure that y != 0
        if x_positive:
            if y_positive:
                print("Quadrant 1")
            else:
                print("Quadrant 4")
        else: # x is negative
            if y_positive:
                print("Quadrant 2")
            else:
                print("Quadrant 3")