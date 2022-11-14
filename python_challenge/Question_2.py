""" Create  a  function  that  calculates  the  power  of  a  number.
Then  write  a unit  test  to  check  the  correctness  of  the
function.
"""


def exponent(num, exp):
    result = 0
    for i in range(exp):
        result *= num
    return result


print(pow(5, 5))