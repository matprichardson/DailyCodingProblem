def daytwo(a):
    n = [] # new array
    calc = 1 # variable to hold intermediate calculation

    # Enumerate - do this twice so we can build the new array based on the values of the second enumeration
    for count1, value1 in enumerate(a):
        for count2, value2 in enumerate(a):
            if count1 != count2: #Check we aren't handling the current item in the array
                calc = calc * value2
        n.append(calc)
        calc = 1 # reset to 1 for the next pass

    return(n)

print(daytwo([1,2,3,4,5]))