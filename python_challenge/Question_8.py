
"""Create a program that prints out the even numbers in an array. Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9,
91, 19,401, 0 ] """


def print_even(num):
    even_num = []
    for i in num:
        if i % 2 == 0:
            print(i)


print_even([1, 2, 3, 4, 5, 6])
print_even([34, 2, 9, 91, 19, 401, 0])