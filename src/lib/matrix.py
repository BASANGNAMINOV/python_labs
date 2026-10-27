def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat==[]:
        return []
    if all(len(i) == len(mat[0]) for i in mat):
        nmat=[]
        for i in range(len(mat[0])):
            row=[]
            for j in range(len(mat)):
                row.append(mat[j][i])
            nmat.append(row)
        return nmat
    else:
        raise ValueError("Матрица рваная")

#print("transpose")
#print([[1, 2, 3],], "=>", transpose([[1, 2, 3]]))
#print([[1], [2], [3]], "=>", transpose([[1], [2], [3]]))
#print([[1, 2], [3, 4]], "=>", transpose([[1, 2], [3, 4]]))
#print([], "=>", transpose([]))
#print([[1, 2], [3]], "=>", transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    "Вернуть список сумм по строкам матрицы"
    if mat==[]:
        return []
    if all(len(i) == len(mat[0]) for i in mat):
        sums=[]
        for row in mat:
            sums.append(sum(row))
        return sums
    else:
        raise ValueError("Матрица рваная")
# print("row_sums")
# print([[1, 2, 3], [4, 5, 6]], "=>", row_sums([[1, 2, 3], [4, 5, 6]]))     
#print([[-1, 1], [10, -10]], "=>", row_sums([[-1, 1], [10, -10]]))        
# print([[0, 0], [0, 0]], "=>", row_sums([[0, 0], [0, 0]]))            
# print([[1, 2], [3]], "=>", row_sums([[1, 2], [3]]))   

def col_sums(mat: list[list[float | int]]) -> list[float]:
    "Вернуть список сумм по столбцам матрицы"
    if mat==[]:
        return []
    if all(len(i) == len(mat[0]) for i in mat):
        sums=[]
        for i in range(len(mat[0])):
            col_sum=0
            for j in range(len(mat)):
                col_sum+=mat[j][i]
            sums.append(col_sum)
        return sums
    else:
        raise ValueError("Матрица рваная")
#print("col_sums")
#print([[1, 2, 3], [4, 5, 6]], "=>", col_sums([[1, 2, 3], [4, 5, 6]]))     
#print([[-1, 1], [10, -10]], "=>", col_sums([[-1, 1], [10, -10]]))        
#print([[0, 0], [0, 0]], "=>", col_sums([[0, 0], [0, 0]]))            
#print([[1, 2], [3]], "=>", col_sums([[1, 2], [3]]))    
    