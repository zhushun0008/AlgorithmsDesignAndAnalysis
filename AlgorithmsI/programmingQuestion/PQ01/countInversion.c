#include<stdio.h>
#include<stdlib.h>
#define MAX_AYYAY_LENGTH	101000
#define MAX_LINE_LENGTH		1024

long long countSortInversion(int *a, int start, int middle, int end)
{
	int *l = NULL;
	int *r = NULL;
	long long count = 0;
	int lsize = middle -start + 1;
	int rsize = end - middle;
	int i = 0;
	int j = 0;
	int k = start;
	l = (int *)malloc(lsize*sizeof(int));
	r = (int *)malloc(rsize*sizeof(int));
	for (i = 0;i < lsize; i++)
		l[i] = a[start + i];
	for (i = 0;i < lsize; i++)
		printf("%d,",l[i]);
	printf("\n");
	for (j = 0; j< rsize; j++)
		r[j] = a[middle+1+j];
	i = 0;
	j = 0;
	while(i < lsize && j< rsize)
	{
		if (l[i] <= r[j])
		{
			a[k] = l[i];
			k++;
			i++;
		}
		else
		{
			a[k] = r[j];
			k++;
			j++;
			count += lsize - i;
		}
	}
	while(i < lsize && k <= end)
		a[k++] = l[i++];
	while(j < rsize && k <= end)
		a[k++] = r[j++];
	free(l);
	free(r);
	return count;
}

long long countAndSort(int *a, int start, int end)
{
	long long x = 0;
	long long y = 0;
	long long z = 0;
	int *p = a;
	int i = 0;
	int middle = (start + end)/2;
	if (p == NULL)
		return 0;
	printf("start=%d,mid=%d,end=%d\n",start,middle,end);
	if (end > start)
	{
		x = countAndSort(a, start, middle);
		y = countAndSort(a,middle+1, end);
		z = countSortInversion(a, start, middle, end);
		p = a;
		printf("mergearray:\n");
		for (i = start; i <= end; i++)
			printf("%d,",p[i]);	
		printf("\n");
		return (x + y + z);
	}
	else
		return 0;

}
int main()
{
	int *start = (int*)malloc(sizeof(int)*MAX_AYYAY_LENGTH);
	int *p = start;
	int i = 0;
	int length = 0;
	long long count = 0;
	FILE * fp = fopen("IntegerArray.txt", "r");
	char buf[MAX_LINE_LENGTH] = {0};
	if (fp == NULL)
	{
		printf("This file can not be opened, maybe it does not exist\n");
		exit(1);
	}
	while (fgets(buf, MAX_LINE_LENGTH, fp) != NULL)
	{
		p[length++] = atoi(buf);
		memset(buf, 0 , MAX_LINE_LENGTH);
	}
	p = start;
//	for (i = 0; i < MAX_AYYAY_LENGTH; i++)
//		printf("%d,",p[i]);	
//	printf("\n");
	count = countAndSort(start,0, length-1);
	printf("%lld\n",count);	
//	p = start;
//	for (i = 0; i < length; i++)
//		printf("%d,",p[i]);	
//	printf("\n");	
}



