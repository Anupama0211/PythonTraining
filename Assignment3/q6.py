"""
Create dictionary with numbers as key and object as list of [square, cube] using comprehension for number as shown below
•	{1: [1, 1], 2: [4, 8], 3: [9,27], 4: [16, 64]}
"""
print({key: [key ** 2, key ** 3] for key in range(1, 5)})
