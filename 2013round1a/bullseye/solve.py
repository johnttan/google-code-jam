"""
Bullseye
Small: Solved
Large: Unsolved
"""

class Classcasesolver(object):
    def casesolve(self, case):
        paint = case.case['paint']
        radius = case.case['radius']
        r = radius + 1
        rings = 0

        while paint >= 0:
            paint -= (2*r - 1)
            if paint >= 0:
                rings += 1
            r += 2
            # print(rings, paint, r, "Case:", case.casenumber)
        return rings

    def casesolvelarge(self, case):
        paint = case.case['paint']
        radius = case.case['radius']
        r = radius
        rings = 0

        low, high = 1, paint

        while low<=high:
            mid = int((low + high) / 2)

            if mid*(2*r+2*mid-1) > paint:
                high = mid -1
            else:
                low, rings = mid + 1, mid

        return rings


