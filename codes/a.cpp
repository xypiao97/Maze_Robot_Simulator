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
    int algorithm(
        int cur_x, int cur_y,
        int tar_x, int tar_y,
        int head, int sensor_data
    ) {
        // Initialization of essential values
        int new_x = 0;
        int new_y = 0;
        int new_head = 1;

        /*
            Add your algorithm in here.
        */

        // Return values
        int send_data = new_head * 100 + new_x * 10 + new_y;
        return send_data;
    }
}

