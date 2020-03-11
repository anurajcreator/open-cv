c = int(input())
n = int(input())
k = int(input())
s = []
flag = 0
for i in range(0,n):
    a = int(input())
    b = int(input())
    s.append([a, b])
s.sort()
#print(s[0][1] , s[1][0])
if k == 0:
    for i in range(0, n-1):
        for j in range(1, n):
            if s[i][1] >= s[j][0]:
                print("Bad")
                flag = 1
                break
    if flag == 0:
        print("Good")

if k == 1:
    count = 0
    setsize = []
    overlap = []
    space = []
    for i in range(0,n):
        x = s[i][1] - s[i][0] + 1
        setsize.append(x) 
    for i in range(0,n):
        if i == 0:
            x = s[i][0] - 1
        else:
            x = s[i][0] - s[i-1][1] - 1
        space.append(x)
    x = c - s[n-1][1]
    space.append(x)
    for i in range(1, n):
       if space[i] < 0:
           if count == 0:
                if i < n - 1:
                    if space[i+1] < 0:
                        for j in range(0,n+1):
                            if setsize[i] <= space[j]:
                                count = 1
                            else:
                                flag = 1
                                break
                else:
                    if abs(space[i]) <= space[i-1] or abs(space[i]) <= space[i+1]:
                        count = 1
                    else:
                        for j in range(0,n+1):
                            if setsize[i] <= space[j]:
                                count= 1
                            else:
                                flag = 1
                                break
           else:
               flag = 1

    if flag == 0:
        print("Good")
    else:
        print("Bad")        


        

    
                    




