#include <stdio.h>
#include <string.h>
#include <locale.h> // setlocale LC_CTYPE  
#include <stdlib.h> //wchar_t  
//#include <wchar.h>

int main(void)
{
    char hello[] = " ";
    wchar_t c = L" ";
    wchar_t *name = L" ";
    printf("size of %d " , strlen(hello));

    printf("%d " , strlen(c));
    // printf("xxx %lc " , c);
    wprintf(L"test %s " , "test");
    
    setlocale(LC_CTYPE, "");
    wprintf(L"test %ls " , L" \n");
    wprintf(L"test %S " , L" \n");

    return 0;
}
