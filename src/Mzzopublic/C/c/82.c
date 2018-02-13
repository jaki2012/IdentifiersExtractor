#include<stdio.h>
void main()
{
    int n,a,b;
    clrscr();
    puts("==========================================================");
    puts("||  This program will find the four figures which have  ||");
    puts("||     the characteristic as follows: abcd=(ab+cd)^2.   ||");
    puts("||            e.g., 3025=(30+25)*(30+25).               ||");
    puts("==========================================================");
    printf("\n >> There are following numbers with satisfied condition:\n\n");
    for(n=1000;n<10000;n++)             /* N 1000~9999*/
    {
        a=n/100;                        /* N a*/
        b=n%100;                        /* N b*/
        if((a+b)*(a+b)==n)      /* N */
	    printf(" %d  ",n);
    }
    puts("\n\n >> Press any key to quit...");
    getch();
}
