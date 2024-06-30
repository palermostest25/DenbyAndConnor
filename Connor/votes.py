import time
import random

with open(f'votes.txt', 'r') as file:
    # Read lines from the file into a list
    votes = file.readlines()
    file.seek(0)
    numofcand = file.readline().strip()

numofcand = int(numofcand)
numstoexclude = []
print(numofcand)
loop = 1
votes.pop(0)
print(votes)
print(len(votes))
for loop in range(len(votes)):
    vote = votes[loop]
    vote = vote.strip()
    vote = vote.split(',')
    vote.append('end')
    vote.append(2)
    votes[loop] = vote
    for loop1 in range(len(vote) - 2):
        vote[loop1] = int(vote[loop1])
    votes[loop] = vote
    print(vote)
    loop += 1
print(votes)
firstlist = []
firstnums = ['ctrl']
for loop2 in range(len(votes)):
    firstlist.append(0)
for loop3 in range(int(numofcand)):
    firstnums.append(0)
print(firstlist)
for loop4 in range(len(votes)):
    first = votes[loop4]
    first = first[0]
    firstlist[loop4] = first
print(firstlist)
print(firstnums)
for firstnum in firstlist:
    print(firstnum)
    if firstnum == 1:
        firstnums[firstnum] = firstnums[firstnum] + 1
    elif firstnum == 2:
        firstnums[firstnum] = firstnums[firstnum] + 1
    elif firstnum == 3:
        firstnums[firstnum] = firstnums[firstnum] + 1
    elif firstnum == 4:
        firstnums[firstnum] = firstnums[firstnum] + 1
    elif firstnum == 5:
        firstnums[firstnum] = firstnums[firstnum] + 1
print(firstnums)
firstnums.pop(0)
winner = False
for loop5 in range(len(firstnums)):
    if firstnums[loop5] >= len(votes) / 2:
        winner = True
        print(f"Candidate {loop5} Wins!")

if not winner:
    while not winner:
        lowest = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        lowests = []
        for loop6 in range(len(firstnums)):
            print(firstnums)
            if not firstnums[loop6] == 'i':
                if firstnums[loop6] < lowest:
                    lowest = firstnums[loop6]
                    lowests = [loop6 + 1]
                elif firstnums[loop6] == lowest:
                    lowests.append(loop6 + 1)
            print(loop6)
        lowestplace = int(random.choice(lowests))
        print(lowest)
        print(lowestplace)
        numstoexclude.append(lowestplace)
        print(len(votes))
        for votetochange in votes:
            if votetochange[0] == lowestplace:
                votetochangeplace = len(votetochange) - 1
                new_place_index = votetochange[votetochangeplace] - 1
                print(new_place_index)
                if votetochange[new_place_index] in numstoexclude:
                    votetochange[votetochangeplace] += 1
                    new_place_index = votetochange[votetochangeplace] - 1
                votetochange[0] = votetochange[new_place_index]
                votetochange[votetochangeplace] = votetochange[votetochangeplace] + 1
                print(votetochange)
        print(votes)
        for loop8 in range(len(votes)):
            first = votes[loop8]
            first = first[0]
            firstlist[loop8] = first
        print(firstlist)
        firstnums = ['ctrl']
        for loop9 in range(int(numofcand)):
            firstnums.append(0)
        print(firstnums)
        for firstnum in firstlist:
            print(firstnum)
            if firstnum == 1:
                firstnums[firstnum] = firstnums[firstnum] + 1
            elif firstnum == 2:
                firstnums[firstnum] = firstnums[firstnum] + 1
            elif firstnum == 3:
                firstnums[firstnum] = firstnums[firstnum] + 1
            elif firstnum == 4:
                firstnums[firstnum] = firstnums[firstnum] + 1
            elif firstnum == 5:
                firstnums[firstnum] = firstnums[firstnum] + 1
        print(firstnums)
        print(numstoexclude)
        for loop9 in range(len(numstoexclude)):
            print(loop9)
            firstnums[numstoexclude[loop9]] = 'i'
        firstnums.pop(0)
        print(firstnums)
        print(len(votes) / 2)
        for loop10 in range(len(firstnums)):
            print(loop10 + 1)
            print(firstnums[loop10])
            if not firstnums[loop10] == 'i' and int(firstnums[loop10]) >= len(votes) / 2:
                winner = True
                print(f"Candidate {loop10 + 1} Wins!")
                

