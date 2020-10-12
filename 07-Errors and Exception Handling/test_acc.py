import unittest
import oop


class AccTestCase(unittest.TestCase):
    def test_acc_open(self):
        new_acc = oop.Account('joe', 500)
        self.assertEqual(new_acc.owner, 'joe')
        self.assertEqual(new_acc.balance, 500)

    def test_acc_deposit(self):
        new_acc = oop.Account('joe', 0)
        new_acc.deposit(500)
        self.assertEqual(new_acc.balance, 500)

    def test_acc_withrawal(self):
        new_acc = oop.Account('joe', 500)
        new_acc.withraw(250)
        self.assertEqual(new_acc.balance, 250)


if __name__ == '__main__':
    unittest.main()
