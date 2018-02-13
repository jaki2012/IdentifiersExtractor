#include<stdio.h>
#include<math.h>
void main()
{
    double y;
    int x,m,n,yy;
    clrscr();
    puts("========This program shows the curve of cos(x) and a line.========");
    puts("        ******* f(x)=cos(x)    +++++++ g(x)=45*(y-1)+31");

    for(yy=0;yy<=20;yy++) /* y */
    {
        y=0.1*yy;                       /*y */
        m=acos(1-y)*10;       /*m: cos(x) y */
        n=45*(y-1)+31;        /*n:  y */
        for(x=0;x<=62;x++)              /*x:  */
            if(x==m&&x==n) printf("+");  /* cos(x) "+"*/
            else if(x==n) printf("+");   /* */
            else if(x==m||x==62-m) printf("*");  /* cos(x) */
            else  printf(" ");                  /* */
        printf("\n");
    }
    puts(" Press any key to quit...");
    getch();
}
