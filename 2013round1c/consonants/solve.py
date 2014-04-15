"""
Problem A
Small: Solved
Large: Unsolved
"""
from itertools import combinations

class Classcasesolver(object):
    def __init__(self):
        self.vowels = ["a", "e", "i", "o", "u"]
    def substrings(self, name, length):
        namelength = len(name)

        for low, high in combinations(range(namelength+1), 2):
            if high-low >= length:
                yield name[low:high]

    def checkn(self, substring, n):
        consec = 0
        # print(substring)
        for letter in substring:
            # print(letter)
            if letter not in self.vowels:
                # print('consonant')
                consec += 1
                if consec >= n:
                    return True
            else:
                consec = 0
        # print(consec)
        return True if consec >= n else False

    def casesolve(self, case):
        dcase = case.case
        name, n = dcase["name"], dcase["n"]
        nvalue = 0
        for substring in self.substrings(name, n):
            ntrue = self.checkn(substring, n)
            if ntrue:
                nvalue += 1

        return nvalue


