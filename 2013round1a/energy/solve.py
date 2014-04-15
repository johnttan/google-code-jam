"""
Problem A
Small: Solved
Large: Unsolved
"""
import bisect

class Classcasesolver(object):
    def casesolve(self, case):
        casedata = case.case
        activities = casedata['activities']
        maxgain = 0
        energy = casedata['energy']
        maxenergy = int(energy)
        regain = casedata['regain']

        if casedata["numberactivities"] == 1:
            return energy * activities[0]

        for index, act in enumerate(activities):
            energy += regain
            if energy > maxenergy:
                energy = maxenergy
            try:
                nextgreater = next((x for x, y in enumerate(activities) if y > act and x > index))
            except StopIteration:
                nextgreater = False
            finally:
                pass

            if nextgreater:
                potential = regain * (nextgreater - index) + energy
                # print(potential, "potential")
                # print(activities[nextgreater], "nextgreateract")
                # print(nextgreater, "nextgreaterindex")
                # print(index, "index")
                if potential > maxenergy:
                    if potential - maxenergy > maxenergy:
                        maxgain += maxenergy * act
                        energy = 0
                    else:
                        energy -= potential - maxenergy
                        maxgain += (potential - maxenergy)*act
            else:
                maxgain += energy * act
                energy = 0

        return maxgain




