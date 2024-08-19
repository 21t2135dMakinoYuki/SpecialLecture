import unittest

from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("tests/sample.csv")
        line =printer.read()
        print(line)
        self.assertEqual(3, len(line))  # add assertion here

    def test1(self):
        printer = CSVPrinter("tests/sample.csv")
        line =printer.read()
        print(line)
        self.assertEqual(3, len(line))  # add assertion here

    def test2(self):
        printer = CSVPrinter("tests/sample.csv")
        lines = printer.read()
        print(lines)

        for line in lines:
            self.assertEqual(4, len(line))


    def test3(self):
        try:
            printer = CSVPrinter("tests/sample1.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            pass



if __name__ == '__main__':
    unittest.main()
