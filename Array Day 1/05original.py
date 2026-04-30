


def prod_itself(arr):   #[7,5,2,1]
    n = len(arr)
    p = 1
    for i in range(n):
        p *= arr[i] #p = 7*5*2*1 = 70
    res = [1]*n #[1,1,1,1]
    for i in range(n):
        res[i] = p//arr[i]  #res[0] = 70//7 = 10, res[1] = 70//5 = 14, res[2] = 70//2 = 35, res[3] = 70//1 = 70
    return res


print(prod_itself([7,5,2,1]))
print(prod_itself([70,50,20,10]))
