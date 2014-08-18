def countSplitInver(left, right, start, mid, end):
	result = []
	l = []
	r = []
	count = 0
	i, j = 0, 0
	lsize = mid - start + 1
	rsize = end - mid
	while i < lsize :
			l.append(left[i])
			i += 1
	i = 0
	while i < rsize :
		r.append(right[i])
		i += 1
	i = 0	
	while i < lsize and j < rsize:
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			count = lsize - i
	if i < lsize:
		result.append(right[i])
		i += 1
	else:
		result.append(right[j])
		j += 1
	return result, count		
	
def countSortInversion(A, start, end):
	count = 0
	if end > start:
		mid = (int)((start+end)/2)
		left, x = countSortInversion(A, start, mid)
		right, y = countSortInversion(A,mid+1, end)
		A, z = countSplitInver(left, right, start, mid, end)
		count = x + y + z
	return A, count

def main():
	f = open('Integer.txt', 'r')
	b = []
	A = []
	for line in f:
		A.append(int(line))
	print A
	b,count  = countSortInversion(A, 0, len(A)-1)
	print b
	print count

if __name__ == "__main__":
	main()

