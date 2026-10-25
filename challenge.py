7
sides=int(input("enter number of sides"))
lenght =int(input("enter the lenght of the side "))
angle=360/sides

from turtle import *
for i in range(sides):
    forward(lenght)
    left(angle)
