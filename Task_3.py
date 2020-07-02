class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        d = self.quantity - other.quantity
        return Cell(d) if d > 0 else print("The result is negative. \n")

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        b = round(self.quantity / other.quantity)
        if b <= 0:
            print("The result is less than 0.")
            return None
        return Cell(b)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += "*" * cells_in_row + "\n"
        row += "*" * (self.quantity % cells_in_row)
        return row


# test
cells_1 = Cell(10)
cells_2 = Cell(5)
# results
print(f"The result of cells' addition is \n"
      f"{cells_1 + cells_2} \n")
c = cells_2 - cells_1
if c is not None:
    print(f"The result of cells' subtraction is \n"
          f"{c} \n")
print(f"The result of cells' multiplication is \n"
      f"{cells_1 * cells_2} \n")
a = cells_1 / cells_2
if a is not None:
    print(f"The result of cells' division is \n"
          f"{a} \n")
print("\n Next task to make_order for cells_2")
print(cells_2.make_order(4))
print("\n Next task to make_order for cells_1")
print(cells_1.make_order(5))

