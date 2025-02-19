class DataInput:
    def __init__(self):
        """Gets input once and stores it in instance variables"""
        self.a, self.b = self.input_number()

    def input_number(self):
        """General input method"""
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        return a, b

    def operation_name(self):
        """General operation name method"""
        return "unknown operation"


class Calculator(DataInput):
    """Class that inherits from DataInput"""
    def calculate(self, operation):
        if operation == "add":
            result = self.a + self.b
        elif operation == "mult":
            result = self.a * self.b
        else:
            result = None  # Avoide error if operation is unknown

        if result is not None:
            print(f"Calculating {self.operation_name(operation)}: {self.a} {'+' if operation == 'add' else '*'} {self.b} = {result}")
        return result

    def operation_name(self, operation):
        """Overriding the method"""
        return "addition" if operation == "add" else "multiplication" if operation == "mult" else "unknown operation"


class AdvancedCalculator(DataInput):
    """Subclass that calculates exponentiation"""
    def power(self):
        result = self.a ** self.b
        print(f"Calculating {self.operation_name()}: {self.a} ** {self.b} = {result}")
        return result

    def operation_name(self):
        """Overriding the method"""
        return "exponentiation"


if __name__ == '__main__':

    calc = Calculator()
    calc.calculate("add")
    calc.calculate("mult")

    adv_calc = AdvancedCalculator()
    adv_calc.power()
