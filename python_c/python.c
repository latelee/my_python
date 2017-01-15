/*
gcc python.c -fPIC -shared -o libhello.so
*/
#include <stdio.h>

int hello(char* buffer)
{
    printf("here in C...\n");
    printf("you input: %s\n", buffer);
    return 250;
}