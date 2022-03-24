import random
import math

def uniform_random():
    """
    This function uniformly returns a random number 
    between 0 and 1
    """
    return random.uniform(0,1)

def distance_from_origin(point):
    """
    This function returns the distance of a point from 
    origin
    """
    return math.sqrt(point[0]**2 + point[1]**2)

def calculate_pi(n):
    """
    This function calculated the value of pi using 
    only the uniform random function
    """
    
    inside_circle = 0
    outside_circle = 0

    for _ in range(n):
        x = uniform_random()
        y = uniform_random()
        # we call the random function two times to get a 
        # point on 1x1 square on coordinate plane
        
        if distance_from_origin((x,y)) < 1 :
            # counting all points which lie inside circle 
            # of radius 1 unit
            inside_circle += 1
        else:
            outside_circle += 1
    
    # since number of points are directly proportional to area
    # pi can be calculated by calculating ratio of points inside 
    # the circular quadrant to total number of points.

    pi = 4 * inside_circle/n
    print(inside_circle)
    return pi

print("Calculated value of pi is : ", calculate_pi(100000))
