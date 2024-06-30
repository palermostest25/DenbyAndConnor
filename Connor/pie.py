import sys
sys.setrecursionlimit(100)

numnumnumnum = 6
numnumnum = 5
num = 4
numnum = 4
numlist = " + (4/(2*3*4))"
for loop in range(1000000):
     lastnumlist = numlist
     numlist = numlist + " - " + f"(4/({numnum*numnumnum*numnumnumnum}))"
     print(eval(f"3{numlist}"))
     numnum += 2
     numnumnum += 2
     numnumnumnum += 2
     numlist = numlist + " + " + f"(4/({numnum*numnumnum*numnumnumnum}))"
     print(eval(f"3{numlist}"))
     numnum += 2
     numnumnum += 2
     numnumnumnum += 2
     num += 2
     sys.setrecursionlimit(num)




     
