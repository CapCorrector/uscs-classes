matrix = [
	[1, 2, 3],
	[4, 5, 6]
]

result = []
for row_index in range(4):
	row=[]
	for col_index in range(4):
		if row_index == col_index:
			row.append((col_index+1)**2)
		else:
			row.append(0)
	result.append(row)

print(result)


matrix_result = [[(col_index+1)**2 if col_index==row_index else 0 for col_index in range(4)]for row_index in range(4)]
print(matrix_result)
