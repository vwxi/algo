#include <stdio.h> /*printf()*/
#include <math.h> /*floor()*/

void merge(int arr[], int lo, int mid, int hi)
{
	int L_s = mid - lo + 1, R_s = hi - mid;
	int L[L_s], R[R_s]; /*fuck C90*/
	int i, j, k;

	i=0;j=0;

	for(;i<L_s;i++)
		L[i]=arr[i+lo];

	for(;j<R_s;j++)
		R[j]=arr[j+mid+1];

	i=0;j=0;k=lo;

	while(i<L_s&&j<R_s) {
		arr[k] = (L[i] <= R[j]) ? L[i++] : R[j++];
		k++;
	}
	
	while(i<L_s) {
		arr[k++] = L[i++];
	}

	while(j<R_s) {
		arr[k++] = R[j++];
	}
}

void mergesort(int arr[], int lo, int hi)
{
	int mid;

	if(lo < hi) {
		mid = floor((hi+lo)/2);
		mergesort(arr, lo, mid);
		mergesort(arr, mid + 1, hi);
		merge(arr, lo, mid, hi);		
	}
}

int main()
{
	int arr[5] = {1, 5, 3, 2, 7}, i=0;
	mergesort(arr, 0, 5);
	for(;i<5;i++)printf("%d ",arr[i]);
	printf("\n");
	return 0;
}
