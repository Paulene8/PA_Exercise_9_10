#   Part 3: Practice with complex maths
#   At a barrel height of 0.5m, an elevation of 80 degrees, and an initial velocity of 44m/s, what is the height of the projectile?
import cmath

# g = acceleration due to gravity: 9.81 m/s squared
# v = initial velocity m/s
# 0 = (theta) elevation angle in radians (80 * (pi/180))
# x = the horizontal distance travelled
# yo = height of the barrel in (m)

# values assigned to each variable
barrelHeight = 1
horizontalDistance = 0.5
elevation = 80 * (cmath.pi / 180)
# print(elevation)
velocity = 44
acceleration = 9.81 ** 2
# print(acceleration)

# created variables for each part of the formula
tan = barrelHeight + horizontalDistance * cmath.tan(elevation)
vel_dist = acceleration * horizontalDistance ** 2
cos = 2 * (velocity * cmath.cos(elevation)) ** 2

# variable assigned to the formula to calculate the overall height of the projectile
projectileHeight = tan - vel_dist / cos

# projectileHeight = barrelHeight + horizontalDistance * cmath.tan (elevation) - acceleration * horizontalDistance ** 2/2 * (velocity * cmath.cos (elevation)) ** 2
# Q: How do I remove the brackets around the answer?
# Response to the question is string concatenated with the calculation
print(projectileHeight)
print("The height of the projectile is", projectileHeight, "metres")
