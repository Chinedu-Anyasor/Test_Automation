
# List stores multiple items ina single variable. List items are created in a sequence bracket. Python list is iterable.

languages = ["python", "java", "C#"]

# append -> add a new item at the end of the list
languages.append("javascript")
print("append:", languages)

#insert -> add a new item at any position in the list
languages.insert(0, 'C')
languages.insert(2, "Kotlin")
print("insert:", languages)

# pop -> remove an item from the specified position. If index is not specified, pop will remove last item on the list
languages.pop(0)
print("pop-0:", languages)
languages.pop()
print("pop:", languages)

# remove -> remove an item by value
languages.remove("Kotlin")
print("remove:", languages)

# count -> to return the number of occurence of items in a list
count_java = languages.count("java")
#print(languages)
print("count:", count_java)

# len -> to count the number of items in a list
length = len(languages)
print("len:", length)

# clear -> deletes all the items in a list
languages.clear()
print("clear:", languages, length)


languages = ["python", "java", "C#"]

#copy -> return a copy of the list
languages_copy = languages.copy()
print("copy:", languages_copy)

# reverse -> reverses the order of the items in the list
before_reverse = languages.copy()
after_reverse = languages.reverse()
print("before reverse:", before_reverse, "after reverse:", languages)


languages = ["python", "java", "C#", "Kotlin", "php"]

#sort -> sort the items inthe list by ascending or descending order
languages.sort()
print("sort-asc:", languages)
languages.sort(reverse=True)
print("sort-desc:", languages)

# extend -> add the content of the specified list to our current list
languages.extend(["visual basic", "sql", "powershell"])
print("extend:", languages)