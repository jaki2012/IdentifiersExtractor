#include<stdio.h>
#define MAX 255
void main()
{
    int i,j,t,k,m,a[MAX];
    long n;
    clrscr();
    puts("     This program will find the Armstrong number.\n");
    printf(" >> Please input the range you want to find (2~n):\n >> ");
    scanf("%ld",&n);
    m=n;
    j=10;
    while(m>=10)
    {
	m=m/10;
	j*=10;
    }
    printf(" >> There are follwing Armstrong number smaller than %d:\n",n);
    for(i=2;i<n;i++)         /* i 2~1000*/
    {
	for(t=0,k=10;k<=j;t++)     /* i ( )*/
        {
	    a[t]=(i%k)/(k/10);        /* a[0]~a[2}*/
	    k*=10;
	}
	for(m=0,t--;t>=0;t--)
		m+=a[t]*a[t]*a[t];
	if(m==i)
                                       /* i */
            printf("%5d",i);            /* */

    }
    printf("\n Press any key to quit...\n");
    getch();
}
