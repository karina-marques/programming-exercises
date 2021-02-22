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

x = float(input('Insert the X coordinate: '))
y = float(input('Insert the Y coordinate: '))

# Program goes here