#Addition of matrix
X = [[1,2,3],[4 ,5,6],[5 ,8,9]]
Y = [[15,3,7],[3,32,4],[3,2,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]
print("Addition is: ")
for i in range(len(X)):
	for j in range(len(X[i])):
		result[i][j] = X[i][j] + Y[i][j]
for r in result:
	print(r)

#Multiplication of matrix
A = [[12, 7, 3],[4, 5, 6],[7, 8, 9]]
B = [[5, 8, 1, 2],[6, 7, 3, 0],[4, 5, 9, 1]]
result = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
print("Multiplication is: ")
for i in range(len(A)):
	for j in range(len(B[i])):
		for k in range(len(B)):
			result[i][j] += A[i][k] * B[k][j]
for r in result:
	print(r)
