#include "stdafx.h"
#include "stdio.h"
#include "iostream.h"
#include "stdlib.h"
#include "malloc.h"
#include "string.h"
#define StackSize 100 // 100  
#define MaxLength  100//   	
typedef int DataType;//  	
typedef struct{
	DataType data[StackSize];
	int top;
}SeqStack;   

//  
void Initial(SeqStack *S)
{// 
	S->top=-1;
} 
// 
int IsEmpty(SeqStack *S)
{
	return S->top==-1;
}
// 
int IsFull(SeqStack *S)
{
	return S->top==StackSize-1;
}
// 
void Push(SeqStack *S,DataType x)
{
	if (IsFull(S))
	{
		printf(" "); // , 
		exit(1);
	}
	S->data[++S->top]=x;// 1 x 
}
// 
DataType Pop(SeqStack *S)
{
	if(IsEmpty(S))
	{
		printf(" "); // , 
		return -1;
	}
	return S->data[S->top--];// 1
}
//  
DataType Top(SeqStack *S)
{
	if(IsEmpty(S))
	{
		printf(" "); // , 
		exit(1);
	}
	return S->data[S->top];
}
int  Hold(int c,int *minH, int *minS,SeqStack H[],int k, int n)
{//  c
	//  0
	//  N o M e m
	//  1
	//  c 
	//  
	int BestTrack = 0,i; //  
	int BestTop = n + 1;//  
	int x;//  
	// 
	for (i = 1; i <= k; i++)
		if (IsEmpty(&H[i])) 
		{//  i  
			x = Top (&H[i]) ;
			if (c<x && x < BestTop)
			{// i  
				BestTop = x;
				BestTrack = i;
			}
		}
		else //  i  
			if (!BestTrack) 
				BestTrack = i;
			if (!BestTrack) 
				return 0; // 
			// c  
			Push(&H[BestTrack],c);
			printf("Move car %d  from input to holding track %d\n" ,c, BestTrack);
			// minH  minS
			if (c<*minH) {
				*minH = c; 
				*minS = BestTrack; 
			}
			return 1;
}
void Output(int* minH, int* minS, SeqStack H[ ], int k, int n)
{ // m i n S m i n H
	int c,i; //  
	//  m i n S minH
	c=Pop(&H[*minS]) ;
	printf("Move car %d from holding track %d to output\n",*minH,*minS);
	//  m i n H m i n S
	*minH=n+2;
	for (i = 1; i <= k; i++)
		if (!IsEmpty(&H[i]) && (c=Top(&H[i])) < *minH) {
			*minH = c;
			*minS = i;
		}
}
int Railroad(int p[], int n, int k)
{// k p [1:n]
	//  1 0
	//  NoMem  
	// 
	SeqStack *H;
	int NowOut = 1; // 
	int minH =n+1; // 
	int minS,i; //minH 
	H=(SeqStack*)calloc((k+1),sizeof(SeqStack)*(k+1));
	// 
	for (i = 1; i<= n; i++)
		if (p[i] == NowOut) {//  t
			printf(" %d ",p[i]);
			NowOut++;
			// 
			while (minH == NowOut) {
				Output(&minH, &minS, H, k, n);
				NowOut++;
			}
		}
		else {//  p[i]  
			if (!Hold(p[i], &minH, &minS, H, k, n))
				return 0;
		}
		return 1;
}
void main(void)
{
	int p[8]={2,4,1,6,5,3,8,7};
	Railroad(p,8,4);
}
