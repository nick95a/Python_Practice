'''
Input:
Take in the number of type of polygon: Triangle, Square, Rectangle and
the coordinates of the points as tuples.

Output:
Area and perimeter of the polygon
'''
from Areas_errors import *
import math


class Area:

    _polygon_types = ('triangle', 'square', 'rectangle')

    def __init__(self, polygon, *args, **kwargs):
        self.points = []
        try:
            if polygon in self._polygon_types:
                self.polygon = polygon
            else:
                self.polygon = input("Input a valid polygon type")
        for arg in args:
            if not isinstance(arg, tuple):
                raise InputError()
            self.points.append(arg)

    def distance(self, point_1, point_2):
        return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

    def calcPerimeter(self):
        perimeter = 0
        for i in range(len(self.points)):
            j = i + 1
            while j < (len(self.points - 1)):
                perimeter += self.distance(self.points[i], self.points[j])
        return perimeter

    def calcArea(self):
        if self.polygon.lower() == 'triangle':

        elif self.polygon.lower() == 'square':

        elif self.polygon.lower() == 'rectangle':

        else:
            raise InvalidPolygon("Only triangle, square or rectangle are permitted")


