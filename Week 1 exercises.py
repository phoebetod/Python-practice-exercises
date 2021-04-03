#name = input("What is your name?")
#print("Hi " + name)

#weather = input("what is the weather like?")
#if weather == "raining":
#   print("Take umbrella")
#else:    print("Wear Coat")

#salary = 200
#salary = salary + salary
#print(salary)


#import random
#myName = input("Hello! What is your name?")
#number = random.randint(1, 10)
#print("Well, " + myName +  " I am thinking of a number between 1 and 10.")
#guess = int(input("Take a guess:") )

#if guess == number:
#    print("Good job," + myName + "! You guessed my number")

#else:
#    print("Wrong")

#number1 = int(input("What is your first number?"))
#number2 = int(input("What is your second number?"))
#print(number1 + number2)

#Homework task 1
#A program that allows the user to enter thier favourite starter, main course, dessert and drink.
starter = input("What is your favourite starter?")
main = input("And what is your favourite main course?")
dessert = input("And then what is your favourite dessert?")
drink = input("Finally what is your favourte drink?")
print("Your favourite meal is " + starter + " followed by " + main + " then for dessert " + dessert + " with a glass of " + drink)

#Homework task 2
#A motorbike costs £2000 and loses 10% of its value every year. Print the bike’s value every year until it falls below £1000.
bikeValue = 2000

while bikeValue >= 1000:
    print(bikeValue)
    bikeValue = bikeValue - (bikeValue*0.1)
    
print("The bike isn't worth very much anymore!")

#Homework task 3 - Basic calculator

num1 = int(input("Please give me your first number"))
num2 = int(input("Please give me your second number"))
operator = input("What would you like to do with your two numbers? 'a' to add, 'b' to subtract, 'c' to divide, 'd' to multiply")

if operator == "a":
    print(num1 + num2)
if operator == "b":
    print(num1 - num2)
if operator == "c":
    print(num1 / num2)
if operator == "d":
    print(num1 * num2)

#Homework task 4
#A program that asks a user for their favourite number and then tells them a joke. The program will call a joke printing function with the user's favourite number.

def joke (favNumber):

    if favNumber % 2 == 1:
        print("joke 1")
    else:
        print("joke 2") 
        
favNumber = int(input("What is your favourite number?"))
joke(favNumber)

