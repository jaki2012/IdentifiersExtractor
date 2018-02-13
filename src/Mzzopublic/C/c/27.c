#include <stdio.h>
#define MAX 50
/*  rep s s1 s2  */
rep(char *s,char *s1,char *s2)
{
	char *p;

	for(;*s;s++)/* s */
	{
		for(p=s1;*p&&*p!=*s;p++);/* s1 */
		if(*p)*s=*(p-s1+s2);/* s1 s2 s */
	}
}
main( )/* */
{
	char s[MAX];/*="ABCABC";*/
	char s1[MAX],s2[MAX];
	clrscr();
	puts("Please input the string for s:");
	scanf("%s",s);
	puts("Please input the string for s1:");
	scanf("%s",s1);
	puts("Please input the string for s2:");
	scanf("%s",s2);

	rep(s,s1,s2);
	puts("The string of s after displace is:");
	printf("%s\n",s);
	puts("\n Press any key to quit...");
	getch();
}
