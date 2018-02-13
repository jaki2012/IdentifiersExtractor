/*[ ] */
#define NULL 0
int *search2(int *pa,int *pb,int an,int bn)
{
	int *ca,*cb;

	ca=pa;cb=pb;/* ca cb */
	while(ca<pa+an&&cb<pb+bn)/* */
	{
	/* */
		if(*ca<*cb)/* 1 < 2 */
		    ca++;/* 1 */
		else if(*ca>*cb)/* 1 > 2 */
		    cb++;/* 2 */
			else	/* 1 == 2 */
				/* */
			return ca;/* */
	}
	return NULL;
}

main( )/* search2( )*/
{
	int *vp,i;
	int a[ ]={1,3,5,7,9,13,15,27,29,37};
	int b[ ]={2,4,6,8,10,13,14,27,29,37};
	clrscr();
	puts("The elements of array a is:");
	for(i=0;i<sizeof(a)/sizeof(a[0]);i++)
		printf(" %d",a[i]);
	puts("\nThe elements of array b is:");
	for(i=0;i<sizeof(b)/sizeof(b[0]);i++)
		printf(" %d",b[i]);
	vp=search2(a,b,sizeof a/sizeof a[0],sizeof b/sizeof b[0]);
	if(vp) printf("\nThe first same number in both arrays is %d\n",*vp);
	else printf("Not found!\n");
	puts("\n Press any key to quit...\n");
	getch();

}
