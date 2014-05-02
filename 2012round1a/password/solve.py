import sys

file = open('test')
out = open('passwordoutput', 'w')
for tc in xrange(1, int(file.readline())+1):
  A, B = [int(w) for w in file.readline().split()]
  p = [float(w) for w in file.readline().split()]
  best, x = B + 2.0, 1
  for i in xrange(A):
    x *= p[i]
    print(best, (B - i) + (A - i - 1) + (B + 1) * (1 - x))
    best = min(best, (B - i) + (A - i - 1) + (B + 1) * (1 - x))
  print 'Case #%d: %f' % (tc, best)
  out.write('Case #%d: %f\n' % (tc, best))