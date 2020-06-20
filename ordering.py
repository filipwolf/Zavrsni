from chrSep import chromosomes
from chrSep import statsSorted

finalOrdering = {}
cnt = 0

for chromosome in chromosomes.keys():
    n = len(chromosomes[chromosome])
    ordering = []
    while n != 1:
        biggestKey = ()
        biggest = 0
        if len(ordering) == 0:
            maxn = 0
            for key in statsSorted.keys():
                if statsSorted[key] > maxn and key[0] in chromosomes[chromosome] and key[1] in chromosomes[chromosome]:
                    maxn = statsSorted[key]
                    biggestKey = key
            ordering.append(biggestKey[0])
            ordering.append(biggestKey[1])
            listTuple = list(chromosomes[chromosome])
            listTuple.remove(biggestKey[0])
            listTuple.remove(biggestKey[1])
            chromosomes[chromosome] = tuple(listTuple)
        else:
            iterList = [ordering[0]] + [ordering[-1]]
            for i in ordering:
                for j in chromosomes[chromosome]:
                    if (i, j) in statsSorted.keys():
                        if statsSorted[i, j] > biggest:
                            biggest = statsSorted[i, j]
                            biggestKey = (i, j)
                    elif (j, i) in statsSorted.keys():
                        if statsSorted[j, i] > biggest:
                            biggest = statsSorted[j, i]
                            biggestKey = (j, i)
            if biggestKey[0] == iterList[0]:
                ordering.insert(0, biggestKey[1])
                listTuple = list(chromosomes[chromosome])
                listTuple.remove(biggestKey[1])
                chromosomes[chromosome] = tuple(listTuple)
            elif biggestKey[1] == iterList[0]:
                ordering.insert(0, biggestKey[0])
                listTuple = list(chromosomes[chromosome])
                listTuple.remove(biggestKey[0])
                chromosomes[chromosome] = tuple(listTuple)
            elif biggestKey[0] == iterList[1]:
                ordering.append(biggestKey[1])
                listTuple = list(chromosomes[chromosome])
                listTuple.remove(biggestKey[1])
                chromosomes[chromosome] = tuple(listTuple)
            elif biggestKey[1] == iterList[1]:
                ordering.append(biggestKey[0])
                listTuple = list(chromosomes[chromosome])
                listTuple.remove(biggestKey[0])
                chromosomes[chromosome] = tuple(listTuple)
            else:
                if biggestKey[0] in ordering:
                    index = ordering.index(biggestKey[0])
                    if (biggestKey[1], ordering[index - 1]) in statsSorted.keys():
                        if (biggestKey[1], ordering[index + 1]) in statsSorted.keys():
                            if statsSorted[(biggestKey[1], ordering[index - 1])] >\
                                    statsSorted[(biggestKey[1], ordering[index + 1])]:
                                ordering.insert(index, biggestKey[1])
                            else:
                                ordering.insert(index + 1, biggestKey[1])
                        else:
                            if statsSorted[(biggestKey[1], ordering[index - 1])] >\
                                    statsSorted[(ordering[index + 1], biggestKey[1])]:
                                ordering.insert(index, biggestKey[1])
                            else:
                                ordering.insert(biggestKey[1], index + 1)
                    else:
                        if (biggestKey[1], ordering[index + 1]) in statsSorted.keys():
                            if statsSorted[(ordering[index - 1], biggestKey[1])] >\
                                    statsSorted[(biggestKey[1], ordering[index + 1])]:
                                ordering.insert(index, biggestKey[1])
                            else:
                                ordering.insert(biggestKey[1], index + 1)
                        else:
                            if statsSorted[(ordering[index - 1], biggestKey[1])] >\
                                    statsSorted[(ordering[index + 1], biggestKey[1])]:
                                ordering.insert(index, biggestKey[1])
                            else:
                                ordering.insert(index + 1, biggestKey[1])
                    listTuple = list(chromosomes[chromosome])
                    listTuple.remove(biggestKey[1])
                    chromosomes[chromosome] = tuple(listTuple)
                else:
                    index = ordering.index(biggestKey[1])
                    if (biggestKey[0], ordering[index - 1]) in statsSorted.keys():
                        if (biggestKey[0], ordering[index + 1]) in statsSorted.keys():
                            if statsSorted[(biggestKey[0], ordering[index - 1])] >\
                                    statsSorted[(biggestKey[0], ordering[index + 1])]:
                                ordering.insert(index, biggestKey[0])
                            else:
                                ordering.insert(index + 1, biggestKey[0])
                        else:
                            if statsSorted[(biggestKey[0], ordering[index - 1])] >\
                                    statsSorted[(ordering[index + 1], biggestKey[0])]:
                                ordering.insert(index, biggestKey[0])
                            else:
                                ordering.insert(biggestKey[0], index + 1)
                    else:
                        if (biggestKey[0], ordering[index + 1]) in statsSorted.keys():
                            if statsSorted[(ordering[index - 1], biggestKey[0])] >\
                                    statsSorted[(biggestKey[0], ordering[index + 1])]:
                                ordering.insert(index, biggestKey[0])
                            else:
                                ordering.insert(biggestKey[0], index + 1)
                        else:
                            if statsSorted[(ordering[index - 1], biggestKey[0])] >\
                                    statsSorted[(ordering[index + 1], biggestKey[0])]:
                                ordering.insert(index, biggestKey[0])
                            else:
                                ordering.insert(index + 1, biggestKey[0])
                    listTuple = list(chromosomes[chromosome])
                    listTuple.remove(biggestKey[0])
                    chromosomes[chromosome] = tuple(listTuple)
        n -= 1
    finalOrdering[cnt] = ordering.copy()
    cnt += 1

for key in finalOrdering.keys():
    print(str(key) + ": " + str(finalOrdering[key]))
