"""
Writing  a  well-documented  code  creates  a  function  that calculates simple interest.
"""


def simple_interest(p, t, r):
    """ P = Principal; T = Time; R = Rate"""
    Simple_Interest = (p * t * r) / 100
    print(Simple_Interest)


simple_interest(25, 5, 3)
