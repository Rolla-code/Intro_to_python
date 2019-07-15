def is_even(x):
    if(x % 2 == 0):
        return True
    else:
        return False
    
numbers = [1,56,234,87,4,76,24,69,90,135]
print(list((map(is_even,numbers))))
