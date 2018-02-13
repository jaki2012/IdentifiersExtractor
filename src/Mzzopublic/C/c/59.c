#include <stdio.h>
#include <malloc.h>
#define  N 7                                         // N=7 7 
#define  OVERFLOW  0
#define  OK  1
typedef struct LNode{                              // 
	int password;
	int order;
	struct LNode *next;
}LNode,*LinkList;

int  PassW[N]={3,1,7,2,4,8,4};
void  Joseph(LinkList p,int m,int x);          // 
int main()
{    
	int  i,m;
	LinkList  Lhead,p,q;     // 
	Lhead=(LinkList)malloc(sizeof(LNode));  // 
	if(!Lhead)return OVERFLOW;                   // 
	Lhead->password=PassW[0];
	Lhead->order=1;
	Lhead->next=NULL;
	p=Lhead;
	for(i=1;i<7;i++){
		if(!(q=(LinkList)malloc(sizeof(LNode))))return OVERFLOW;
		q->password=PassW[i];                      // 
		q->order=i+1;
		p->next=q;p=q;                 // p->next , p=q
	}
	p->next=Lhead;                        // p->next , 
	printf(" m:  \n");
	scanf("%d",&m);                                      // m
	printf(" m= %d \n",m);
	Joseph(p,m,N);
    return OK;
}
void  Joseph(LinkList p,int m,int x){
	LinkList q;
	int i;
	if(x==0)return;                          // , 
	q=p;
	m%=x;                                  //m x , 
	if(m==0)m=x;               // m x, m=x, m=0, 
	//for , q ,p ,   
	for(i=1;i<=m;i++){
		p=q;
		q=p->next;                    // q ,p q 
	}
	p->next=q->next;                              // q 
	i=q->password;
	printf("%d  ",q->order);                     
	free(q);                                        // q 
	Joseph(p,i,x-1);
}
