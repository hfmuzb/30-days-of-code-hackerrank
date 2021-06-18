# Enter your code here. Read input from STDIN. Print output to STDOUT
#####################################################################
#####################################################################
import math

a = []
T = int(input())
for i in range(T):
    a.append(int(input()))

res = []

for j in a:
    flag = True
    if j == 1:
        flag = False
    else:
        for k in range(2, round(math.sqrt(j)) + 1):
            if j % k == 0:
                flag = False
    if flag:
        res.append('Prime')
    else:
        res.append('Not prime')

print(*res, sep='\n')
#####################################################################
#####################################################################
