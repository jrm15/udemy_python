# LIST COMPREHENSION:

# new_list = [new_item for item in list]

name = "angela"

new_name = [n.upper() for n in name]

range_list = [num*2 for num in range(1, 5)]

print(range_list)

new_name2 = [letter for letter in name if letter == "a"]

print(new_name2)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

numbers_squared = [num * num for num in numbers]

numbers_even = [num for num in numbers if num % 2 == 0]

print (numbers_squared)
print(numbers_even)


# DICTIONARY COMPREHENSION:

# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key,value) in dict.items}

names = ["Javi", "Marta", "Dani"]
i = 0

names_score = {name:i for name in names}

print(names_score)

sentence = "What is the Airspeed Velocity of a unladen Smallow?"

sentence_list = (sentence.split())

result = {word: len(word) for word in sentence_list}

print(result)
