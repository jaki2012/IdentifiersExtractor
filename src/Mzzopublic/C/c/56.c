#include<stdio.h>
#include<stdlib.h>
#define NULL 0 /* */
typedef struct node /* */
{
	char c; /* */
	struct node *next; /* */
}Node,*L; /* Node *L struct node */

main()
{
	L l,p,q,r; /* */
	char ch;
	l=(L)malloc(sizeof(Node)); /* */
	l->c='\0'; /* */
	l->next=NULL; /* */
	q=l; /*q */
	printf("Input a character:\n");
	scanf("%c",&ch);
	getchar();
	while(ch!='0') /* 0 */
	{
		p=(L)malloc(sizeof(Node)); /* */
		p->c=ch;
		p->next=NULL; /* */
		q->next=p; /*q */
		q=p; /*q */
		scanf("%c",&ch);
		getchar();
	}	
	/* */
	q=l->next;
	p=q->next;
	r=p->next;
	q->next=NULL;
	while(r!=NULL)
	{
		p->next=q;
		q=p;
		p=r;
		if(r->next!=NULL) /*r */
			r=r->next;
		else
			break;
	}
	r->next=q;
	l->next=r; // 
	
	q=l; /* q l */
	while(q->next!=NULL) /* q */
	{
		printf("%c-->",q->next->c); /*q->next->c q */
		q=q->next; /* q */
	}
	printf("\n");
}
