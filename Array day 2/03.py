# spiral matrix

def spiral(arr) :
    res=[]
    t=l=0
    r=len(arr[0])-1 # Last column index #2
    b=len(arr)-1 # Last row index #2
    while l<=r and t<=b :
        for j in range(l,r+1) :
            res.append(arr[t][j])
        t+=1
        for i in range(t,b+1) :
            res.append(arr[i][r])
            # [1][2] = 3 , [2][2] = 10
        r-=1
        if t<=b:
            for j in range(r,l-1,-1) :
                res.append(arr[b][j])
                    # [2][1] = 9 , [2][0] = 8
            b-=1
        if l<=r:
            for i in range(b,t-1,-1) :
                res.append(arr[i][l])
            l+=1
    return res
print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
        

''' for leetcode 54. Spiral Matrix
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # spiral matrix
        res=[]
        t=l=0
        r=len(matrix[0])-1 # Last column index #2
        b=len(matrix)-1 # Last row index #2
        while l<=r and t<=b :
            for j in range(l,r+1) :
                res.append(matrix[t][j])
            t+=1
            for i in range(t,b+1) :
                res.append(matrix[i][r])
                # [1][2] = 3 , [2][2] = 10
            r-=1
            if t<=b:
                for j in range(r,l-1,-1) :
                    res.append(matrix[b][j])
                        # [2][1] = 9 , [2][0] = 8
                b-=1
            if l<=r:
                for i in range(b,t-1,-1) :
                    res.append(matrix[i][l])
                l+=1
        return res
    '''