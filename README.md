# Maze Robot Simulator (MRSim)
Design by PXY

## Overview
- MRSim is a simple simulator to simulate or evaluate various find-path algorithms in Arduino project (such as a robot has to escape from a large Maze).
- Users only need to focus on C++ coding in `codes/` folder, do not need to modify simulator source code.
- MRSim is based on Python language and has an interface to communicate between C++ and Python.
- In addition, this simulator also supports simple visualizations for users to analyze easily.

## Install
Recommand env: Anaconda
```
(base) $ conda env crate -f maze_env.yaml
(base) $ conda activate simulation
(simulation) $ 
```

## How to use
- Quick simulation 1
```
$ cd ./test
$ python test_sim.py
---------- [Epoch: 0] ----------
●.........
.■........
.....■....
.■........
..........
.....x....
..........
..........
..........
..........
--------------------------------
[Send] head: 2, sensor: 111, current: (0, 0), target: (5, 5)
[Recv] head: 1, new robot pos: (0, 0)
---------- [Epoch: 1] ----------
●.........
.■........
.....■....
.■........
..........
.....x....
..........
..........
..........
..........
--------------------------------
```
- Quick simulation 2
```
(step 1) modify a.cpp file to design your a star algorithm.
$ cd ./test/
$ vim a_star.cpp
(step 2) build your modified algorithm for simulation.
$ ./build.sh a_star.cpp
(step 2-1, optional) if you want to test another algorithm, modify toml file.
$ vim ./maps/ex_maps.toml
(step 2-2, optional) if you want to test in another map, modify toml file.
 $ vim ./maps/ex_maps.toml
(step 3) simulation your algorithm
$ python test_sim.py
---------- [Epoch: 0] ----------
●.........
.■........
.....■....
.■........
..........
.....x....
..........
..........
..........
..........
--------------------------------
[Send] head: 2, sensor: 111, current: (0, 0), target: (5, 5)
[Recv] head: 1, new robot pos: (0, 0)
---------- [Epoch: 1] ----------
●.........
.■........
.....■....
.■........
..........
.....x....
..........
..........
..........
..........
--------------------------------
```

## User find-path algorithm
- In MRSim, the main algorithm code is C++-based code.
- If you want to modify algorithm code, please modify `./test/a_star.cpp` code or add a new C++-based code in `./test/` folder.
```
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
```
- (Notice) if you do not want to change simulation source code, you should fix function name('algorithm') and arguments order.
    - If your algorithm function name is changed, modify `./MRS/interface.py` code.


## Map
- If you want to change another map for evaluating algorithm performance, modify `./maps/ex_maps.toml` file or add a new toml file in `./maps`.
```
title='Example map'

[sim]
    epoch=2
    user_code='./lib.a_star.cpp.so'

[obstacle]
    x=[1,5,1]
    y=[1,2,3]

[size]
    x=10
    y=10

[robot]
    num_sensor=3
    x=0
    y=0
    target_x=5
    target_y=5
```
- `user_code`: compiled C++ code, MRSim uses the paths described here to load your algorithm.
