#include <stdio.h>
#include <string.h>

char c_je[51];  /* */

char* zh( x )                     /* */
double x;                          /* */
{
	int i, n, bz;
	char je[14];        /* */
	char temp[13];
	char f1[10][3] = {" "," "," "," "," "," ",
	                  " "," "," "," "}; /* */
	char f2[11][3] = {" "," "," "," "," ",
	                  " "," "," "," "," "," "}; /* */
	sprintf( je, "%.01f", 100*x); /* */
	n = strlen( je );
	c_je[0] = '\0';
	bz  = 1;
	for( i = 0; i < n; i++ )
	{
		strcpy( temp, &je[i] );  /* */
		if( atoi(temp)==0)    /* i 0*/
		{
			bz = 2;
			break;
		}
		if( je[i] != '0' )
		{
			if( bz == 0 )
				strcat( c_je, f1[0] );
			strcat( c_je, f1[je[i] - '0'] ); /* */
			bz = 1;
			strcat( c_je, f2[13-n+i]);
		}
		else
		{
			if( n-i == 7 && (je[i-1]!='0'||je[i-2]!='0' || je[i-3]!='0')) /* */
				strcat( c_je, " " );
			if( n-i == 3 ) /* */
				strcat( c_je, " ");
			bz = 0;
		}
	}
	if( bz == 2 )
	{
		if( n-i >= 7 && n-i < 10 )
			strcat( c_je, " ") ; /* 0 */
		if( n-i >= 3 )
			strcat( c_je, " ");
		strcat( c_je, " " ); /* */
	}
	return c_je; /* */
}

main()
{
	double count;
	//clrscr();
	printf("*********************************************************\n");
	printf("*                                                       *\n");
	printf("*             Ver.1.0          *\n");
	printf("*                                                       *\n");
	printf("*                                By RZLIN               *\n");
	printf("*                                                       *\n");
	printf("*                                    *\n");
	printf("*                     ");
	scanf("%lf", &count );
	printf("*            %10.2lf                 *\n",count);
	printf("*                                                       *\n");
	printf("* %s\n", zh( count ) );
	printf("*                                                       *\n");
	puts("*                 ...                      *");
	printf("*********************************************************\n");
	getch();
}