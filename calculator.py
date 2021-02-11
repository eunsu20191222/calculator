#클래스를 이용해서 계산기를 만들겠슴
class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        add = self.first + self.second
        return add
    
    def subtract(self):
        subtract = self.first - self.second
        return subtract
    
    def multiply(self):
        multiply = self.first * self.second
        return multiply

    def divide(self):
        divide = self.first / self.second
        return divide

    def square(self):
        square = self.first * self.first, self.second * self.second
        return square

    def cube(self):
        cube = self.first * self.first * self.first, self.second * self.second * self.second
        return cube


cal = Calculator(35, 33)
print(cal.multiply())
    

