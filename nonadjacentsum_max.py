#!/usr/bin/env python3

def calcMax(list):

    max1 = max2 = temp = 0

    for num in reversed(list):
        #print("=========")
        #print("num:" +  str(num))
        temp = max1
        
        if (num + max2 > max1):
            max1 = num + max2
        else:
            max1 = 0 + max1

        max2 = temp
        
        #print("max1 "+str(max1))
        #print("max2 "+str(max2))

    print(max1)



calcMax([1, 2, 3])
