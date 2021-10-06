import random
n = random.randint(1, 100)
guess = int(input("Guess an number from 1 to 100 "))
while n !=("guess"):   
    if guess < n:
        print("TOO LOW!")
        guess = int(input("Guess an number from 1 to 100 "))
    elif guess > n:
        print("TOO HIGH!")
        guess = int(input("Guess an number from 1 to 100 "))
    else:
        print("YOU GOT IT!")
        break
        
