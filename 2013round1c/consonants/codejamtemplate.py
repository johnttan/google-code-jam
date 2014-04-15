from helperclasses import FileLoader
import os
from solve import Classcasesolver

config = {
    "name": os.getcwd().split(os.sep)[-1],
    "casefilepath": "tests/A-large-practice.in",
    # "casefilepath": "tests/A-small-practice.in",
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
    line = file.readline().split()
    d = {}
    d["name"] = line[0]
    d["n"] = int(line[1])

    return d
############################Loads case################################

#Initializes case solving class.
#Classcasesolver.casesolve(case) method takes case and calls necessary functions to solve it. Returns solution.
casesolver = Classcasesolver()
files.loadcustom(caseloader)
files.solve(casesolver.casesolve, True)
#Case number input is 1 less than real case number. 0 indexed deque.
# files.solvesingle(40, casesolver, True)

