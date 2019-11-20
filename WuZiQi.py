import random
def win(r1,r2,r3,n):
    sum_row = sum([r1.count(n) == 3,r2.count(n) ==3,r3.count(n) ==3])
    sum_col = 0
    for i in range(0,3):
        sum_col+=[r1[i],r2[i],r3[i]].count(n) == 3
    sum_diag = sum([[r1[0],r2[1],r3[2]].count(n) == 3,[r1[2],r2[1],r3[0]].count(n) == 3])
    return sum_row+sum_col+sum_diag

def decide(r1,r2,r3):
    r = r1+r2+r3
    if abs(r.count(1) - r.count(2)) >1:
        return -1
    if win(r1,r2,r3,1) == 0 and win(r1,r2,r3,2) == 0 and r.count(0) == 0:
        return 2
    if win(r1,r2,r3,1) >1 or win(r1,r2,r3,2) >1:
        return -1
    if win(r1,r2,r3,1) ==1 or win(r1,r2,r3,2) ==1:
        return -1
    if win(r1,r2,r3,1) ==1 and win(r1,r2,r3,2) ==0:
        return 1
    if win(r1,r2,r3,2) ==1 and win(r1,r2,r3,1) ==0:
        return 2
    else:
        return 2
        
for i in range(1000):
    a1 = [random.randint(0, 2) for iter in range(3)]
    a2 = [random.randint(0, 2) for iter in range(3)]
    a3 = [random.randint(0, 2) for iter in range(3)]
    if decide(a1,a2,a3) == None:
        print('oops'+":"+str(a1)+str(a2)+str(a3))