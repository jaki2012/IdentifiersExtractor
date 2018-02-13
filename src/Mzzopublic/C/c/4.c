/*   */
#include <stdio.h>
main()
{
	float x,y,c;				/*   */
	printf("Please input x and y:\n");	/*   */
	scanf("%f%f",&x,&y);
	c=x>y?x:y;				/*  c=max(x,y) */
	printf("MAX of (%f,%f) is %f",x,y,c);	/*  c */
}
