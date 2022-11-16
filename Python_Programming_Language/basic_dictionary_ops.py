
"""
A dictionary is a collection of key-value pair elements. They are created ina curly bracket.
"""
animals = {
    "bird": "Parrot",
    "mammal": "Cow",
    "fish": "Titus"
}
print("dictionary", animals)

# get -> fetch a value using the specified key
bird = animals.get("bird")
print("get-1:", bird)
mammal = animals.get("mammal")
print("get-2:", mammal)

# items -> list of the dictionary key-value pair as a tuple
# tuple = (1, 2) - Content of a tuple cannot be changed
# list = [1, 2] - Content of a list can be changed
animals_items = animals.items()
print("Items:", animals_items)

# keys -> return the keys as a list
animals_keys = animals.keys()
print("Keys:", animals_keys)

# values -> return the values as a list
animals_values = animals.values()
print("Values:", animals_values)

# pop -> remove a key-value pair using the specified key
animals.pop("mammal")
print("Pop:", animals)

# update -> add more key-values pairs into a dictionary
animals.update({"mammal": "Goat", "Insect": "Ant"})
print("Update:", animals)

# popitem -> remove the last key-value pair from the dictionary
animals.popitem()
print("Popitem:", animals)

#copy -> returns a copy of a dictionary
copied_animals = animals.copy()
print("Copy:", animals)

# clear -> removes all the elements, items, key-value pair from the dictionary
animals.clear()
print("Clear:", animals)
print(copied_animals) # This will remain because we have copied the dictionary before the clear operation