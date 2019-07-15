sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
print([len(word) for word in words])
print([len(word) for word in words if word != "the"])
print()

#this code prints positive numbers in the list
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print(list(num for num in numbers if num >= 0))
print()

# this code prints even numbers in the list
numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
print(list(num for num in numbers if num%2 == 0))

# this code prints the capitalized elements along with their length
words = ["hello", "my", "name", "is", "Sam"]
for w in words: print ((w.upper(),len(w))) 
