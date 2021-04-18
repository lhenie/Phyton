print("-----------------------------------------------------")
print("     EVEN/ODD NUMBER!")
print("-----------------------------------------------------")
i=1
even_count = 0
odd_count = 0
num = int(input("Enter a number:"))
print("-----------------------------------------------------")
while i <=num:
    if (i%2==0):
       even_count += 1
    else:
        odd_count += 1
    i += 1
print("Number of even numbers:",even_count)
print("Number of odd numbers:",odd_count)
print("-----------------------------------------------------")
print("                 THANK YOU!")
print("-----------------------------------------------------")