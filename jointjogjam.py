import math

def obtain_distance(x1: int, y1: int, x2: int, y2: int):
    ''' Determine the distance between two points given their 2d coordinates '''
    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    distance = math.sqrt(distance)
    return distance

def obtain_furthest_distance(coordinates):
    starting_dist = obtain_distance(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
    ending_dist = obtain_distance(coordinates[4], coordinates[5], coordinates[6], coordinates[7])
    return max(starting_dist, ending_dist)


coordinates = list(map(int, input().rstrip().split()))
print(obtain_furthest_distance(coordinates))
