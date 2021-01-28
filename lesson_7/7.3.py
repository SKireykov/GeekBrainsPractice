class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'{self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'{sub} ' if sub > 0 else 'Клетка разрушилась'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cell = Cell(25)
cell_2 = Cell(3)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))
print(cell.make_order(7))