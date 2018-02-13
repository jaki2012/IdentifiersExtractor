#include<stdio.h>
void main()
{
    long mul,number,k,ll,kk,n;
    clrscr();
    puts("============================================================");
    puts("||    This program will find the automorphic numbers.     ||");
    puts("|| The defination of a automorphic number is: the mantissa||");
    puts("||     of a natural number's square equals to itself.     ||");
    puts("||       e.g., 25^2=625, 76^2=5776, 9376^2=87909376.      ||");
    puts("============================================================");
    printf("\n >> Please input the scale n you want to find : ");
    scanf("%ld",&n);
    printf("\n >> The automorphic numbers small than %ld are:\n\n",n);
    for(number=0;number<n;number++)
    {
        for(mul=number,k=1;(mul/=10)>0;k*=10);
                   /* number k*/
        kk=k*10;      /*kk */
        mul=0;        /* n */
        ll=10;        /*ll */
        while(k>0)
        {
            mul=(mul+(number%(k*10))*(number%ll-number%(ll/10)))%kk;
                 /*( + N * M ) %kk */
            k/=10;               /*k */
            ll*=10;
        }
        if(number==mul)         /* */
            printf("%ld   ",number);
    }
    puts("\n\n >> Press any key to quit...");
    getch();
}
