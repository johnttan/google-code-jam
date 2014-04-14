import sys
from collections import defaultdict, deque
from pprint import pprint

class _Case(object):
    def __init__(self, case, casenumber, split=False):
        self.casenumber = casenumber
        self.case = case 
        self.split = split

    def printcase(self):
        print("Case: ", self.casenumber)
        pprint(self.case)

"""
Primary Class. Import FileLoader
Args: problemname, casefile=False, split=False, debug=False
                                                debug is dictionary

methods:
loadcases: default loadcases
loadcustomcases: pass in casefunction(file)
solvecases: pass in casesolver(case)

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

    def loadcases(self, *args):
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

    def loadcustomcases(self, casefunction):
        for casen in range(self.casesnumber):
            self.casesdeque.append(_Case(casefunction(self.file), casen))


    def checkvariables(self):
        pprint(self.__dict__)

    def solvecases(self, casesolver):
        for ind, case in enumerate(self.casesdeque):
            self.output.write("Case #{0}: {1}\n".format(ind+1, casesolver(case))) 

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
    testfile.loadcustomcases(caseloadingtest)
    testfile.solvecases(casesolvertest)
    # testfile.checkvariables()
    # print(testfile.casesdeque.pop().case)





