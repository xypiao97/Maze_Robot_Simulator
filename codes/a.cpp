#include<iostream>
#include<stdio.h>

class Calling{
    public :
        void func() {
            int a = 1;
            int b = 2;
            printf( "Para: %d, Para: %d\n", a, b );
        }
};

extern "C" {
    Calling* Calling_new() {
        return new Calling();
    }
    void Calling_func(Calling* call) { call -> func(); }

    int algorithm(int a, int b) {
        printf("Arg0: %d, Arg1: %d\n", a, b);
        return 0;
    }
}

