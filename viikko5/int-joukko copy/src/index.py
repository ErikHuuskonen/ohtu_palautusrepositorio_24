import unittest
from int_joukko import IntJoukko

def create_and_populate_joukko():
    joukko = IntJoukko()
    elements = [1, 2, 3, 2]
    for element in elements:
        joukko.lisaa(element)
    return joukko

def main():
    joukko = create_and_populate_joukko()
    print(joukko.to_int_list())

if __name__ == "__main__":
    main()
