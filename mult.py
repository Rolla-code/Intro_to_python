def calculate():
	op = input("Type operation you want to perform: Add, Subtract, Multiply, Divide ")
	first = int(input("Enter First number: "))
	second = int(input("Enter Second number: "))
	operand = op.lower()
	result = 0

	if operand == "add":
		result = first + second
	elif operand == "subtract":
		result = first - second
	elif operand == "multiply":
                result = first * second
	elif operand == "divide":
                result = first / second
	return result

print(calculate())
