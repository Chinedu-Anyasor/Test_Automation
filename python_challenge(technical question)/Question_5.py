"""Rite  a  Python  program  that  checks  if  a  string  is  a palindrome,  Then  optionally  write  a  unit  test
to  check your program's correctness. """
"""A palindrome is a string that reads the same forwards and backwards."""


def is_a_palindrome(string):
    if string == string[::-1]:
        print("Is Palindrome")
    else:
        print("Not a Palindrome")


is_a_palindrome("Mama")
is_a_palindrome("rotator")
