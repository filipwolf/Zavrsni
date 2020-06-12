import sys

chromosomeNamesDict = {}
numOfContigs = 0
numOfChr = 0

inp = ""
while True:
    print("Enter chromosome name, followed by the number of contigs it contains, Q to finish")
    inp = input()
    if inp == "Q":
        break
    sep = inp.split()
    chromosomeNamesDict[sep[0]] = int(sep[1])
    numOfContigs += int(sep[1])
    numOfChr += 1
print("Enter contig length")
step = int(input())
start = 0
contigTailLen = 100000
flag = False
n = numOfContigs
densities = {}
contigs = {}
contigTails = {}
contigTailsFlags = {}
stats = {}
chromosomes = {}
contigList = [i + 1 for i in range(numOfContigs)]
chromosomeNames = []
contigRev = {}

for i in range(numOfContigs):
    contigs[i + 1] = [start, start + step, False]
    contigTailsFlags[i + 1] = [False, False]
    contigRev[i + 1] = 0
    start += step
    for j in range(numOfContigs):
        contigTails[(i + 1, j + 1)] = [0, 0, 0, 0]
        stats[(i + 1, j + 1)] = 0
        densities[j + 1] = 0

with open(sys.argv[1]) as f:
    for line in f:
        fields = line.split("\t")
        if fields[0][0] == '@':
            continue
        if not flag:
            flag = True
            for key in contigs.keys():
                contigs[key][2] = False
            for key in contigTailsFlags.keys():
                for i in range(len(contigTailsFlags[key])):
                    contigTailsFlags[key][i] = False
            for key in contigs.keys():
                if contigs[key][0] <= int(fields[3]) < contigs[key][1]:
                    index = 0
                    for key2 in chromosomeNamesDict.keys():
                        if key2 != fields[2]:
                            index += chromosomeNamesDict[key2]
                        else:
                            break
                    if contigs[key][0] <= int(fields[3]) < contigs[key][0] + contigTailLen:
                        contigTailsFlags[key + index][0] = True
                    elif contigs[key][1] - contigTailLen <= int(fields[3]) < contigs[key][1]:
                        contigTailsFlags[key + index][1] = True
                    contigs[key + index][2] = True
                    densities[key + index] += 1
                    break
        else:
            flag = False
            for key in contigs.keys():
                if contigs[key][0] <= int(fields[3]) < contigs[key][1]:
                    index = 0
                    for key2 in chromosomeNamesDict.keys():
                        if key2 != fields[2]:
                            index += chromosomeNamesDict[key2]
                        else:
                            break
                    for i in contigs.keys():
                        if contigs[i][2] and i != key + index:
                            for j in range(2):
                                if contigTailsFlags[i][j]:
                                    if contigs[key][0] <= int(fields[3]) < contigs[key][0] + contigTailLen:
                                        contigTails[(key + index, i)][0 + 2 * j] += 1
                                    elif contigs[key][1] - contigTailLen <= int(fields[3]) < contigs[key][1]:
                                        contigTails[(key + index, i)][1 + 2 * j] += 1
                            stats[(key + index, i)] += 1
                            densities[key + index] += 1
                            break
                    else:
                        continue
                    break

statsCopy = stats.copy()

for key1 in statsCopy.keys():
    for key2 in statsCopy.keys():
        if key1[0] == key2[1] and key1[1] == key2[0]:
            stats[key1] = (statsCopy[key1] + statsCopy[key2]) / (densities[key1[0]] * densities[key2[0]])
            del stats[key2]
            break

statsSorted = {k: v for k, v in sorted(stats.items(), key=lambda item: item[1])}

for key in statsSorted.keys():
    print(str(key) + ": " + str(statsSorted[key]))

while n != numOfChr:
    n -= 1
    maxn = 0
    biggestConting = ()

    for key in stats.keys():
        if stats[key] > maxn:
            maxn = stats[key]
            biggestConting = key

    del stats[biggestConting]
    contigList.remove(biggestConting[0])
    contigList.remove(biggestConting[1])
    contigListCopy = contigList.copy()

    for i in contigListCopy:
        if (biggestConting[0], i) in stats.keys():
            if (biggestConting[1], i) in stats.keys():
                stats[("newContig" + str(n), i)] = (stats[(biggestConting[0], i)] + stats[(biggestConting[1], i)]) / 2
                del stats[(biggestConting[0], i)]
                del stats[(biggestConting[1], i)]
            else:
                stats[("newContig" + str(n), i)] = (stats[(biggestConting[0], i)] + stats[(i, biggestConting[1])]) / 2
                del stats[(biggestConting[0], i)]
                del stats[(i, biggestConting[1])]
        else:
            if (biggestConting[1], i) in stats.keys():
                stats[("newContig" + str(n), i)] = (stats[(i, biggestConting[0])] + stats[(biggestConting[1], i)]) / 2
                del stats[(i, biggestConting[0])]
                del stats[(biggestConting[1], i)]
            else:
                stats[("newContig" + str(n), i)] = (stats[(i, biggestConting[0])] + stats[(i, biggestConting[1])]) / 2
                del stats[(i, biggestConting[0])]
                del stats[(i, biggestConting[1])]

    contigList.append("newContig" + str(n))
    if n == numOfContigs - 1:
        chromosomes["newContig" + str(n)] = biggestConting
    else:
        chromosomes["newContig" + str(n)] = ()
        if biggestConting[0] in chromosomes:
            chromosomes["newContig" + str(n)] += chromosomes[biggestConting[0]]
        else:
            chromosomes["newContig" + str(n)] += (biggestConting[0],)
        if biggestConting[1] in chromosomes:
            chromosomes["newContig" + str(n)] += chromosomes[biggestConting[1]]
        else:
            chromosomes["newContig" + str(n)] += (biggestConting[1],)
        if biggestConting[0] not in chromosomes and biggestConting[1] not in chromosomes:
            chromosomes["newContig" + str(n)] = biggestConting

for key in chromosomes.keys():
    print(str(key) + ": " + str(chromosomes[key]))

for key in contigTails.keys():
    print(str(key) + ": " + str(contigTails[key]))

# for key in contigRev.keys():
#     print(str(key) + ": " + str(contigRev[key]))
