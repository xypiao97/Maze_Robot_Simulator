#include<iostream>
#include<stdio.h>
#include<tuple>

using namespace std;

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
        int c = a * 100 + b * 10 + (a+0);
        return c;
    }
}

