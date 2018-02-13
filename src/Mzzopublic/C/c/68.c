#include <math.h>
#include <stdio.h>
#define MAX 8 /*  MAXxMAX */
int board[MAX];

/*   */
void show_result()
{
    int i;
    for(i=0;i<MAX;i++)
	printf("(%d,%d)",i,board[i]);
    printf("\n");
}

/*   */
int check_cross(int n)
{
    int i;
    for(i=0;i<n;i++){
	if(board[i]==board[n] || (n-i)==abs(board[i]-board[n]))return 1;
    }
    return 0;
}

/*   */
void put_chess(int n)
{
    int i;
    for(i=0;i<MAX;i++){
	board[n]=i;
	if(!check_cross(n)){
	    if(n==MAX-1) show_result();/*  ...  */
	    else put_chess(n+1);
	}
    }
}

void main()
{
	clrscr();
	puts("The possible placements are:");
    put_chess(0);
    puts("\n Press any key to quit...");
	getch();
    return;
}
