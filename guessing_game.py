
print('Welcome to the number guessing game!')
import random 

class Error(Exception):
    pass
class Valuetoosmall(Error):
    def __str__(self):
        return f'The value is small, try with a bigger number'
class Valuetoolarge(Error):
    def __str__(self):
        return f'The value is large, try with a smaller number'
    
num = random.randint(30, 200)
while True:
    try: 
        user = int(input('Guess a number: '))
        if user < num:
            raise Valuetoosmall
        elif user > num: 
            raise Valuetoolarge
        break

    except Valuetoolarge as v:
        print(v)
    except Valuetoosmall as vs:
        print(vs)

print('You guessed it correctly! ')
