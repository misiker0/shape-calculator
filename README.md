# Polygon Area Calculator

A Python project with a `Rectangle` class and a `Square` class that inherits from it. Built as part of the freeCodeCamp Scientific Computing with Python certification.

## Features

**Rectangle**
- `set_width(width)` and `set_height(height)` change the dimensions
- `get_area()` returns width × height
- `get_perimeter()` returns 2 × (width + height)
- `get_diagonal()` returns the diagonal length
- `get_picture()` returns a text picture made of `*` characters, or `Too big for picture.` if the width or height is over 50
- `get_amount_inside(shape)` returns how many times another shape fits inside this one, without rotating it
- Printing a rectangle shows `Rectangle(width=..., height=...)`

**Square** (a subclass of `Rectangle`)
- Created with a single `side`
- `set_side(side)` changes both width and height
- `set_width(side)` and `set_height(side)` also change both, so the shape always stays a square
- Printing a square shows `Square(side=...)`

## Usage

```python
rect = Rectangle(10, 5)
print(rect.get_area())         # 50
rect.set_height(3)
print(rect.get_perimeter())    # 26
print(rect)                    # Rectangle(width=10, height=3)

sq = Square(9)
print(sq.get_area())           # 81
sq.set_side(4)
print(sq.get_diagonal())       # 5.656854249492381
print(sq)                      # Square(side=4)
print(sq.get_picture())
```

Output of the last line:

```
****
****
****
****
```

Fitting shapes inside each other:

```python
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))   # 8
```

The 16×8 rectangle holds 4 squares across and 2 down, so 8 in total.

## Running it
Requires Python 3. Add your own test code at the bottom of the file, or import the classes from another script.

## What I practiced

- Classes, inheritance, and `super()`
- Overriding methods without causing infinite recursion
- Private attributes and name mangling
- Reading test failures and grouping them by cause
