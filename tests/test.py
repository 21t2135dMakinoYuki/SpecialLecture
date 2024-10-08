import unittest

from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_1(self):
        printer = CSVPrinter("./sample.csv")
        lines = printer.read()
        print(lines)
        self.assertEqual(3, len(lines))  # add assertion here

    def test_2(self):
        printer = CSVPrinter("./sample.csv")
        lines = printer.read()
        print(lines)

        for line in lines:
            self.assertEqual(4, len(line))


    def test_3(self):
        try:
            printer = CSVPrinter("./sample1.csv")
            printer.read()
            self.fail("This line should not be invoked")
        except FileNotFoundError:
            pass



if __name__ == '__main__':
    unittest.main()
