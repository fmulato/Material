
class Data_input():
    def input_number(self):
        a = input("Enter the first number:")
        b = input("Enter the second number:")
        return a, b

class Calculator(Data_input):
    def add(self):
        a, b = self.input_number()
        return int(a) + int(b)
    def mult(self):
        a, b = self.input_number()
        return int(a) * int(b)


if __name__ == '__main__':
    calc = Calculator()
    print(calc.add())
    print(calc.mult())

# create some tests with unittest

