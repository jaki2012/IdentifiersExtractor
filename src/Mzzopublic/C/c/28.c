#define ERR 5
#define OK 6
#include <stdio.h>
  
int status;
double result,sig,scale;
int sign(int c)/* */
{
	if(c=='-')/* */
		sig=-sig;
}

int integer(int c)/* */
{
	result=result*10.0+c-'0';
}

int decimal(int c)/* */
{
	result+=(c-'0')*scale;
	scale/=10.0;
}
/* */
int statbl[ ][4]={{   1,2,3,ERR},/*0*/
	        {ERR,2,3,ERR},/*1*/
	        {OK,2,4,OK},/*2*/
	        {ERR,4,ERR,ERR},/*3*/
	        {OK,4,OK,OK}};/*4*/
/* */
int(*funtbl[ ][4])( )={{sign,integer,NULL,NULL},
	                {NULL,integer,NULL,NULL},
	                {NULL,integer,NULL,NULL},		
	                {NULL,decimal,NULL,NULL},
                                    {NULL,decimal,NULL,NULL}};

int readreal(double *dp)
{
	int c,ckind;
	sig=1.0;
	result=0.0;
	scale=0.1;

	while((c=getchar( ))==' '||c=='\n'||c=='\t');/* */
	status=0;/* */
	for(;;)
	{
		/* */
		if(c=='+'||c=='-') ckind=0;/* */
		else if(c>='0'&&c<='9') ckind=1;/* */
		else if(c=='.') ckind=2;/* */
		else ckind=3;/*   */

		if(funtbl[status][ckind])/*   */
			(*funtbl[status][ckind])(c);/*   */
		status=statbl[status][ckind];/* */
		if(status==ERR||status==OK)break;/*   */
		c=getchar();
	}
	ungetc(c,stdin); /*   */
	if(status==OK)
	{
		*dp=result *sig;/*   */
		return 1;
	}
	return -1; /*   */
}
main()
{
	double x;
	clrscr();
	printf("\nPlease input real numbers (use nonreal char to end input):\n");
	while(readreal(&x)==1)
		printf("The real number you input is: %f\n",x);
	printf("\nYou have inputted nonreal char.\n Press any key to quit...\n");	
	getch();
}