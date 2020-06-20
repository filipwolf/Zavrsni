from chrSep import contigTails
from ordering import finalOrdering
import sys

for key in finalOrdering.keys():
    suspect = []
    for i in range(len(finalOrdering[key])):
        for j in range(len(finalOrdering[key])):
            if i == j + 1:
                value1 = 0
                value2 = 0
                value3 = 0
                for k in range(4):
                    if (k == 1 or k == 2) and contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
                            contigTails[finalOrdering[key][j], finalOrdering[key][i]][3 - k] > value1:
                        value1 = contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
                                 contigTails[finalOrdering[key][j], finalOrdering[key][i]][3 - k]
                    elif k == 0:
                        value2 = contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
                                 contigTails[finalOrdering[key][j], finalOrdering[key][i]][k]
                    else:
                        value3 = contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
                                 contigTails[finalOrdering[key][j], finalOrdering[key][i]][k]
                if value1 > 0 and value2 / value1 > 0.05:
                    suspect.append((finalOrdering[key][i], finalOrdering[key][j]))
                    continue
                if value1 > 0 and value3 / value1 > 0.05:
                    suspect.append((finalOrdering[key][i], finalOrdering[key][j]))
    if len(sys.argv) == 3 and sys.argv[2] == "-v":
        print(suspect)
    reverse = []
    for i in suspect:
        for j in suspect:
            if i[0] == j[1]:
                reverse.append(i[0])
            if j[0] == i[1]:
                reverse.append(j[0])
    print(set(reverse))
