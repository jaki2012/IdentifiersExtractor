#include <stdio.h>
#define CHILDREN 5
struct person{
	char *name;/* */
	char sex;/* 'M' 'F'*/
	struct person *father;/* */
	struct person *mother;/* */
	struct person *mate;/* */
	struct person *children[CHILDREN];/* */
};

/* [ ]newperson  */
struct person *newperson(char *name,char sex)
{
	struct person *p;
	int index;

	p=(struct person *)malloc(sizeof(struct person));
	p->name=(char *)malloc(strlen(name)+1);
	strcpy(p->name,name);
	p->sex=sex;
	p->father=NULL;
	p->mother=NULL;
	p->mate=NULL;
	for(index=0;index<CHILDREN;index++)
		p->children[index]=NULL;
	return p;
}

/* [ ]father_child  */
father_child(struct person *father,struct person *child)
{
	int index;

	for(index=0;index<CHILDREN-1;index++)/* */
		if(father->children[index]==NULL)/* */
			break;
	father->children[index]=child;/* */
	child->father=father;
}
/* [ ]mother_child  */
mother_child(struct person *mother,struct person *child)
{
	int index;
	for(index=0;index<CHILDREN-1;index++)/* */
		if(mother->children[index]==NULL)/* */
			break;
	mother->children[index]=child;/* */
}
/* [ ]mate   */
mate(struct person *h,struct person *w)
{

	h->mate=w;/* */
	w->mate=h;
}

/* [ ]brotherinlow   */
int brothersinlaw(struct person *p1,struct person *p2)
{
	struct person *f1,*f2;

	if(p1==NULL||p2==NULL||p1==p2) return 0;
	if(p1->sex==p2->sex) return 0;/* */
	f1=p1->father;
	f2=p2->father;
	if(f1!=NULL&&f1==f2) return 0;/* */
	while(f1!=NULL&&f2!=NULL&&f1!=f2)/* */
	{
		f1=f1->father;
		f2=f2->father;
		if(f1!=NULL&&f2!=NULL&&f1==f2) return 1;
	}
	return 0;
}
/*  print_relate p  */
void print_relate(struct person *p)
{
	int index,i;
	if(p->name==NULL)
		return;
	if(p->sex=='M')
		printf(" %s is male.",p->name);
	else
		printf(" %s is female.",p->name);
	if(p->father!=NULL)
		printf(" %s's father is %s.",p->name,p->father->name);
	if(p->mother!=NULL)
		printf(" %s's mother is %s.",p->name,p->mother->name);
	printf("\n");
	if(p->mate!=NULL)
		if(p->sex=='M')
			printf(" His wife is %s.",p->mate->name);
		else
			printf(" Her husband is %s.",p->mate->name);
	if(p->children!=NULL)
	{	for(index=0;index<CHILDREN-1;index++)/* */
		if(p->children[index]==NULL)/* index  */
			break;
		if(index>0)
			printf(" Children are:");
		for(i=0;i<index;i++)
			printf(" %s",p->children[i]->name);
	}
	printf("\n");

}
main()
{
	char *name[8]={"John","Kate","Maggie","Herry","Jason","Peter","Marry","Jenny"};
	char male='M',female='F';
	struct person *pGrandfather,*pFather1,*pFather2,*pMother1,*pMother2,*pSon,*pDaughter,*pCousin;
	clrscr();
	pGrandfather = newperson(name[0],male);
	pFather1 = newperson(name[3],male);
	pFather2 = newperson(name[4],male);
	pMother1 = newperson(name[1],female);
	pMother2 = newperson(name[2],female);
	pSon = newperson(name[5],male);
	pDaughter = newperson(name[6],female);
	pCousin = newperson(name[7],female);
	father_child(pGrandfather,pFather1);
	father_child(pGrandfather,pFather2);
	father_child(pFather1,pSon);
	father_child(pFather1,pDaughter);
	father_child(pFather2,pCousin);
	mate(pFather1,pMother1);
	mate(pFather2,pMother2);
	mother_child(pMother1,pSon);
	mother_child(pMother1,pDaughter);
	mother_child(pMother2,pCousin);
	/*   */
	print_relate(pGrandfather);
	print_relate(pFather1);
	print_relate(pFather2);
	print_relate(pMother1);
	print_relate(pMother2);
	print_relate(pSon);
	print_relate(pDaughter);
	print_relate(pCousin);
	

	if(!brothersinlaw(pDaughter,pCousin))
		printf("%s and %s are not brothers (sisters) in law.\n",pDaughter->name,pCousin->name);
	else
		printf("%s and %s are brothers (sisters) in law.\n",pDaughter->name,pCousin->name);
	if(!brothersinlaw(pSon,pCousin))
		printf("%s and %s are not brothers (sisters) in law.\n",pSon->name,pCousin->name);
	else
		printf("%s and %s are brothers (sisters) in law.\n",pSon->name,pCousin->name);
	if(!brothersinlaw(pSon,pDaughter))
		printf("%s and %s are not brothers (sisters) in law.\n",pSon->name,pDaughter->name);
	else
		printf("%s and %s are brothers (sisters) in law.\n",pSon->name,pDaughter->name);

	puts("\n Press any key to quit...");
	getch();

}
