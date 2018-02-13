#include <stdio.h>
#define ZIPLEN 10
#define PHONLEN 15
/*struct addr */

struct addr
{
	char *name;/* */
	char *address;/* */
	char zip[ZIPLEN];/* */
	char phone[PHONLEN];/* */
};

main()/* */
{
	struct addr p[100];
	int i,j;
	clrscr();
	for(i=0;readaddr(p+i);i++);
	for(j=0;j<i;j++) writeaddr(p+j);
	puts("\n Press any key to quit...");
	getch();
}

/*  readaddr  */
int readaddr(struct addr *dpt)
{
	int len;
	char buf[120];/* */

	printf("\nPlease input the Name:\n");/* */
	if(scanf("%s",buf)==1)
	{
		len=strlen(buf);
		dpt->name=(char *)malloc(len+1);/* */
		strcpy(dpt->name,buf);
	}
	else return 0;/*Ctrl+Z */
	printf("Please input the Address:\n");/* */
	if(scanf("%s",buf)==1)
	{
		len=strlen(buf);
		dpt->address=(char *)malloc(len+1);/* */
		strcpy(dpt->address,buf);
	}
	else
	{/*Ctrl+Z */
		free(dpt->name);/* */
		return 0;
	}
	printf("Please input the Zip code:\n");/* */
	if(scanf("%s",buf)==1)
		strncpy(dpt->zip,buf,ZIPLEN-1);
	else
	{
		free(dpt->name);/* */
		free(dpt->address);/* */
		return 0;/*Ctrl+Z */
	}
	printf("Please input the Phone number:\n");/* */
	if(scanf("%s",buf)==1)
		strncpy(dpt->phone,buf,PHONLEN-1);
	else
	{
		free(dpt->name);
		free(dpt->address);
		return 0;/*Ctrl+Z */
	}
	return 1;
}

/*  writeaddr  */
int writeaddr(struct addr*dpt)
{
	printf("Name	:   %s\n",	dpt->name);/* */
	printf("Address	:   %s\n",	dpt->address);/* */
	printf("Zip	:   %s\n",	dpt->zip);/* */
	printf("Phone	:   %s\n\n",	dpt->phone);/* */
}
