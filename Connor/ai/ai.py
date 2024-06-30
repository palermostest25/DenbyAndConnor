referances = []
while True:
    try:
        numofr = int(input("Number Of Referances: "))
        break
    except ValueError:
        print("Please Enter A Number!")
for loop0 in range(1, numofr+1):
    referance = open(f"referance{loop0}.txt", "r")
    referances.append(referance.read().strip())
art = open("art.txt", "r")
art = art.read()

linenum = 0
workinglineref = []
workinglineart = []
score = {}
referancethatweareon = 0
for loop1 in range(numofr):
    score.update({f"{loop1+ 1}" : 0})
    for loop2 in range(10):
        workinglineref = referances[referancethatweareon].split()[linenum]
        workinglineref = list(workinglineref)
        workinglineart = art.split()[linenum]
        workinglineart = list(workinglineart)
        for loop3 in range(10):
            if workinglineref[loop3] == "@" and workinglineart[loop3] == "@":
                score[f"{loop1 + 1}"] += 1
        linenum += 1
    referancethatweareon += 1
    linenum = 0


d = score
value = int(max(score))
for key, val in d.items():
        if val == value:
            break
print(art)
print("Is closest to")
print(referances[int(key) - 1])

