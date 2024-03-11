val = input("Välj 1/2/3/4:")


class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        self.res = 0

    def add(self):
        self.res = self.num1 + self.num2
        return self.res

    def subtract(self):
        self.res = self.num1 - self.num2
        return self.res

    def multiply(self):
        self.res = self.num1 * self.num2
        return self.res

    def divide(self):
        self.res = self.num1 / self.num2
        return self.res


if val in ('1', '2', '3', '4'):
    num1 = float(input(f"Ange första numret:"))
    num2 = float(input(f"Ange andra numret:"))
    s = Calculator(num1, num2)
    if val == '1':
        print(f"Resultat", s.add())
    elif val == '2':
        print(f"Resultat", s.subtract())
    elif val == '3':
        s.multiply()
        print(f"Resultat:", s.multiply())
    elif val == '4':
        s.divide()
        print(f"Resultat:", s.divide())
    else:
        print("Ogiltigt val! Välj 1, 2, 3 eller 4")

else:
    print("Ogiltigt val! Välj 1, 2, 3 eller 4.")

