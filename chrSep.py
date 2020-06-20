import sys

print("Enter contig length")
step = int(input())
numOfChr = 2
contigTailLen = 100000
flag = False
densities = {}
contigs = {}
contigTails = {}
contigTailsFlags = {}
stats = {}
chromosomes = {}
contigList = []

with open(sys.argv[1]) as f:
    for line in f:
        fields = line.split("\t")
        if line.startswith("@SQ"):
            split1 = fields[1].split(":")
            contigs[split1[1]] = False
            contigList.append(split1[1])
            contigTailsFlags[split1[1]] = [False, False]
            densities[split1[1]] = 0
            continue
        if line.startswith("@PG"):
            numOfContigs = len(contigList)
            n = numOfContigs
            for i in contigs.keys():
                for j in contigs.keys():
                    contigTails[(i, j)] = [0, 0, 0, 0]
                    stats[(i, j)] = 0
            continue
        if not flag:
            flag = True
            for key in contigs.keys():
                contigs[key] = False
            for key in contigTailsFlags.keys():
                for i in range(len(contigTailsFlags[key])):
                    contigTailsFlags[key][i] = False
            for key in contigs.keys():
                if fields[2] == key:
                    if 0 <= int(fields[3]) < contigTailLen:
                        contigTailsFlags[key][0] = True
                    elif step - contigTailLen <= int(fields[3]) < step:
                        contigTailsFlags[key][1] = True
                    contigs[key] = True
                    densities[key] += 1
                    break
        else:
            flag = False
            for key in contigs.keys():
                if fields[2] == key:
                    for i in contigs.keys():
                        if contigs[i]:
                            for j in range(2):
                                if contigTailsFlags[i][j]:
                                    if 0 <= int(fields[3]) < contigTailLen:
                                        contigTails[(key, i)][0 + 2 * j] += 1
                                    elif step - contigTailLen <= int(fields[3]) < step:
                                        contigTails[(key, i)][1 + 2 * j] += 1
                            stats[(key, i)] += 1
                            densities[key] += 1
                            break
                    else:
                        continue
                    break

statsCopy = stats.copy()

for key in statsCopy.keys():
    if statsCopy[key] == 0:
        del stats[key]

densitiesCopy = densities.copy()

for key in densitiesCopy.keys():
    if densities[key] == 0:
        del densities[key]
        contigList.remove(key)
        n -= 1

statsCopy = stats.copy()

for key1 in statsCopy.keys():
    for key2 in statsCopy.keys():
        if key1[0] == key2[1] and key1[1] == key2[0] and densities[key1[0]] != 0 and densities[key2[0]] != 0:
            stats[key1] = (statsCopy[key1] + statsCopy[key2]) / (densities[key1[0]] * densities[key2[0]])
            del stats[key2]
            break

statsSorted = {k: v for k, v in sorted(stats.items(), key=lambda item: item[1])}

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
    chromosomes["newContig" + str(n)] = ()
    if biggestConting[0] in chromosomes:
        chromosomes["newContig" + str(n)] += chromosomes[biggestConting[0]]
        del chromosomes[biggestConting[0]]
    else:
        chromosomes["newContig" + str(n)] += (biggestConting[0],)
    if biggestConting[1] in chromosomes:
        chromosomes["newContig" + str(n)] += chromosomes[biggestConting[1]]
        del chromosomes[biggestConting[1]]
    else:
        chromosomes["newContig" + str(n)] += (biggestConting[1],)

if len(sys.argv) == 3 and sys.argv[2] == "-v":
    for key in statsSorted.keys():
        print(str(key) + ": " + str(statsSorted[key]))
    for key in contigTails.keys():
        print(str(key) + ": " + str(contigTails[key]))

for key in chromosomes.keys():
    print(str(key) + ": " + str(chromosomes[key]))
