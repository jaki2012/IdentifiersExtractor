#include<stdio.h>
void main()
{
    int x,y,z,count=0;
    clrscr();
    puts("****************************************************************");
    puts("*  This program is to solve an interesting math question in    *");
    puts("*                  Karl Marx's manuscript.                     *");
    puts("* The Problem is as follows: 30 persons spent 50 yuan in a     *");
    puts("* restaurant, amony them, each man spent 3 yuan, each woman    *");
    puts("* spent 2 yuan, and each child spent 1 yuan. The question is   *");
    puts("* how many men, women and children are there?                  *");
    puts("****************************************************************");
    puts(" >> The solutions are:");
    printf("   No.        Men       Women     Children\n");
    printf("---------------------------------------------\n");
    for(x=0;x<=10;x++)
    {
        y=20-2*x;                     /*x (3) y*/
        z=30-x-y;                     /* (1) z*/
        if(3*x+2*y+z==50)             /* (2)*/
	    printf(" <%2d>    |    %2d    |    %2d    |    %2d\n",++count,x,y,z);
    }
    printf("---------------------------------------------\n");
    printf(" Press any key to quit...");
    getch();
}
