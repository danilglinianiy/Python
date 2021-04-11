from random import randint

userNum = input('Enter your number:')
a = int(userNum)

n = randint(0, 100)

if(a>n):
    print('Your number is higher')
if(a<n):
    print('Your number lower')
if(a==n):
    print('Thats fantastic, you guessed the number!')

print('\nRand number is: ', n1)
