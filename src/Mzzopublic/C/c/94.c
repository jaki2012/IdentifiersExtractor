#include<stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#define N 30000
void main()
{
   double e=0.1,b=0.5,c,d;
   long int i;                /*i:  */
   float x,y;
   int c2=0,d2=0;
   clrscr();
   puts("***********************************************************");
   puts("*      This program is to calculate PI approximatively    *");
   puts("*                    in two methods.                      *");
   puts("*       One method is Regular Polygon Approximating,      *");
   puts("*          the other is Random Number Method.             *");
   puts("***********************************************************");
   puts("\n >> Result of Regular Polygon Approximating:");
   for(i=6;;i*=2)            /* */
   {
      d=1.0-sqrt(1.0-b*b);     /* */
      b=0.5*sqrt(b*b+d*d);
      if(2*i*b-i*e<1e-15) break;         /* 1e-15 */
      e=b;      /* */
   }
   printf("---------------------------------------------------------\n");
   printf(" >> pi=%.15lf\n",2*i*b);       /* */
   printf(" >> The number of edges of required polygon:%ld\n",i);
   printf("---------------------------------------------------------\n");
   randomize();
   while(c2++<=N)
   {
        x=random(101);      /*x: 0 100 101 */
        y=random(101);      /*y: 0 100 101 */
        if(x*x+y*y<=10000)     /* */
            d2++;
   }
   puts("\n >> Result of Random Number Method:");
   printf("---------------------------------------------------------\n");
   printf(" >> pi=%f\n",4.*d2/N);    /* */
   printf("---------------------------------------------------------\n");
   puts("\n Press any key to quit...");
   getch();
}
