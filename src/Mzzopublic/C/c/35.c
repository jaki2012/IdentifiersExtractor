#include <stdio.h>
struct ele{
	int no;
	struct ele *link;
}
main()
{
	int n,m,i;
	struct ele *h,*u,*p;
	clrscr();
	printf("Please input n&m:\n");
	scanf("%d%d",&n,&m);/* n m*/
	h=u=(struct ele *)malloc(sizeof(struct ele));/* */
	h->no=1;
	for(i=2;i<=n;i++)/* n-1 */
	{
		u->link=(struct ele *)malloc(sizeof(struct ele));
		u=u->link;
		u->no=i;/* i i*/
	}
	u->link=h;/* */
	puts("\nThe numbers of who will quit the cycle in turn are:");
	while(n)
	{
		for(i=1;i<m;i++)/* m 1 */
			u=u->link;
		p=u->link;/*p m */
		u->link=p->link;/* m */
		printf("%4d",p->no);
		free(p);/* m */
		n--;
	}
	printf("\n\n Press any key to quit...\n");
	getch();
}
