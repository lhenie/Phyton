print("-----------------------------------------------------")
print("  PICK YOUR LUCKY NUMBER!")
print("-----------------------------------------------------")
num = 0
while num != 7:
    guess = int(input("Enter the lucky number: "))
    if (guess == 7):
        break
    print ("Try again!\n")
print("YOU'VE GOT THE LUCKY NUMBER!")
print("-----------------------------------------------------")
print("                 THANK YOU!")
print("-----------------------------------------------------")