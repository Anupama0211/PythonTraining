"""
Create list compreshension for numbers between 1 to 20 whose square are even numbers
•	[4,16,36, 64,100, 144, 196, 256, 324, 400]
"""

print([i * i for i in range(21) if i * i % 2 == 0])
