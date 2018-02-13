/*  BC31   VC6.0*/
/* compile under Borland C++ 3.1 or Visual C++ 6.0*/

/*#include "stdafx.h"*/
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "conio.h"

#define TRUE 1
#define FALSE 0
#define STACK_INIT_SIZE 100/* */
#define STACKINCREMENT 20/* */

typedef struct
{
	int *pBase;/* ,base NULL*/
	int *pTop;/* */
	int StackSize;/* , */
}Stack;

typedef int BOOLEAN;
 
char Operator[8]="+-*/()#";/* */
char Optr;/* */
int Opnd=-1;/* */
int Result;/* */

/* */
char PriorityTable[7][7]=
{
	{'>','>','<','<','<','>','>'},
	{'>','>','<','<','<','>','>'},
	{'>','>','>','>','<','>','>'},
	{'>','>','>','>','<','>','>'},
	{'<','<','<','<','<','=','o'},
	{'>','>','>','>','o','>','>'},
	{'<','<','<','<','<','o','='},
};

// 
// , 0, 
Stack InitStack()/* */
{
	Stack S;
	S.pBase=(int*)malloc(STACK_INIT_SIZE*sizeof(int));
	if(!S.pBase)
	{/* */
		printf(" , \n");
		exit(-1);
	}
	else
	{
		S.pTop=S.pBase;
		S.StackSize=STACK_INIT_SIZE;
	}
	return S;
}
// S,S 
void DestoryStack(Stack *S)
{
	if(S->pBase)
	{
		free(S->pBase);
		S->pTop=S->pBase=NULL;
        
	}
}
// , e S 
// : , 
int GetTop(Stack S)
{
	return *(S.pTop-1);
}
// e , 1, 0
int Push(Stack *S,int e)
{
	if(S->pTop-S->pBase==S->StackSize)
	{// , 
		S->pBase=(int*)realloc(S->pBase,S->StackSize+STACKINCREMENT*sizeof(int));
		if(!S->pBase)
			return 0;// 
		S->pTop=S->pBase+S->StackSize;
		S->StackSize+=STACKINCREMENT;
	}
	*(S->pTop++)=e;
	return 1;
}

int Pop(Stack *S,int *e)
{// , S , e  , 1; 0
	if(S->pTop==S->pBase)
		return 0;
	*e=*--(S->pTop);
	return 1;

}
// 
// operator_1,operator_2 , '<','=', '>'
char CheckPriority(char operator_1,char operator_2)
{
	int i,j;// 
	//char *ptr;
	i=strchr(Operator,operator_1)-Operator;// Operators 
	j=strchr(Operator,operator_2)-Operator;
	// 
	return PriorityTable[i][j];
}

BOOLEAN IsOperator(char ch)
{// 
	if(strchr(Operator,ch))
		return TRUE;
	else 
		return FALSE;

}
// 
void GetInput(void)
{
	char Buffer[20];// , 
	char ch;// 
	int index;// Buffer 
	index=0;
	ch=getch();// 
	while(ch!=13&&!IsOperator(ch))
	{// , 
		if(ch>='0'&&ch<='9')
		{// 
			printf("%c",ch);
			Buffer[index]=ch;
			index++;

		}
		ch=getch();
	}
	if(ch==13)
		Optr='#';// 
	else
	{
		Optr=ch;
		printf("%c",ch);

	}
	if(index>0)
	{
		Buffer[index]='\0';
		Opnd=atoi((Buffer));
	}
	else
		Opnd=-1;// , Opnd , 
}
// a+b ,theta ,a,b 
int Calc(int a,char theta,int b)
{
	switch(theta)
	{
	case '+':
		return a+b;
	case '-':
		return a-b;
	case '*':
		return a*b;
	default:
		if(b==0)// 
		{
			printf(" ");
			return 0;// 0 
		}
		else
			return a/b;
	}
}
/* */
BOOLEAN EvaluateExpression()
{
	int temp;// 
	char theta;// 
	int itheta;// add by me
	int a,b;// 
	int topOpnd;// 
	char topOptr;// 
	
	Stack OPTR=InitStack();// 
	Stack OPND=InitStack();// 

	if(!Push(&OPTR,'#'))// # 
		return FALSE;

	GetInput();// 

	while(Optr!='#'||GetTop(OPTR)!='#')
	{// Optr>=0, 
		if(Opnd>=0)Push(&OPND,Opnd);
		switch(CheckPriority(GetTop(OPTR),Optr))
		{
		case '<':// 
			if(!Push(&OPTR,Optr))return FALSE;
				GetInput();
			break;
		case '=':// 
			Pop(&OPTR,&temp);GetInput();
			break;
		case '>':// 
			// itheta theta
			Pop(&OPTR,&itheta);
			Pop(&OPND,&b);
			Pop(&OPND,&a);
			theta = (char)( itheta );
			Push(&OPND,Calc(a,itheta,b));
			Opnd=-1;
			break;

		}
	}
	// , ,
	//OPND.pTop==OPND.pBase
	// OPND.pTop==OPND.pBase Opnd<0, 
	// [ ], 
	// 
	if(OPND.pTop==OPND.pBase&&Opnd<0)
	{
		printf("\n\n !\n");
		exit(1);

	}
	else if(OPND.pTop==OPND.pBase)
		Result=Opnd;
	else
	{
		Result=GetTop(OPND);
		DestoryStack(&OPND);
		DestoryStack(&OPTR);
	}
	return TRUE;

}

void Message(void)
{
	printf("\n \n");
	printf("-------------------------------\n");
	printf(" : , . 45*(12-2)[ ]\n");
	printf(" 0: [ ] , .\n");
	printf(" 1: .\n");
	printf(" 2: , .\n");
	printf("-------------------------------\n\n");
}
void main(void)
{
	int i;// 
	Message();
	for(i=1;;i++)
	{
		printf(" %d:",i);
		if(EvaluateExpression())
			printf("=%d\n",Result);
		else
			printf(" \n");
		
	}
}
