import sys
import copy

f = open(sys.argv[1])
if len(sys.argv)==3:
    debug = sys.argv[2]
else:
    debug = False
T = int(f.readline())

output = open('magictrickoutput', 'w')
def casesolve(case):
    if debug:
        print('CASETEST' + str(case))
    guess1 = int(f.readline())
    line1 = []
    for line in range(1, 5):
        if line == guess1:
            line1 = f.readline().split()
        else:
            f.readline() 
    if debug:
        print('guess1: ' + str(guess1))
        print('line: ' + str(line1))

    guess2 = int(f.readline())
    columns = [[], [], [], []]
    line2 = []
    for line in range(0, 4):
        temp = f.readline().split()
        if line+1 == guess2:
            line2 = copy.copy(temp)
        for column in range(0, 4):
            columns[column].append(temp[column])
    # for index, column in enumerate(columns):
    #     if debug:
    #         print(guess2-1)
    #         print(line1, column, index, line2)
    #     if line1 == column and column[guess2-1] in line1:
    #         output.write('Case #{0}: {1}\n'.format(case, column[guess2-1]))
    #         return
    #     if line1[index] in line2:
    #         cheat = False
    #         bad = True
    possible = []
    for index, value in enumerate(line1):
        if value in line2:
            possible.append(value)
    if len(possible) == 0:
        output.write('Case #{0}: {1}\n'.format(case, 'Volunteer cheated!'))
        return
    elif len(possible) == 1:
        output.write('Case #{0}: {1}\n'.format(case, possible[0]))
        return
    else:
        output.write('Case #{0}: {1}\n'.format(case, 'Bad magician!'))
        return


    if debug:
        print('columns: ' + str(columns))

if debug:
    print('testcases: ' + str(T))
for t in range(T):
    casesolve(t+1)
