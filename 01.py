# Product of Smallest Pair

# def is the keyword to define a function in Python. It is used to create reusable blocks of code that perform a specific task. The syntax for defining a function is as follows:

def psp (arr , d) :     #[78,34,56,12,38]
    if len(arr) < 2 :
        return -1
    
    arr.sort()          #[12,34,38,56,78]
    
    if arr[0]+arr[1] < d :
        return arr[0]*arr[1]
    else :
        return -1
    
# Example usage:
arr = [78, 34, 56, 12, 38] 
d = 50
result = psp(arr, d)
print(result)  # Output: 408 (12 * 34)

print("D = 50 ->",psp([78, 34, 56, 12, 38], 50)) 
print("D = 40 ->",psp([78, 34, 56, 12, 38], 40)) 
print("D = 46 ->",psp([78, 34, 56, 12, 38], 46)) 
print("D = 400 ->",psp([78,100], 400)) 