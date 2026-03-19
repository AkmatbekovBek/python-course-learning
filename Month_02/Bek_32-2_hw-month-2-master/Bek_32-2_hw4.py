data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

letters = [i for i in data_tuple if type(i) != int and type(i) != float ]
numbers = [i for i in data_tuple if type(i) != str and type(i) != bool]

numbers.remove(6.13)

letters.insert(9, True)
letters.remove(True)

numbers.insert(1, 2)

letters[0], letters[-1] = letters[-1], letters[0]
letters[1], letters[-2] = letters[-2], letters[1]
letters[2], letters[-3] = letters[-3], letters[2]
letters[3], letters[-4] = letters[-4], letters[3]
letters[4], letters[-5] = letters[-5], letters[4]

numbers[0], numbers[-1] = numbers[-1], numbers[0]
numbers = [1**2,2**2,3**2]

letters[1] = 'G'
letters[-2] = 'c'
letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)











