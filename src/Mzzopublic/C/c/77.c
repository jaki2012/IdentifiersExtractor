#include<stdio.h>
struct date{
    int year;
    int month;
    int day;
};
int days(struct date day);


void main()
{
    struct date today,term;
    int yearday,year,day;
	puts(" ");
	puts("                                         ");
	puts("                 ");
	puts(" 20 1990 1 1 ");
	puts("    ");
	puts(" \n");
	while(1)
	{
		printf(" >>  / / 1990 1 1  ");
		scanf("%d%d%d",&today.year,&today.month,&today.day);  /* */
		if(today.year<1990)
		{
			if(today.year<1970)
				puts(" >>  ...");
			else
				puts(" >>  ...");
			getch();
			continue;
		}
		if(today.year==1990&&today.month==1&&today.day==1)
			break;
		term.month=12;               /* */
		term.day=31;                 /* */
		for(yearday=0,year=1990;year<today.year;year++)
		{
			term.year=year;
			yearday+=days(term);     /* 1990 */
		}
		yearday+=days(today);       /* */
		day=yearday%5;               /* */
		if(day>0&&day<4) printf(" >> %d %d %d \n",today.year,today.month,today.day);   /* */
		else printf(" >> %d %d %d \n",today.year,today.month,today.day);
		
	}
	puts("\n >>       ...");
	getch();
}

int days(struct date day)
{
    static int day_tab[2][13]=
            {{0,31,28,31,30,31,30,31,31,30,31,30,31,},      /* */
             {0,31,29,31,30,31,30,31,31,30,31,30,31,},
    };
    int i,lp;
    lp=day.year%4==0&&day.year%100!=0||day.year%400==0;
      /* year lp=0 0 */
    for(i=1;i<day.month;i++)            /* 1 1 */
        day.day+=day_tab[lp][i];
    return day.day;
}
