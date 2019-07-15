def evens():
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	while(num1 <= num2):
		if(num1%2 == 0):
			return num1
	num1 += 1
print(evens())
