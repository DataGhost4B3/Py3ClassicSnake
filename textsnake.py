bodylist = [(0,-12),(0,-11),(0,-10),(0,-9),(0,-8),(0,-7),(0,-6),(0,-5), (0,-4), (0,-3), (0,-2), (0, -1), (0,0)]

# key = 8

testInputs = [8, 8, 8, 8, 4, 4, 4, 4, 6, 6, 6, 6, 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]


def mvsnake(ikey: int, sbody: list):
    try:
        prevunit = sbody[-2]
    except IndexError:
        prevunit = sbody[-1]
    if ikey == 8:
        if prevunit != (sbody[-1][0], sbody[-1][1] + 1):
            sbody.append((sbody[-1][0], sbody[-1][1] + 1))
            lastunit=sbody.pop(0)
    if ikey == 2:
        if prevunit != (sbody[-1][0], sbody[-1][1] - 1):
            sbody.append((sbody[-1][0], sbody[-1][1] - 1))
            lastunit=sbody.pop(0)
    if ikey == 6:
        if prevunit != (sbody[-1][0] + 1, sbody[-1][1]):
            sbody.append((sbody[-1][0] + 1, sbody[-1][1]))
            lastunit=sbody.pop(0)
    if ikey == 4:
        if prevunit != (sbody[-1][0] - 1, sbody[-1][1]):
            sbody.append((sbody[-1][0] - 1, sbody[-1][1]))
            lastunit=sbody.pop(0)
    try:                    #in case lastunit does not instantiate because of opposite turn.
        return lastunit     #should be prevented while implementing in game
    except UnboundLocalError:
        return sbody[0]


for iput in testInputs:
    lu = mvsnake(iput, bodylist)
    print(bodylist,' ', lu)

#print(bodylist)