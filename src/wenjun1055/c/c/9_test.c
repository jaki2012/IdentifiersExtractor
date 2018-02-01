#include <stdio.h>
#include <string.h>

int main()
{
    char *a = "abcd";
    char *b = "abcde";
    
    if (strlen(a) > strlen(b)) {
        printf("1\r\n");
    } else {
        printf("2\r\n");
    }

    //stlen >= 
    // 
    if (strlen(a) - strlen(b) >= 0) {
        printf("3\r\n");
    } else {
        printf("4\r\n");
    }
}
