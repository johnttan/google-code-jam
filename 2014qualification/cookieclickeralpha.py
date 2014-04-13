import sys
import copy

f = open(sys.argv[1])
if len(sys.argv)==3:
    debug = sys.argv[2]
else:
    debug = False
T = int(f.readline())

output = open(sys.argv[0][:-3] + 'output', 'w')

def casesolve(case, c, f, x):
    if debug:
        print(c, f, x)
    t = 0
    k = 0
    h = 0
    r = 2

    while True:
        if k >= x:
            if debug and case == 19:
                print('c:{0} k:{1} r:{2} t:{3} already reached'.format(c, k, r, t))
            return t
        elif (x-k)/r > (x-k+c)/(r+f) and k >= c:
            k = k - c
            r = r + f
            if debug and case == 19:
                print('c:{0} k:{1} r:{2} t:{3}bought house'.format(c, k, r, t))

        elif k < c and k < x and (x-k)/r < (x-k+c)/(r+f):
            return (x-k)/r

        elif k < c and k < x:
            k = c
            t = t + k/(r)
            if debug and case == 19:
                print('c:{0} k:{1} r:{2} t:{3} advanced'.format(c, k, r, t))
        elif (x-k)/r <= (x-k+c)/(r+f) and k >= c:
            if debug and case == 19:
                print('c:{0} k:{1} r:{2} t:{3} can reach without buying'.format(c, k, r, t))
            return (x-k)/r + t

if debug:
    print('testcases: ' + str(T))
for t in range(T):
    print(t+1)
    values = f.readline().split()
    cased = casesolve(t+1, float(values[0]), float(values[1]), float(values[2]))
    out = "{:.7f}".format(cased) + '\n'
    output.write('Case #{0}: {1}'.format(t+1, out))
    if debug:
        print('Case #{0}: {1}'.format(t+1, out))