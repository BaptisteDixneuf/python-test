from __future__ import annotations
import math


class Point2D():
   def __init__(self, x, y):
       self.x = x
       self.y = y

   def distance_to_0(self):
       calcul = math.sqrt( ((self.x-0)**2) + ((self.y-0)**2) )
       return calcul

   def distance_to_other(self, other:Point2D):
        calcul = math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )
        return calcul

   def print_values(self):
       ma_chaine = "x : {} , y : {} ".format(self.x, self.y)
       return ma_chaine

point1 =  Point2D(4,4)
point2 =  Point2D(3,3)


print(point1.distance_to_0())
print(point1.distance_to_other(point2))