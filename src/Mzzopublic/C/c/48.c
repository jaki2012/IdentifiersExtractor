#include <stdio.h>
#define MAX 255
int R[MAX];

void Merge(int low,int m,int high)
{/*  R[low..m) R[m+1..high]  */
     /*  R[low..high] */
     int i=low,j=m+1,p=0; /*   */
     int *R1; /* R1 p  */
     R1=(int *)malloc((high-low+1)*sizeof(int));
     if(!R1) /*   */
     {
       puts("Insufficient memory available!");
       return;
     }
     while(i<=m&&j<=high) /*  R1[p]  */
       R1[p++]=(R[i]<=R[j])?R[i++]:R[j++];
     while(i<=m) /*  1 R1  */
       R1[p++]=R[i++];
     while(j<=high) /*  2 R1  */
       R1[p++]=R[j++];
     for(p=0,i=low;i<=high;p++,i++)
       R[i]=R1[p];/*  R[low..high] */
} /* end of Merge */


void Merge_SortDC(int low,int high)
{/*  R[low..high]  */
       int mid;
       if(low<high)
       {/*  1 */
          mid=(low+high)/2; /*   */
	  Merge_SortDC(low,mid); /*  R[low..mid]  */
	  Merge_SortDC(mid+1,high); /*  R[mid+1..high]  */
          Merge(low,mid,high); /*   */
        }
}/* end of Merge_SortDC */


void main()
{
	int i,n;
	clrscr();
	puts("Please input total element number of the sequence:");
	scanf("%d",&n);
	if(n<=0||n>MAX)
	{
		printf("n must more than 0 and less than %d.\n",MAX);
		exit(0);
	}
	puts("Please input the elements one by one:");
	for(i=1;i<=n;i++)
		scanf("%d",&R[i]);
	puts("The sequence you input is:");
	for(i=1;i<=n;i++)
		printf("%4d",R[i]);
	Merge_SortDC(1,n);
	puts("\nThe sequence after merge_sortDC is:");
	for(i=1;i<=n;i++)
		printf("%4d",R[i]);
	puts("\n Press any key to quit...");
	getch();
	
}