import sys
from pprint import pprint

# Unsuccessful attempt
# Perhaps depth first search graph problem?
def solve():
  file = open('B-small-practice.in')
  out = open('binarytreeout', 'w')
  debug = open('debug', 'w')
  for test in xrange(1, int(file.readline())+1):
    N = int(file.readline())
    tree = {}
    freeleaves = []
    trischild = []
    tris = []
    bis = []
    multis = []
    for node in range(1, N+1):
      tree[node] = []
    for node in range(1, N):
      a, b = [int(x) for x in file.readline().split()]
      tree[a].append(b)
      tree[b].append(a)
    for node in range(1, N+1):
      if len(tree[node]) == 3:
        trischild = trischild + tree[node]
      if len(tree[node]) > 3:
        multis.append(node)
    # print(trischild, 'trischild')
    for node, connect in tree.iteritems():
      if len(connect) == 1:
        freeleaves.append(node)
      elif len(connect) == 3:
        tris.append(node)
      elif len(connect) == 2:
        bis.append(node)

    solved = False
    deletes = 0
    deleted = []

    newleaves = []
    leavestocheck = list(freeleaves)
    leaveschecked = []
    iterations = 0
    if test == debugtest:
      debug.write(str(tree) + 'tree' + '\n')
      pprint(tree)
    while len(leavestocheck) > 0:
      if test == debugtest:
        debug.write(str(leavestocheck) + 'leavestocheck' + '\n')
        debug.write(str(deleted) + 'deleted' + '\n')
        debug.write(str(newleaves) + 'newleaves' + '\n')
        debug.write(str(freeleaves) + 'freeleaves' + '\n')
      iterations += 1
      # print(leavestocheck)
      for leaf in list(leavestocheck):
        leavestocheck.remove(leaf)
        # print(leaf, leavestocheck)
        # print(leaf, 'treeleaf0')
        # print(freeleaves, newleaves, 'newleaves')
        # if tree[leaf][0] in newleaves:
        #   print('deleted' + str(leaf))
        #   deletes += 1
        #   deleted.append(leaf)
        #   if leaf in freeleaves:
        #     freeleaves.remove(leaf)

        #   else:
        #     newleaves.remove(leaf)

        if tree[leaf][0] in bis:
          for child in tree[tree[leaf][0]]:
            if child != leaf and child in bis and child not in newleaves:
              deletes += 1
              deleted.append(leaf)
              # print('2nddeleted' + str(leaf))
              # print(freeleaves, leaf, '49')
              if leaf in freeleaves:
                freeleaves.remove(leaf)

              else:
                newleaves.remove(leaf)
              newleaves.append(tree[leaf][0])
              tree[tree[leaf][0]].remove(leaf)
              leavestocheck.append(tree[leaf][0])
        elif tree[leaf][0] in multis:
          if leaf in freeleaves:
            freeleaves.remove(leaf)

          else:
            newleaves.remove(leaf)

          deletes += 1
          deleted.append(leaf)
          tree[tree[leaf][0]].remove(leaf)
          if len(tree[tree[leaf][0]]) == 3:
            multis.remove(tree[leaf][0])
            tris.append(tree[leaf][0])
    # print(deletes)
    # print('Case #{0}: {1}\n'.format(test, deletes))

    leavestocheck = newleaves + freeleaves
    if test == debugtest:
        debug.write('pruning' + '\n')
    while len(leavestocheck) > 0:
      if test == debugtest:
        debug.write(str(leavestocheck) + 'LEAVEStocheck' + '\n')
        debug.write(str(deleted) + 'deleted' + '\n')
        debug.write(str(newleaves) + 'newleaves' + '\n')
        debug.write(str(freeleaves) + 'freeleaves' + '\n')
      for leaf in list(leavestocheck):
        if test == debugtest:
          debug.write(str(leaf) + 'pruneleaf' + '\n')
          debug.write(str(tree[tree[leaf][0]]) + 'parent' + '\n')
          print(leaf)
        leavestocheck.remove(leaf)
        if len(tree[tree[leaf][0]]) ==2 :
          for leaf1 in list(leavestocheck):
            if test == debugtest:
              debug.write(str(leaf1) + 'otherleaf' + '\n')
              print(leaf1, leaf, freeleaves, newleaves)
            if len(tree[tree[leaf1][0]]) ==2 and tree[leaf1][0] != tree[leaf][0]:
              deletes += 1
              if test == debugtest:
                debug.write(str(newleaves) + 'newleavesdelete' + '\n')
                debug.write(str(freeleaves) + 'freeleavesdelete' + '\n')
                debug.write(str(leaf) + 'deleteleaf' + '\n')
              if leaf in newleaves:
                newleaves.remove(leaf)
              elif leaf in freeleaves:
                freeleaves.remove(leaf)
              if leaf not in deleted:
                deleted.append(leaf)
                tree[tree[leaf][0]].remove(leaf)
                newleaves.append(tree[leaf][0])
                leavestocheck.append(tree[leaf][0])
                if test == debugtest:
                  print(newleaves, 'newleaves')
                  print(leavestocheck, 'leavestocheck')


    out.write('Case #{0}: {1}\n'.format(test, len(deleted)))




    # print(tree)
    # print(freeleaves)

debugtest = 3
solve()