
name = "  testify is good  "

# len -> get the size of string
size = len(name)
print("len=", size)

# upper -> convert a string to upper case
upper_value = name.upper()
print("Upper=", upper_value)

# lower -> convert a string to lower case
lower_value = name.lower()
print("Lower=", lower_value)

# capitalize -> convert the first letter to upper case
capitalized_value = name.capitalize()
print("Capitalize=", capitalized_value)

# count -> count the number of value in a string
count_value = name.count('t')
print("Count=", count_value)

# find -> get the position of a value in the string, if the value is not in the string it does not throws an exception
for_position = name.find("i")
print("Find=", for_position)

# index -> get the position of a value in the string, if the value is not in the string it throws an exception
for_index = name.index("t")
print("Index=", for_index)

# strip -> removes excess white space at the beginning and end of a string
stripped_name = name.strip()
print("Stripped=", stripped_name)

# rstrip -> right trim a string, removes excess  white space at the end of string
rstriped_name = name.rstrip()
print("rstriped=", rstriped_name)

# lstrip -> left trim a string, removes excess  white space at the beginning of string
lstriped_name = name.lstrip()
print("lstripped=", lstriped_name)

# split -> it splits a string to an array using the specified value
splited_name = name.split("is")
print("splited=", splited_name)

# format -> format the specified value of a string. formatting can be done using name, index or curly bracket(unindexed)
# named format

unformatted_one = "My name is {name}, I am an {occupation}"
formatted_one = unformatted_one.format(name="Jide", occupation="Automation Engr")
print(formatted_one)

# index format
unformatted_index = "My name is {0}, I am a {1}"
formatted_index = unformatted_index.format("Sean", "Student")
print(formatted_index)

# unindexed format
unformatted_index = "My name is {}, I am a {}"
formatted_index = unformatted_index.format("Sean", "Student")
print(formatted_index)