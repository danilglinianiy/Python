from math import sqrt


firstNum = input('Enter n:')
n = int(firstNum)
secondNum = input('Enter m:')
m = int(secondNum)

z = sqrt(2) - sqrt(3*n) / 2*m
print('z =', z)