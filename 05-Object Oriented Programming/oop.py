# very basic oop challenge - classes implementations

import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[0]-self.coor1[0])**2 +
                         (self.coor2[1]-self.coor1[1])**2)

    def slope(self):
        return (self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0])


class Cylinder:

    def __init__(self, height=1.0, radius=1.0):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * math.pi*(self.radius**2)

    def surface_area(self):
        return self.height*2*math.pi*self.radius + 2*math.pi*(self.radius**2)


class Account:

    def __init__(self, owner='', balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'deposit of {amount} accepted; new balance = {self.balance}')

    def withraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'withrawal of {amount} accepted; new balance = {self.balance}')
        else:
            print(f'withrawal of {amount} rejected; balance = {self.balance}')
