#define N 50
main()
{
	int primes[N];
	int pc,m,k;

	clrscr();
	printf("\n The first %d prime numbers are:\n",N);
	primes[0]=2;/*2 */
	pc             =1;/* */
	m               =3;/* 3 */
	while(pc<N)
	{
	 /* m */
	k=0;
	while(primes[k]*primes[k]<=m)
		if(m%primes[k]==0)
		{/*m */
		    m+=2;/* m */
		    k=1;/* primes[0]=2 m k */
		}
		else
		k++;/* */
	primes[pc++]=m;
	m+=2;/* 2 */
	}
	/* primes[0] primes[pc-1]*/
	for(k=0;k<pc;k++)
		printf("%4d",primes[k]);
	printf("\n\n Press any key to quit...\n ");
	getch();
}