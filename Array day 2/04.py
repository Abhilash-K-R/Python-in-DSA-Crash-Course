# transpose

def trans(arr):
    row = len(arr)
    col = len(arr[0])
    tmat = [[0 for i in range(row)] for j in range(col)]
    for i in range(row) :
        for j in range(col) :
            tmat[j][i] = arr[i][j]
    return tmat

print(trans([[1,2,3],[4,5,6],[7,8,9]]))