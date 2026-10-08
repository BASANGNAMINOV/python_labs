def min_max(nums: list[float | int]) -> tuple[float | int , float | int]:
    "Вернуть кортеж (минимум, максимум)"
    if nums==[]:
        raise ValueError("Список пуст")
    min=max=nums[0]
    for x in nums[1:]:
        if x<min:
            min=x
        if x>max:
            max=x
    return (min,max)
#print('min_max')
#print( [3, -1, 5, 5, 0] ,"=>",min_max([3, -1, 5, 5, 0]))
#print( [42] ,"=>",min_max([42]))
#print( [-5, -2, -9] ,"=>",min_max([-5, -2, -9]))
#print( [], "=>",min_max([]))
#print( [1.5, 2, 2.0, -3.1], "=>",min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    "Вернуть отсортированный список уникальных значений"
    if nums==[]:
        return []
    unic=list(set(nums))
    for i in range(len(unic)):
        for j in range(len(unic)-1):
            if unic[j]>unic[j+1]:
                unic[j],unic[j+1]=unic[j+1],unic[j]
    return unic
#print('unique_sorted')
#print( [3, 1, 2, 1, 3] ,"=>",unique_sorted([3, 1, 2, 1, 3]))
#print( [] ,"=>",unique_sorted([]))
#print( [-1, -1, 0, 2, 2] ,"=>",unique_sorted([-1, -1, 0, 2, 2]))
#print( [1.0, 1, 2.5, 2.5, 0], "=>",unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    "«Расплющить» список списков/кортежей в один список по строкам"
    if mat==[]:
        raise ValueError("Список пуст")
    finalmat=[]
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise TypeError("строка не строка строк матрицы")
        for element in row:
            finalmat.append(element)
    return finalmat
#print("flatten")
#print( [[1, 2], [3, 4]] ,"=>",flatten([[1, 2], [3, 4]]))
#print( [[1, 2], (3, 4, 5)] ,"=>",flatten([[1, 2], (3, 4, 5)]))
#print( [[1], [], [2, 3]] ,"=>",flatten([[1], [], [2, 3]]))
#print( [[1, 2], "ab"] ,"=>",flatten([[1, 2], "ab"]))


        
        

        