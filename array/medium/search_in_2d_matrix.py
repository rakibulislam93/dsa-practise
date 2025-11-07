
# mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ] 
# target = 8
mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
target = 78
result = False
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==target:
            result = True
            break


print("True" if result else "False")