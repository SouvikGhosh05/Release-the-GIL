#include<stdio.h>

long long adder_fromc(long  a, long b){

    for (long i = 0; i < b; i++)
    {
        a += i;
    }
    return a;
}
