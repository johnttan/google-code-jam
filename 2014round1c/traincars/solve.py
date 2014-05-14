import sys
import itertools
import copy

def check(train):
    train = ''.join(train)
    checked = {}
    current = ''
    for letter in train:
      if letter not in checked.keys():
        checked[letter] = True
        current = letter
      # if not checked[letter] and letter != current:
      #   checked[letter] = True
      #   current = letter
      elif checked[letter] and letter != current:
        return False
      elif checked[letter] and letter == current:
        pass
    return True

def solveprob(i, file):
    numcars = int(file.readline())
    cars = [str(x) for x in file.readline().split()]
    combinations = 0
    if numcars <= 8:
      for subset in itertools.permutations(cars, numcars):
        # print(subset, i)
        if check(subset):
          combinations += 1
      return combinations
    for car in cars:
      if not check(car):
        return 0

    newcars = list(cars)  
    used = []
    found = True
    while found and len(cars) > 0:
        found = False
        car = cars[-1]
        ind = cars.index(car)
        cars.pop()
        first = car[0]
        last = car[-1]
        for ind1, car1 in enumerate(cars):
            # print(car1, car)
            if ind1 not in used:
                if car1[0] == car[0]:
                  return 0
                elif car1[0] == car[-1]:
                  if i == 21:
                    print(car)
                    print(newcars)
                    print(used)
                    print(ind1)
                  if car in newcars:
                    newcars.remove(car)
                  if car1 in newcars:
                    newcars.remove(car1)
                  newcars.append(car + car1)
                  used.append(ind)
                  used.append(ind1)
                  found = True
                elif car1[-1] == car[-1]:
                  return 0
                elif car1[-1] == car[0]:
                  if car in newcars:
                    newcars.remove(car)
                  if car1 in newcars:
                    newcars.remove(car1)
                  newcars.append(car1 + car)
                  used.append(ind)
                  used.append(ind1)
                  found = True
    # print(newcars)
    for subset in itertools.permutations(newcars, len(newcars)):
      if check(subset):
        combinations += 1
    return combinations







    # print(combinations)
    # for index, car in enumerate(cars):
    #   cars[index] = ''.join(ch for ch, _ in itertools.groupby(car))
def solve():
  file = open('B-small-attempt0 (2).in')
  out = open('Attempt2', 'w')

  t = int(file.readline())
  for i in range(1, t+1):
    print('Case', i)
    result = solveprob(i, file)
    print(result)
    # if i == 11:
    #   print(result)
    #   return 0
    out.write("Case #{0}: {1}\n".format(i, result %1000000007 ))

solve()
