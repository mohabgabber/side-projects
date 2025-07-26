#include <stdio.h>
#include <stdbool.h> //* Must be included to be able to use boolean values
//* 3 - Data Types

int main(void)
{
    //* Char variables
    char mychar = 'C'; //* Must be inside single quotation marks
    printf("Char: %c\n", mychar);

    //* array of chars
    //* when assigning a value to an array of characters it must be inside double quotation marks
    char mystring[6] = "Hello"; //* This string can have a maximum of 5 chars, the final one is for the null character.
    printf("Fixed-Size string: %s\n", mystring);

    char mysecondstring[] = "I am free!"; //* Strings can also be specified without a specific size
    printf("A string with no specified length: %s\n", mysecondstring);

    //* Boolean Variables
    bool myboolean = true;              //* A boolean variable can only be either true, or false. Which is represented as the integer 1 for true, and 0 for false
    printf("Boolean: %d\n", myboolean); //* This will print 1, because the value is true

    //* Numeric Variables
    int myinteger = 100; //* Integer values can be between -2,147,483,648 to +2,147,483,647
    printf("Integer: %d\n", myinteger);

    float myfloat = 100.1254; //* 6 decimal points
    printf("Float: %f\n", myfloat);

    double mydouble = 10000.545455; //* 15 decimal points
    printf("Double: %lf\n", mydouble);
    return 0;
}

/*
 * Data Types In C

 * char = Single Character, they can also be used to store integers between the range -128 to +127, which could be used to correspond to specific characters in the ASCII table
 * char [] = array of characters (We can specify the length of this array inside the brackets)
 * float = a number with decimal points, contains 4 bytes of data (32-bit precision)
 * double = A double, is literally double the size of a float variable, doubles contain 8 bytes of data (64-bit precision)
 * int = A whole number, contains 4 bytes of data
 * bool = A boolean value can only be one of those two either: true, or false
 */

/*
!Note
* When specifying the size of a string (Example: char mystring[5] = "hell";), the size must be n+1
* For example, if you want to store a string with 5 characters, make sure to specify a size of 6
* This extra size is used by the null character which is required in C
*/