import sys

#Fraser High Canteen Assessment - Harley Lambert-Ehu

#Sequence 1: a normal te reo greeting
name = input("Kia Ora! what's your name? ") 

print("Nice to meet ya, " + name)


#Sequence 2: 

input("would you like to see the menu? ")
answer = input().lower()
if answer == "yes" or answer == "y":
  answer = "yes"
  print("Cool! Here's what we have.")

elif answer == "no" or answer == "no":
  answer = "no"
  print("Ok then, have a nice day!")
  sys.exit()

else:
  print("Sorry, was that a yes or no?")











