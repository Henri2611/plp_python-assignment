my_list = []

# Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# Inserting an element at a specific position
my_list.insert(1, 15)
print(my_list)
# Adding another list to the existing list
another_list = [50, 60, 70]
my_list.extend(another_list)
print(my_list)

# Removing an element from the list
my_list.pop()
print(my_list)


# sorting the list in ascending order 
my_list.sort()
print(my_list)


print(my_list.index(30))  # Finding the index of an element