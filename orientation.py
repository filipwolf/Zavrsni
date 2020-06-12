from chrSep import contigTails
from ordering import finalOrdering

for key in finalOrdering.keys():
    # listBiggest = [0, 0, 0, 0]
    # for i in range(len(finalOrdering[key])):
    #     for j in range(len(finalOrdering[key])):
    #         if i == j + 1:
    #             for k in range(4):
    #                 if k == 1 or k == 2:
    #                     if contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
    #                             contigTails[finalOrdering[key][j], finalOrdering[key][i]][3 - k] > listBiggest[k]:
    #                         listBiggest[k] = contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
    #                                          contigTails[finalOrdering[key][j], finalOrdering[key][i]][3 - k]
    #                 else:
    #                     if contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
    #                             contigTails[finalOrdering[key][j], finalOrdering[key][i]][k] > listBiggest[k]:
    #                         listBiggest[k] = contigTails[finalOrdering[key][i], finalOrdering[key][j]][k] + \
    #                                          contigTails[finalOrdering[key][j], finalOrdering[key][i]][k]
    # print(listBiggest)
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
    print(suspect)
    reverse = []
    for i in suspect:
        for j in suspect:
            if i[0] == j[1]:
                reverse.append(i[0])
            if j[0] == i[1]:
                reverse.append(j[0])
    print(set(reverse))





# first = 0
# flag = True
# for key1 in finalOrdering2.keys():
#     for key2 in finalOrdering2[key1]:
#         if finalOrdering2[key1][key2] == 0:
#             first = key2
#
#
# biggest = 0
# for key in contigTails.keys():
#     for i in range(len(contigTails[key])):
#         biggest = max(biggest, contigTails[key][i])
#
# contigTailsCopy = contigTails.copy()
#
# for key1 in contigTailsCopy.keys():
#     for key2 in contigTailsCopy.keys():
#         if key1[0] == key2[1] and key1[1] == key2[0]:
#             for i in range(4):
#                 contigTails[key1][i] = contigTailsCopy[key1][i] + contigTailsCopy[key2][i]
#             del contigTails[key2]
#             break
#
# for key in contigTails.keys():
#     print(print(str(key) + ": " + str(contigTails[key])))

# for key1 in finalOrdering2.keys():
#     cnt = len(finalOrdering2[key1])
#     while cnt != 0:
#         sumList = [0, 0, 0, 0]
#         maxn = 0
#         position = -1
#         if flag:
#             flag = False
#             for item in finalOrdering2[key1].items():
#                 if item[1] == first:
#                     for i in range(len(contigTails[(first, finalOrdering2[key1][item[0]])])):
#                         for j in range(len(contigTails[(finalOrdering2[key1][item[0]], first)])):
#                             if i == j:
#                                 sumList[i] = contigTails[(first, finalOrdering2[key1][item[0]])][i] + contigTails[(finalOrdering2[key1][item[0]], first)][i]
#             for i in range(len(sumList)):
#                 if sumList[i] > maxn:
#                     maxn = sumList[i]
#                     position = i
#             if maxn >= biggest * 0.1 and position != - 1:
#                 if position == 1 or position == 2:
#                     print("nema okretanja")
#                 else:
#                     print("okrecem")
#
#

















# for key1 in finalOrdering2.keys():
#     for key2 in finalOrdering2[key1]:
#         if finalOrdering2[key1][key2] == 0:
#             continue
#         maxn = 0
#         position = -1
#         sumList = [0, 0, 0, 0]
#         if (key2, finalOrdering2[key1][key2]) or (finalOrdering2[key1][key2], key2) in contigTails.keys():
#             for i in range(len(contigTails[(key2, finalOrdering2[key1][key2])])):
#                 for j in range(len(contigTails[(finalOrdering2[key1][key2], key2)])):
#                     if i == j:
#                         sumList[i] = contigTails[(key2, finalOrdering2[key1][key2])][i] + contigTails[(finalOrdering2[key1][key2], key2)][i]
#         for i in range(len(sumList)):
#             if sumList[i] > maxn:
#                 maxn = sumList[i]
#                 position = i
#         if position != -1:
#             if position == 1 or position == 2:
#                 print(key2)
#                 print("nema okretanja")
#             else:
#                 print("okrecem")
#                 contigTails[(key2, finalOrdering2[key1][key2])][position].reverse()
#                 contigTails[(finalOrdering2[key1][key2], key2)][position].reverse()





                # if contigTails[(key2, finalOrdering2[key1][key2])][i] > maxn:
                #     maxn = contigTails[(key2, finalOrdering2[key1][key2])][i]
                #     position = i
                # if (i == 1 or i == 2) and contigTails[(key2, finalOrdering2[key1][key2])][i] != 0:
                #     print("nema okretanja")
                #     #print(contigTails[(key2, finalOrdering2[key1][key2])])
                # elif (i == 0 or i == 3) and contigTails[(key2, finalOrdering2[key1][key2])][i] != 0:
                #     print("fuj")
                #     print(contigTails[(key2, finalOrdering2[key1][key2])])
            # for i in range(len(contigTails[(finalOrdering2[key1][key2], key2)])):
            #     if i == 1 or i == 2 and contigTails[(finalOrdering2[key1][key2], key2)][i] != 0:
            #         print("niec")
            #         print(contigTails[(finalOrdering2[key1][key2], key2)])
            #     elif (i == 0 or i == 3) and contigTails[(finalOrdering2[key1][key2], key2)][i] != 0:
            #         print("fuj")
            #         print(contigTails[(key2, finalOrdering2[key1][key2])])
