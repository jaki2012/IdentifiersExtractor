#include<stdio.h>
void main()
{
    int i,x,y,last=1;    /* last X Y */
    clrscr();
    puts("**********************************************************");
    puts("*  This is a program to calculate the last 3 digits of   *");
    puts("*              high order value, e.g., 13^15.            *");
    puts("**********************************************************");
    printf("\n >> Input X and Y(X^Y): ");
    scanf("%d%d",&x,&y);
    for(i=1;i<=y;i++)                /*X Y */
        last=last*x%1000;     /* last X 1000 */
    printf("\n >> The last 3 digits of %d^%d is: %d\n",x,y,last%1000); /* */
    puts("\n >> Press any key to quit...");
    getch();
}
