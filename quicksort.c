#include <stdio.h>

void swap(int* i, int* j)
{
	int ii=*i;
	*i = *j;
	*j = ii;
}

/* find next pivot point */
int pivot(int arr[], int lo, int hi)
{
	/* pivot, new pivot, counter */	
	int p = hi, np = lo, i = lo;

	for(; i < hi; i++)
		if(arr[i] < arr[p]) {
			swap(&arr[i], &arr[np]);
			np++;
		}

	swap(&arr[p], &arr[np]);

	return np;
}

void qs(int arr[], int lo, int hi)
{
	int p;

	if((hi - lo) > 0) {
		p = pivot(arr, lo, hi);
		qs(arr, lo, p-1);
		qs(arr, p+1, hi);
	}
}

void quicksort(int arr[], int sz)
{
	qs(arr, 0, sz-1);
}

int main()
{
	int arr[5] = { 10, 5, 2, 49, 3 }, i = 0;
	quicksort(arr, 5);

	for(; i < 5; i++)
		printf("%d ", arr[i]);
	printf("\n");

	return 0;
}
