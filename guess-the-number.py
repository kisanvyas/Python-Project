# guess the game
import random

print("Enter your name :")
name = input()

print('Hello, ' + name + ', I am thinking a number between 1 and 20')
snumber = random.randint(1,20)
x = bin(snumber)
print('DEBUG: the secret number is : ' + str(x  ))

for guessTaken in range(1,6):
    print("Take a guess ")
    guess = int(input())

    if guess < snumber:
        print("Your number is very low, guess high")
    elif guess > snumber:
        print("Your number is very high, guess low")
    else:
        break

if guess == snumber:
    print('Good job, ' + name + ' ! you guessed right number')
else:
    print('Nope, The number I was thinking of was ' + str(snumber))
    
