def reverse_evens():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    while(num1 < num2):
        num2 -=1
        if(num2 % 2 == 0):
            print(num2)
            
print(reverse_evens())