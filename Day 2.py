def daytwo(a):
    n = [] # this will store the new array
    calc = 1 # this will store the intermediate calculated value for each pass through the array.  Start with 1 as will be used to multiply items

    # iterate through the items in the array
    for count1, value1 in enumerate(a):
        for count2, value2 in enumerate(a):
            if count1 != count2: #Check we aren't handling the current item in the array
                calc = calc * value2
        n.append(calc)
        calc = 1

    return(n)

print(daytwo([1,2,3,4,5]))