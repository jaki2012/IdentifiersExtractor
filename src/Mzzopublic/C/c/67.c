/* */

#include "string.h" 
#include "stdio.h" 

typedef struct ArcCell{
	int adj;  /* */
}ArcCell; /* */

typedef struct VertexType{
	int number;    /* */
	char *city;   /* */
}VertexType; /* */

typedef struct{
	VertexType vex[25];  /* */
	ArcCell arcs[25][25]; /* */
	int vexnum,arcnum; /* */
}MGraph; /* */

MGraph G; /* */

int P[25][25]; 
long int D[25];

void CreateUDN(v,a) /* */
int v,a;
{ int i,j;
	G.vexnum=v;
	G.arcnum=a;
	for(i=0;i<G.vexnum;++i) G.vex[i].number=i;
	/* */
	G.vex[0].city=" "; 
	G.vex[1].city=" ";
	G.vex[2].city=" ";
	G.vex[3].city=" ";
	G.vex[4].city=" ";
	G.vex[5].city=" ";
	G.vex[6].city=" ";
	G.vex[7].city=" ";
	G.vex[8].city=" ";
	G.vex[9].city=" ";
	G.vex[10].city=" ";
	G.vex[11].city=" ";
	G.vex[12].city=" ";
	G.vex[13].city=" ";
	G.vex[14].city=" ";
	G.vex[15].city=" ";
	G.vex[16].city=" ";
	G.vex[17].city=" ";
	G.vex[18].city=" ";
	G.vex[19].city=" ";
	G.vex[20].city=" ";
	G.vex[21].city=" ";
	G.vex[22].city=" ";
	G.vex[23].city=" ";
	G.vex[24].city=" ";
	/* 20000 */
	for(i=0;i<G.vexnum;++i)
		for(j=0;j<G.vexnum;++j) 
			G.arcs[i][j].adj=20000;
	/* 
		 */
	G.arcs[0][2].adj=G.arcs[2][0].adj=1892;
	G.arcs[1][2].adj=G.arcs[2][1].adj=216;
	G.arcs[2][3].adj=G.arcs[3][2].adj=1145;
	G.arcs[2][10].adj=G.arcs[10][2].adj=676;
	G.arcs[3][4].adj=G.arcs[4][3].adj=668;
	G.arcs[4][5].adj=G.arcs[5][4].adj=137;
	G.arcs[5][6].adj=G.arcs[6][5].adj=704;
	G.arcs[6][7].adj=G.arcs[7][6].adj=305;
	G.arcs[7][8].adj=G.arcs[8][7].adj=242;
	G.arcs[6][9].adj=G.arcs[9][6].adj=397;
	G.arcs[4][11].adj=G.arcs[11][4].adj=695;
	G.arcs[5][12].adj=G.arcs[12][5].adj=674;
	G.arcs[10][13].adj=G.arcs[13][10].adj=842;
	G.arcs[11][14].adj=G.arcs[14][11].adj=534;
	G.arcs[12][15].adj=G.arcs[15][12].adj=651;
	G.arcs[13][16].adj=G.arcs[16][13].adj=1100;
	G.arcs[13][17].adj=G.arcs[17][13].adj=967;
	G.arcs[14][18].adj=G.arcs[18][14].adj=409;
	G.arcs[17][18].adj=G.arcs[18][17].adj=902;
	G.arcs[15][19].adj=G.arcs[19][15].adj=825;
	G.arcs[18][19].adj=G.arcs[19][18].adj=367;
	G.arcs[19][20].adj=G.arcs[20][19].adj=622;
	G.arcs[17][21].adj=G.arcs[21][17].adj=607;
	G.arcs[18][21].adj=G.arcs[21][18].adj=672;
	G.arcs[21][22].adj=G.arcs[22][21].adj=255;
	G.arcs[18][23].adj=G.arcs[23][18].adj=675;
	G.arcs[23][24].adj=G.arcs[24][23].adj=140;
	G.arcs[16][17].adj=G.arcs[17][16].adj=639;
	G.arcs[10][11].adj=G.arcs[11][10].adj=511;
	G.arcs[11][12].adj=G.arcs[12][11].adj=349;
}
void narrate() /* */
{
	int i,k=0;
	printf("\n***************** !***************\n");
	printf("\n :\n\n");
	for(i=0;i<25;i++)
	{
		printf("(%2d)%-10s",i,G.vex[i].city); /* */
		k=k+1;
		if(k%4==0) printf("\n");
	}
}

void ShortestPath(num) /* */
int num;
{ 
	int v,w,i,t;
	int final[25];
	int min;
	for(v=0;v<25;++v)
	{
		final[v]=0;D[v]=G.arcs[num][v].adj;
		for(w=0;w<25;++w) P[v][w]=0;
		if(D[v]<20000) {P[v][num]=1;P[v][v]=1;}
	}
	D[num]=0;final[num]=1;
	for(i=0;i<25;++i)
	{
		min=20000;
		for(w=0;w<25;++w)
			if(!final[w])
				if(D[w]<min){v=w;min=D[w];}
		final[v]=1;
		for(w=0;w<25;++w)
			if(!final[w]&&((min+G.arcs[v][w].adj)<D[w]))
			{
				D[w]=min+G.arcs[v][w].adj;
				for(t=0;t<25;t++) P[w][t]=P[v][t];
				P[w][w]=1;
			}
	}
}

void output(city1,city2) /* */
int city1;
int city2;
{
	int a,b,c,d,q=0;
	a=city2;
	if(a!=city1)
	{
		printf("\n %s %s ",G.vex[city1].city,G.vex[city2].city);
		printf("(  %dkm.)\n\t",D[a]);
		printf("%s",G.vex[city1].city);
		d=city1;
		for(c=0;c<25;++c)
		{
gate:; /* goto */
	 P[a][city1]=0;
	 for(b=0;b<25;b++)
	 {
		 if(G.arcs[d][b].adj<20000&&P[a][b])
		 {
			 printf("-->%s",G.vex[b].city);q=q+1;
			 P[a][b]=0;
			 d=b;
			 if(q%8==0) printf("\n");
			 goto gate;
		 }
	 }
		}
	}
	
}
void main() /* */
{
	int v0,v1;
	CreateUDN(25,30);
	
	narrate();
	printf("\n\n 0 24 \n");
	scanf("%d",&v0);
	printf(" 0 24 \n");
	scanf("%d",&v1);
	ShortestPath(v0);  /* */
	output(v0,v1);     /* */
	printf("\n");
	printf("\n  ...\n");
	getch();
}