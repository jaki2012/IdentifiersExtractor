#include "math.h"
#include "stdio.h"


int BinSearchRoot(a,b,h,eps,x,m) /* */
int m;
/* 
a     
b      [a,b] 
h     
eps   
x     
m     */
double a,b,h,eps,x[];
{ 
	extern double Equation(); /* */
    int n,js;
    double z,y,z1,y1,z0,y0;
    n=0; z=a; y=Equation(z);
    while ((z<=b+h/2.0)&&(n!=m)) /* */
	{ 
		if (fabs(y)<eps)  /* */
		{ 
			n=n+1; 
			x[n-1]=z;
            z=z+h/2.0; 
            y=Equation(z);
		}
        else /* */
		{ 
			z1=z+h; 
			y1=Equation(z1);
			if (fabs(y1)<eps) /* */
			{ 
				n=n+1;
				x[n-1]=z1;
				z=z1+h/2.0;
				y=Equation(z);
			}
			else if (y*y1>0.0) /* */
			{ y=y1; z=z1;}
			else   /* */
			{ 
				js=0;/* 0 1 */
				while (js==0)
				{ 
					if (fabs(z1-z)<eps) /* */
					{ 
						n=n+1;  
						x[n-1]=(z1+z)/2.0; /* */
						z=z1+h/2.0; /* */
						y=Equation(z);
						js=1; /* */
					}
					else /* */
					{ 
						z0=(z1+z)/2.0;  /* */ 
						y0=Equation(z0);
						if (fabs(y0)<eps) /*z0 */
						{ 
							x[n]=z0; 
							n=n+1; 
							js=1;
							z=z0+h/2.0; 
							y=Equation(z);
						}
						else if ((y*y0)<0.0) /*[z,z0] */
						{ z1=z0; y1=y0;} 
						else { z=z0; y=y0;}
					}
				}
			}
		}
	}
    return(n); /* */
}
main()
{
	int i,n;
    static int m=6;
    static double x[6];
    clrscr();
    puts("This is a program to solve Nonlinear function\n   by Binary Divisive Procedure.");
    puts("\n The Nonlinear function is:");
    puts("\n f(x)=(((((x-5.0)*x+3.0)*x+1.0)*x-7.0)*x+7.0)*x-20.0\n");
    n=BinSearchRoot(-2.0,5.0,0.2,0.000001,x,m);
    puts("\n >> Solve successfully!\n >> The results are:");
    printf(" >> The function has %d roots, they are:\n",n);/* */
    for (i=0; i<=n-1; i++)
		printf(" >> x(%d)=%13.7e\n",i,x[i]);
    printf("\n Press any key to quit...\n");
    getch();

}

double Equation(x)
double x;
{
	double z;
	z=(((((x-5.0)*x+3.0)*x+1.0)*x-7.0)*x+7.0)*x-20.0;
	return(z);
}