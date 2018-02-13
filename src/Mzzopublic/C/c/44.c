#include <stdio.h>
#define MAX 255
int R[MAX];
int Partition(int i,int j)
{/*  Partition(R low high) R[low..high] */
     /*   */
      int pivot=R[i]; /*  1  */
      while(i<j){ /*  i=j  */
        while(i<j&&R[j]>=pivot) /* pivot i  */
          j--;  /*  1 pivot.key R[j] */
        if(i<j) /*  R[j] <pivot.key  */
            R[i++]=R[j]; /*  R[i] R[j] i 1 */
        while(i<j&&R[i]<=pivot) /* pivot j */
            i++; /*  1 pivot.key R[i] */
        if(i<j) /*  R[i] R[i].key>pivot.key */
            R[j--]=R[i]; /*  R[i] R[j] j 1 */
       } /* endwhile */
      R[i]=pivot; /*  */
      return i;
} /* end of partition  */

void Quick_Sort(int low,int high)
{ /*  R[low..high]  */
     int pivotpos; /*   */
     if(low<high){/*  1  */
	pivotpos=Partition(low,high); /*  R[low..high]  */
        Quick_Sort(low,pivotpos-1); /*   */
        Quick_Sort(pivotpos+1,high); /*   */
      }
} /* end of Quick_Sort */


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
	Quick_Sort(1,n);
	puts("\nThe sequence after quick_sort is:");
	for(i=1;i<=n;i++)
		printf("%4d",R[i]);
	puts("\n Press any key to quit...");
	getch();
	
}