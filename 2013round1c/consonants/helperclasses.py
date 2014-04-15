import sys
from collections import defaultdict, deque
from pprint import pprint

class _Case(object):
    def __init__(self, case, casenumber, split=False):
        self.casenumber = casenumber
        self.case = case 
        self.split = split

    def printcase(self, caseitself=True):
        print("Case: ", self.casenumber)
        if caseitself:
            pprint(self.case)

"""
Primary Class. Import FileLoader
Args: problemname, casefile=False, split=False, debug=False
                                                debug is dictionary

methods:
load: default loadcases
loadcustom: pass in casefunction(file)
solve: pass in casesolver(case)

FileLoader.casesdeque is deque of _Case objects.
_Case.case is dictionary of case with custom keys.

FileLoader attributes:
    self.file
    self.casesnumber
    self.casesdeque

"""
class FileLoader(object):
    def __init__(self, problemname, casefile=False, split=False, debug=False):
        self.file = open(casefile or sys.argv[1])
        self.casesnumber = int(self.file.readline())
        self.debug = debug
        self.problemname = problemname or sys.argv[0][:-3]
        self.output = open("tests/{0}output{1}".format(self.problemname, casefile[6:-3]), 'w')
        self.casesdeque = deque()
        self.split = split

    def load(self, *args):
        for casen in range(self.casesnumber):
            casedict = {}
            for key in args:
                num = self.file.readline()
                if self.split:
                    num = num.split()
                casedict[key] = num
            self.casesdeque.append(_Case(casedict, casen, self.split))
            if self.debug and self.debug['loadcases']:
                self.casesdeque[casen].printcase()

    def loadcustom(self, casefunction):
        for casen in range(self.casesnumber):
            self.casesdeque.append(_Case(casefunction(self.file), casen))


    def checkvariables(self):
        pprint(self.__dict__)

    def solve(self, casesolver, printed=False):
        for ind, case in enumerate(self.casesdeque):
            solved = casesolver(case)
            self.output.write("Case #{0}: {1}\n".format(ind+1, solved))
            if printed:
                print("Case #{0}: {1}\n".format(ind+1, solved))

    def solvesingle(self, casenumber, casesolver, printed=False):
        solvedsingle = casesolver(self.casesdeque[casenumber])
        if printed:
            print(solvedsingle)
        return solvedsingle

"""
"""

debugconfig = {
    'fileloaderinit': True,
    'loadcases': False
}

def caseloadingtest(file):
    casedict = {}
    args = ['blocksize', 'naomi', 'ken']
    for key in args:
        num = file.readline()
        num = [float(x) for x in num.split()]
        casedict[key] = num
    return casedict

def casesolvertest(case):
    return case.case

if __name__ == "__main__":
    testfile = FileLoader('magictrick', 'tests/D-large.in', split=True, debug=False)
    testfile.loadcustom(caseloadingtest)
    testfile.solve(casesolvertest)
    # testfile.checkvariables()
    # print(testfile.casesdeque.pop().case)





