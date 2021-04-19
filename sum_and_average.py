print("------------------------------------------------------------------------")
print("     SUM AND AVERAGE")
print("------------------------------------------------------------------------")
print("Input some integers to calculate their sum and average. Input 0 to exit.")
print("------------------------------------------------------------------------")
count = 0
sum = 0.0
numbers = []
while True:
	num = int(input(""))
	
	if num == 0:
	    break
	
	sum = sum + num
	numbers.append(num)
	count += 1

	
print(sum/count, " is the Average and ", sum, "is the Sum of", ' and '.join(map(str, numbers)))
print("------------------------------------------------------------------------")
print("                 THANK YOU!")
print("------------------------------------------------------------------------")
