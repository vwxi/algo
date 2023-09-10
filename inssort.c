#include <stdio.h>

void insswap(int* i, int* j)
{
	int ii = *i, jj = *j;
	*i = jj;
	*j = ii;
}

void inssort(int arr[], int sz)
{
	int i = 0, j = 0; /* index */
	
	for(; i < sz; i++) {
		j = i;
		for(; j > 0; j--) {
			if(arr[j] < arr[j-1])
				insswap(&arr[j], &arr[j-1]);
		}
	}
}

int main()
{
	int arr[5] = { 50, 40, 30, 20, 10 }, i = 0;
	inssort(arr, 5);

	for(; i < 5; i++)
		printf("%d ", arr[i]);
	printf("\n");

	return 0;
}
