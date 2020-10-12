"""
very basic oop challenge - classes implementations
"""

import math


class Line:
    """
    line object in 2D world
    """
    def __init__(self, coor1, coor2):
        """
        :param coor1: expecting int or float (x,y) coordinate
        :param coor2: expecting int or float (x,y) coordinate
        """
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        """
        :return: distance between 2 points of the line
        """
        return math.sqrt((self.coor2[0]-self.coor1[0])**2 +
                         (self.coor2[1]-self.coor1[1])**2)

    def slope(self):
        """
        :return: slope of the line
        """
        return (self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0])


class Cylinder:
    """
    cylinder object in 3D world
    """
    def __init__(self, height=1.0, radius=1.0):
        """
        :param height: h dimension of the cylinder to create
        :param radius: r dimention of the cylinder to create
        """
        self.height = height
        self.radius = radius

    def volume(self):
        """
        :return: volume of the cylinder in h,r units^3
        """
        return self.height * math.pi*(self.radius**2)

    def surface_area(self):
        """
        :return: surface area of the cylinder in h,r units^2
        """
        return self.height*2*math.pi*self.radius + 2*math.pi*(self.radius**2)


class Account:
    """
    bank account object for a single owner
    """
    def __init__(self, owner='', balance=0):
        """
        :param owner: name of the sole owner of this account
        :param balance: opening balance
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        :param amount: amount of money to deposit
        :return: prints new balance
        """
        self.balance += amount
        print(f'deposit of {amount} accepted; new balance = {self.balance}')

    def withraw(self, amount):
        """
        :param amount: amount of money to withraw
        :return: prints new balance
        """
        if self.balance > amount:
            self.balance -= amount
            print(f'withrawal of {amount} accepted; new balance = {self.balance}')
        else:
            print(f'withrawal of {amount} rejected; balance = {self.balance}')
