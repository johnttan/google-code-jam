from helperclasses import FileLoader
import os
from solve import Classcasesolver

config = {
    "name": os.getcwd().split(os.sep)[-1],
    # "casefilepath": "tests/A-small-practice.in",
    # "casefilepath": "tests/initial",
    "casefilepath": "tests/A-large-practice.in",
    "split": False
}
# FileLoader attributes:
#     self.file
#     self.casesnumber
#     self.casesdeque

files = FileLoader(config["name"], config["casefilepath"])



############################Loads case################################
#Return case dictionary to be stored in _Case object.
def caseloader(file):
    line = [int(x) for x in file.readline().split()]
    dictionary = {}
    dictionary['radius'] = line[0]
    dictionary['paint'] = line[1]
    return dictionary
############################Loads case################################

#Initializes case solving class.
#Classcasesolver.casesolve(case) method takes case and calls necessary functions to solve it. Returns solution.
casesolver = Classcasesolver()
files.loadcustom(caseloader)
# files.solve(casesolver.casesolve)

#Large input solver
files.solve(casesolver.casesolvelarge)


#Case number input is 1 less than real case number. 0 indexed deque.
# files.solvesingle(1, casesolver.casesolve, True)

