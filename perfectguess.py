from random import randint
val = randint(1,10)
flag = 'Wrong'
count = 0
while(flag=='Wrong'):
    guess = int(input("Guess the no. (1-10): "))
    count += 1
    if guess == val:
        print(f'You took {count} chances to guess it correctly')
        flag = 'Correct'
        print(f'Original value: {val} and Your choice: {guess}')
        break
    elif guess < val:
        print("Higher no. please")
    else:
        print("Lower no. please")
