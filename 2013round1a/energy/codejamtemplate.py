from helperclasses import FileLoader
import os
from solve import Classcasesolver

config = {
    "name": os.getcwd().split(os.sep)[-1],
    "casefilepath": "tests/B-large-practice.in",
    # "casefilepath": "tests/B-small-practice.in",
    # "casefilepath": "tests/initial",
    "split": False
}
# FileLoader attributes:
#     self.file
#     self.casesnumber
#     self.casesdeque

files = FileLoader(config["name"], config["casefilepath"])



############################Loads case################################
def caseloader(file):
    line1 = [int(x) for x in file.readline().split()]
    line2 = [int(x) for x in file.readline().split()]
    dictionary = {}
    dictionary['energy'] = line1[0]
    dictionary['regain'] = line1[1]
    dictionary['numberactivities'] = line1[2]
    dictionary['activities'] = line2

    return dictionary
############################Loads case################################

#Initializes case solving class.
#Classcasesolver.casesolve(case) method takes case and calls necessary functions to solve it. Returns solution.
casesolver = Classcasesolver()
files.loadcustom(caseloader)
# files.solve(casesolver.casesolve, True)
#Case number input is 1 less than real case number. 0 indexed deque.
files.solvesingle(36, casesolver.casesolve, True)

