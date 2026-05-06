# leetcode 134. Gas Station
'''gas = [1,2,3,4,5]
cost = [3,4,5,1,3]'''


def gas_station(gas, cost):
    if sum(gas) < sum(cost): # if total gas is less than total cost, then it's impossible to complete the circuit
        return -1
    
    startidx = 0
    for i in range(len(gas)):
        g = g+ gas[i] - cost[i] # calculate the net gas after visiting the station                                  # 0+1-3 = -2            0-2+2-4 = -4            0-4+3-5 = -6            0-6+4-1 = -3            0-3+5-3 = 2
        if g < 0: # if net gas is negative, then we cannot start from this station, so we move to the next station  # -2 < 0 => True        # -4 < 0 => True        -6 < 0 => True          -3 < 0 => True          2 < 0 => False
            startidx = i + 1 # update the starting index to the next station                                        # startidx = 0 + 1 = 1  startidx = 1 + 1 = 2    startidx = 2 + 1 = 3    startidx = 3 + 1 = 4    startidx = 4 + 1 = 5
            g = 0 # reset the net gas to 0 for the new starting point                                               # g = 0                 g = 0                   g = 0                   g = 0                   g = 0
    return startidx # return the starting index of the station from which we can complete the circuit               # startidx = 1          startidx = 2            startidx = 3            startidx = 4            startidx = 5


