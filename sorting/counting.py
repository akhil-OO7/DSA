def count_sort(arr):
    m = max(arr)
    tmp = [0] * (m + 1)
    for i in range(len(arr)):
        tmp[arr[i]] += 1
    print(tmp)
    idx = 0
    i = 0
    while i < m + 1:
        while tmp[i] != 0:
            arr[idx] = i
            idx += 1
            tmp[i] -= 1
        i += 1    
    return arr

# Driver code
if __name__ == "__main__":
	# Input array
	input_array = [4, 3, 12, 1, 5, 5, 3, 9]

	# Output array
	output_array = count_sort(input_array)

	for num in output_array:
		print(num, end=" ")
