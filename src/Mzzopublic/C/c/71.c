#include   <stdio.h> 
#include   <string.h> 
#include   <stdlib.h> 
#include   <conio.h> 
 
/* */ 
#define   TRUE   1 
#define   FALSE   0 
#define   OK   1 
#define   ERROR   0 
#define   NULL   0 
#define   OVERFLOW   -2 
#define   MAXSIZE   100 
#define   stack_init_size   100 
#define   stackincrement   10 
typedef   char   selemType; 
typedef   char   qelemType; 
typedef   char   elemType; 
typedef   int   status; 
char   e;     
char   demon[MAXSIZE];
     
/*  */   
typedef   struct   
{   
	selemType   *base; 
	selemType   *top; 
	int   stacksize; 
}sqstack;     
status   initstack   (sqstack   *s) 
{     
	s->base=(selemType   *)malloc(stack_init_size*sizeof(selemType));     
	if(!s->base)   exit   (OVERFLOW); 
	s->top=s->base; 
	s->stacksize=stack_init_size; 
	return   OK; 
}/* */ 
status   push   (sqstack   *s,selemType   e) 
{ 
	if(s->top-s->base>=s->stacksize) 
	{ 
		s->base=(elemType*)   realloc(s->base,(s->stacksize+stackincrement)*sizeof(elemType))     
		if(!s->base)   exit(OVERFLOW); 
		s->top=s->base+s->stacksize; 
		s->stacksize+=stackincrement; 
	} 
	*(s->top++)=e; 
	return   OK; 
}/* */ 
status   pop(sqstack   *s,selemType   *e) 
{     
	if(s->top==s->base)   return   ERROR; 
	*e=*(--(s->top)); 
	return   OK; 
}/* */ 
/* */ 
typedef   struct   qnode 
{ 
	qelemType   data; 
	struct   qnode   *next; 
}qnode,*queueptr; 
typedef   struct 
{ 
	queueptr   front; 
	queueptr   rear; 
}linkqueue; 
status   initqueue(linkqueue   *q) 
{ 
	q->front=q->rear=(queueptr)malloc(sizeof(qnode)); 
	if(!q->front)   exit(OVERFLOW); 
	q->front->next=NULL; 
	return   OK; 
}/* */ 
status   enqueue(linkqueue   *q,qelemType   e) 
{ 
	queueptr   p; 
	p=(queueptr)malloc(sizeof(qnode)); 
	if(!p)   exit(OVERFLOW); 
	p->data=e; 
	p->next=NULL; 
	q->rear->next=p; 
	q->rear=p; 
	return   OK; 
}/* */ 
status   dequeue(linkqueue   *q,qelemType   *e) 
{ 
	queueptr   p; 
	if(q->front==q->rear)   return   ERROR; 
	p=q->front->next; 
	*e=p->data; 
	q->front->next=p->next; 
	if(q->rear==p) 
	{ 
		q->rear=q->front; 
	} 
	free(p);
	return   OK;
}/* */ 
 /* */
void   tempstack(sqstack   *temps) 
{ 
	int   i=0; 
	char   t; 
	char   c;
	c=demon[i];
	for(i=0;c!='#';i++)/* */
	{
		c=demon[i];
		if(c=='(')/* */
		{
			t=demon[i+1];/* */
			push(temps,t);/* */
			i++;/* */
			do 
			{ 
				i++; 
				c=demon[i]; 
				push(temps,c)/* */; 
				push(temps,t);/* */ 
			}while(c!=')');/* */ 
			pop(temps,&t);/* t */ 
			pop(temps,&t);   /* ')' */ 
		} 
	} 
}/* */ 

 /* */
void   spenqueue(linkqueue   *q,char   key)     
{     
	int   j=0;
	char   a[5]; 
	switch(key)   /* */ 
	{ 
	case'A':strcpy(a,"ase");break; 
	case'B':strcpy(a,"tAdA");break;
	case'C':strcpy(a,"abc");break; 
	case'D':strcpy(a,"def");break; 
	case'E':strcpy(a,"ghi");break; 
	case'F':strcpy(a,"klm");break; 
	case'H':strcpy(a,"mop");break; 
	default:strcpy(a,"???");   /* "???" */ 
	} 
	while(a[j]!='\0')   /* */ 
	{ 
		enqueue(q,a[j]);/* */ 
		j++; 
	} 
}/* */ 
/* */ 
status   sort(sqstack   *s,linkqueue   *q) 
{     
	qnode   b; 
	int   flag=0;/* */ 
	int   i; 
	for(i=0;demon[   i]!='#';i++)/* */ 
	{ 
		b.data=demon[   i]; 
		if(   ('a'<=b.data&&b.data<='z')||b.data=='?')   /* '?' */     
		{ 
			enqueue(q,b.data); 
		} 
		else 
		{ 
			if('A'<=b.data&&b.data<='Z')   /* , ,*/     
			{ 
				spenqueue(q,b.data); 
				flag=1;   /* 1*/ 
			} 
			else 
			{ 
				if(b.data=='(')/* */ 
				{
					do 
					{ 
						pop(s,&e); 
						enqueue(q,e); 
					}while(!(s->top==s->base));   /* , */     
					while   (b.data!=')')   /* , , */ 
					{ 
						i++; 
						b.data=demon[i]; 
					} 
				} 
			} 
		} 
	}
	return   flag; 
}/* */
/* */
status   main() 
{ 
	sqstack   s1; 
	linkqueue   q1; 
	int   k=0; 
	int   flag=1; 
	clrscr(); 
	printf("Please   Input   the   Demon's   Words:\n"); 
	printf("!:   Less   Than   30   Letters:   )\n"); 
	printf("!:   End   with   '#':   )\n\t"); 
	scanf("%s",demon);
	printf("\n***************************************"); 
	initstack(&s1);   /* */ 
	initqueue(&q1);   /* */ 
	tempstack(&s1);   /* */ 
	while   (flag==1)   /* */ 
	{ 
		k=0; 
		flag=sort(&s1,&q1); 
		while(q1.front!=q1.rear)   /* demon[i   ]*/ 
		{ 
			dequeue(&q1,&e); 
			demon[k]=e;
			k++;
		}
		demon[k]='#';
	}
	demon[k]='\0';
	printf("\n***************************************");
	printf("\nThe   Human   Words:\n\t%s",demon);
	printf("\n***************************************");
}
