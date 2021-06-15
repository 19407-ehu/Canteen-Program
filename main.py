#Fraser High Canteen Assessment - Harley Lambert-Ehu

#Sequence 1: a normal te reo greeting
name = input("Kia Ora! what's your name? ") 

print("Nice to meet ya, " + name)


#Sequence 2: 

program_continue = print("Cool! So here's what we've got")

end_program = print("Ok then. Have a nice day.")

print(input("would you like to see the menu? "))
answer = input().lower()
if answer == "yes" or answer == "y":
  answer = "yes"
  print(program_continue)

elif answer == "no" or answer == "no":
  answer = "no"
  print(end_program)
  exit

else:
  print("Sorry, was that a yes or no?")









