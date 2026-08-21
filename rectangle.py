import math
user_input = input("Enter base and height of the rectangle: ")
base, height = map(float, user_input.split())
area = base * height
print(f"The area of the rectangle with base {base} and height {height} is: {area}")