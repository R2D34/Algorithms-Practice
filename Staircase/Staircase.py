import numpy as np

def staircase(height, strides):
    #0 is our ground condition
    #if we have no stairs there is only 1 way to go
    if height == 0:
        return 1
        # numpy array for higher efficiency: no rellocation of memory
    ways = np.zeros(height + 1)
    ways[0] = 1

    for currStep in range (1, height+1):
        total = 0
        for currStride in strides:
            #Check whether currently analized step
            #Isn't getting us behind our goal
            if (height - currStride)>= 0:
                #If it doesn't, we can add to our total
                # amount of ways, the amount of ways
                # that currStep-currStride step can be reached
                total += ways[currStep - currStride]
        ways[currStep] = total
    return ways[height]