#include <stdio.h>
#include <stdbool.h>
//* 4 - Advanced Data Types, Part 1
int main(void)
{
    //* char variables
    unsigned char mychar = 68; //* Can hold a value from 0 to 255 (1 Byte). This will print out "D" because 68 corresponds to D in the ascii table
    printf("Char: %c\n", mychar);
    //* Numeric Variables
    long long int mysuperlongint = 5999999999;                        //* long long int holds 8 bytes of data, and can have values between -9 quintillion to 9 quintillion, and we use the format specifier %lld
    unsigned long long int myunsignedlonglongint = 35345565343454364; //* same as long long int but with no negative values, we use the format specifier %llu
    unsigned int myint = 2;                                           //* Same as int but doesn't hold negative values
    short int myshortint = 3;                                         //* Unlike normal int which hold 4 bytes of data, a short int can only hold 2 bytes
    unsigned short int myunsignedshortint = 5;                        //* Same as short int but doesn't hold negative values
    printf("Long long int: %lld\nUnsigner long long int: %llu\nUnsigned int: %u\nShort int: %d\nUnsigned short int: %d\n",
           mysuperlongint, myunsignedlonglongint, myint, myshortint, myunsignedshortint); //* Unsigned int uses the format specifier %u, not %d

    return 0;
}
/*
!Note
* The keyword unsigned means that the value cannot be negative number
* By default datatypes are signed, meaning they can hold negative and positive values
* You can declare short int without typing the "int" keyword (example: short myint = 2;)
* Normal int data type is considered long int, that is why there is another data type long long, to represent huge numbers
*/