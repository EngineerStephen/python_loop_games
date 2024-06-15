# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print()
print("Hey there, welcome to my world!")
print()

user_name=input ("What's your name?").title()
print()
print(user_name, "Welcome! Here are the days of the week!")
print()
for day in days_of_week:
    print(day)
print()
print("Now we are going to choose for you each day of the week, but only if that day is on an even index") 
print(user_name, "Would you like to see it?")

while True:
    user_input = input("Enter 1 if you would like to continue or 2 if you would like to quit")
    if user_input == "2":
        print("It was great playing with you, bye!")
        break
    elif user_input == "1":
        print()
        print("Let's gooooo!")
        break
    else:
        print("Please choose a valid option")
print()

days_enum= enumerate(days_of_week)
if user_input == "1": 
    for i, element in enumerate(days_of_week):
     if i % 2 == 0: 
        print (element)  
print()        
print("End of Game, thank you for playing!")   

#Create a while loop that will terminate after 5 iterations,
# and each iteration you print which iteration it is on. (use a control variable)
user_name=input ("Hello, what's your name?").title()
print()
print(user_name, "Here are a list of US weapons you should check out")

weapons_list = ["Air-to-Air", "AIM-7 Sparrow", "Tuesday", "AIM-9 Sidewinder", "AIM-120 AMRAAM", "AGM-65 Maverick", "AGM-88HARM"]
print()

user_name = input("Hello, what's your name?").title()
print()
print(user_name, "Here are a list of US weapons you should check out")
weapons_list = ["Air-to-Air", "AIM-7 Sparrow", "AIM-9 Sidewinder", "AIM-120 AMRAAM", "AGM-65 Maverick", "AGM-88HARM"]
print()
for weapons in weapons_list:
    print(weapons)
    print()
print("Now we're gonna iterate through the weapons with each weapon and print which iteration we are on")

while True:
    user_input = input("Do you wish to continue? Enter 1 for Yes or 2 for No")
    if user_input == "2":
        print("At least, now you know some weapons we have, bye!")
        break
    elif user_input == "1":
        print()
        print("Alrighty,Here you go:")
        weapons_enum = enumerate(weapons_list)
        for i, element in enumerate(weapons_list):
             print(i, element)
    else:
        print("Please choose a valid option")
print()
print(THE END)


# Task 1: Random Choice Game Create a game where a player has a list of items.
# They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. 
# Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.
print()
print("Hello, welcome to I want to be a billionaire! Here you will guess from the list of items I present which is the choice of the day")
print("If you guess correctly, you will advance to the next stage of the game for an opportunity to win more money")
print("But if you quit, you will forfeit all your gains and owe us 5% of what had you previously gained. Now let's start")
print()
user_name=input ("Let's start by knowing your name. Please enter your beautiful name   ").title()

weapons_list = ["Air-to-Air", "AIM-7 Sparrow", "Tuesday", "AIM-9 Sidewinder", "AIM-120 AMRAAM", "AGM-65 Maverick", "AGM-88HARM"]
print()
print(user_name,"note the following weapons:")

for weapons in weapons_list:
    print(weapons)
    
print()
print(user_name," Which weapon from our list was last used by the US Millitary in the most recent campaign?   ")

import random
correct_answer = random.choice(weapons_list)

while True:
    user_input = input("Do you wish to continue? Enter 1 for Yes or 2 for No   ")
    print()
    if user_input == "2":
        print(user_name, "hehe! You have forfeited all your gains and will pay us 5% of what's in your account. We love you too, bye! ")
        break
    elif user_input == "1":
       user_answer = input("Alrighty, Make your choice. Enter here   ")
       print()
       print("YOUR CHOICE IS", end=" ")
       print(user_answer)
       print("THE CORRECT ANSWER IS")      
       print(correct_answer)
       print() 
       if user_answer == correct_answer:
           print("CONGRATULATIONS, YOU WON! YOU ARE NOW A BILLIONAIRE")
           break
       else:
        print("Hmm, that wasn't quite it. Please try again.")
        print()
    else:  
        print("Please choose a valid option")
