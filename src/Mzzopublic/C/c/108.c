/*  BC31  */
/* compile under Borland C++ 3.1 */

/*
 ( )
<exp> -> <term> { <addop> <term> }
<addop> -> + | -
<term> -> <factor> { <mulop> <factor> }
<mulop> -> * | /
<factor> -> ( <exp> ) | Number
*/

#include <stdio.h>
#include <stdlib.h>

char token; /* */

/* */
int exp( void );
int term( void );
int factor( void );

void error( void ) /* */
{
	fprintf( stderr, " \n");
	exit( 1 );
}

void match( char expectedToken ) /* */
{
	if( token == expectedToken ) token = getchar(); /* */
	else error(); /* */
}
void Message(void)
{
	printf("================================================================\n");
	printf("*                               *\n");
	printf("****************************************************************\n");
	printf(" : , . 45*(12-2)[ ]\n");
	printf("*****************************************************************\n\n");
}
main()
{
	int result;  /* */
	Message();
	printf(" >>  : ");
	token = getchar(); /* */
	
	result = exp(); /* */
	if( token == '\n' ) /*   */
		printf( " >>   : %d\n", result );
	else error(); /*   */
	puts("\n\n                    ...\n");
	getch();
	return 0;
}

int exp( void )
{
	int temp = term(); /* */
	while(( token == '+' ) || ( token == '-' ))
		switch( token ) {
		case '+': match('+');     /* */
			  temp += term();
			  break;
		case '-': match('-');
			  temp -= term(); /* */
			  break;
		}
	return temp;
}

int term( void )
{
	int div; /* */
	int temp = factor();   /* */
	while(( token == '*' ) || ( token == '/' ))
		switch( token ) {
		case '*': match('*');  /* */
			  temp *= factor();
			  break;
		case '/': match('/');   /* */
			  div = factor();
			  if( div == 0 ) /* 0*/
			  {
			  	fprintf( stderr, " 0.\n" );
			  	exit(1);
			  }
			  temp /= div; 
			  break;
		}
	return temp;
}

int factor( void )
{
	int temp; 
	if( token == '(' ) /* */
	{
		match( '(' );
		temp = exp();
		match(')');
	}
	else if ( isdigit( token )) /* */
	{
		ungetc( token, stdin ); /* */
		scanf( "%d", &temp ); /* */
		token = getchar();  /* */
	}
	else error(); /* */
	return temp;
}