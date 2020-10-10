# scratchpad for python bootcamp
from oop import *


def test_line():
    coordinate1 = (3, 2)
    coordinate2 = (8, 10)

    li = Line(coordinate1, coordinate2)
    print(li.distance())
    print(li.slope())


def test_cyl():
    # c = Cylinder(2, 3)
    c = Cylinder(10,10)
    print(c.volume())
    print(c.surface_area())


def test_acc():
    a = Account('amit', 0)
    a.withraw(50)
    a.deposit(100)
    a.deposit(80000)
    a.withraw(100000)
    a.withraw(20000)
    print(a.owner)


def main():
    test_line()
    test_cyl()
    test_acc()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
