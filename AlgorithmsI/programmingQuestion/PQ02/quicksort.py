def partitionFirstElem(A, start, end):
	countComparison = end - start
	pivot = A[start]
	i = start + 1
	for j in range(start,end+1):
		if A[j] < pivot:
			(A[i],A[j]) = (A[j],A[i])
			i += 1
	(A[start],A[i-1]) = (A[i-1],A[start])	
	return (i-1,countComparison)

def partitionLastElem(A, start, end):
	countComparison = end - start
	(A[start],A[end]) = (A[end],A[start])
	pivot = A[start]
	i = start + 1
	for j in range(start,end+1):
		if A[j] < pivot:
			(A[i],A[j]) = (A[j],A[i])
			i += 1
	(A[start],A[i-1]) = (A[i-1],A[start])	
	return (i-1,countComparison)

def partitionMiddleElem(A, start, end):
	countComparison = end - start
	mid = int((start+end)/2)
	if A[start]< A[mid]:
		if A[mid] <  A[end]:
			(A[start],A[mid]) = (A[mid],A[start])
		else:
			if A[start] < A[end]:
				(A[start],A[end]) = (A[end],A[start])
			else:
				A[start] = A[start]
	else:
		if A[start] < A[end]:
			A[start] = A[start]
		else:
			if A[mid]< A[end]:
				(A[start],A[end]) = (A[end],A[start])
			else:
				(A[start],A[mid]) = (A[mid],A[start])
	pivot = A[start]
	i = start + 1
	for j in range(start,end+1):
		if A[j] < pivot:
			(A[i],A[j]) = (A[j],A[i])
			i += 1
	(A[start],A[i-1]) = (A[i-1],A[start])	
	return (i-1,countComparison)



def quickSort(A,start,end):
	countComparison = 0
	if start < end:
		(pivot,x) = partitionMiddleElem(A,start,end)
		y = quickSort(A,start, pivot-1)
		z = quickSort(A,pivot+1,end)
		countComparison = x + y + z
	return countComparison



def main():
	f = open('QuickSort.txt', 'r')
	A = []
	count = 0
	for line in f:
		A.append(int(line))
	print A
	print A
	print len(A)
	count = quickSort(A,0,len(A)-1)
	print A
	print count


if __name__ == "__main__":
	main()

