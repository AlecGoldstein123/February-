import random

'''tries=0
while True:
    if tries<6:
        for i in range(3):
            print(random.randint(1,6))
            tries = tries+1
    else:
        break'''

name = input("Enter your name: ")
print("Hi", name, "I am thinking of a number between 1 and 500. Can you guess it?")

computer_number= random.randint(1,501)

total_guesses= 0

while total_guesses<10:
    guess = int(input("Enter your guess: "))
    total_guesses= total_guesses+1

    if guess<computer_number:
        print("The number I am thinking of is higher. Try again.")
    elif guess> computer_number:
            print("The number I am thinking of is lower. Try again.")
    elif guess == computer_number:
            print("Congrats!", name, "has guessed the number in", total_guesses, "attempts")
    if total_guesses==10:
            print(name, "failed... I win, haha")
            break
        
