
#Fraser High Canteen Assessment - Harley Lambert-Ehu

#Sequence 1: A normal te reo greeting. Harley Lambert-Ehu, 15/06/2021, Version 2, Function: Asks the user what their name is and greets them in Te Reo.

name = input("Hello, welcome te what's your name? ") 
print()
print("Kia Ora, " + name)
print()

#Sequence 2 and 3: Order and receive. Harley Lambert-Ehu, 18/06/2021, version 4, Function: asks the user If they would like to see the menu. If the answer is yes, ask what they would like to order, and tell them how much it costs.

answer = input("Would you like to see the menu? ").lower()
if answer == "yes" or answer == "y":
  print()
  question = input("The Pie is worth $4.50 and the burger is worth $7.89, what would you like to order? ").lower()
  if question == "pie":
    print()
    print("Thank you for ordering the pie! That'll be $4.50 please.")
  
  elif question == "burger":
    print()
    print("Thank you for ordering the Burger! That'll be $7.89 please.")
  
  else:
    print()
    print("Sorry, was that a Pie or Burger?")

  
elif answer == "no" or answer == "n":
  print()
  print("Thank you for coming to the Fraser High Canteen. Have a nice day!")
  

else:
  print()
  print("Sorry, was that a yes or no?")











