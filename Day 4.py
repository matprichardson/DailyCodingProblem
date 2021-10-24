def DayFour(a):
    i = 1
    while True:
        if i in a:
            i += 1
        else:
            return i
    
print(DayFour([3,4,2,6,7,3,4,5,8,10,-1,1]))
