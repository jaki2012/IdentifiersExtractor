
#include <stdio.h>
#include <math.h>


void oplot(n,x,y) /* DOS */
int n;
double x[],y[];
{
	int i, j;
	char screen[25][80]; /* */
	memset(screen, ' ', 25*80);  /* */
	/* x */
	for( i = 0; i <79; i++)
		screen[10][i] = '-';
	screen[10][79] = 'X';
	/* y */
	for( i = 1; i <25; i++)
		screen[i][40] = '|';
	screen[0][40] = 'Y';
	/* (x,y) */
	for( i = 0; i < n; i++)
		screen[(int)(x[i]+10)][(int)(y[i]*2+40)] = '*';
	/* */
	for( i = 0; i < 25; i++)
		for( j = 0; j <80; j++)
			printf("%c", screen[i][j] );
}

main()
{
    int points,k;
    double x[50], y[50], angle, portion;
    clrscr();

	points = 40; /* 40 */
	portion = 4.0 * M_PI / points; /* 720 40 */
	/* */
	for (k=0; k<points; k++)
	{
		angle=k * portion; /* */
		x[k]=2.0+angle*cos(angle); /*x */
		y[k]=angle*sin(angle); /*y */
	}
    oplot(points,x,y); /* */

    getch();
}