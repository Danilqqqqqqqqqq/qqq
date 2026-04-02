import math
print('Введите градус:')
z = float(input())
x = math.radians(z)
result = math.sin(x) + math.cos(x) + math.tan(x)**2
print(result)