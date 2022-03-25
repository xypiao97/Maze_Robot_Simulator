# Maze Robot Simulator (MRS)
Design by PXY

## Overview
- MRS simulator is a simple simulator to simulate or evaluate 'A star' algorithm in Arduino project (such as a robot has to escape from a large Maze).
- Users only need to focus on c++ coding in `codes/` folder, do not need to modify simulator source code.

## Install
Recommand env: Anaconda
```
$ conda env crate -f maze_env.yaml
$ conda activate simulation
```

## How to use
```
$ cd ./test
$ python test_sim.py
---------- [Epoch: 1] ----------
⚉.........
.🁢........
.....🁢....
.🁢........
..........
..........
..........
..........
..........
..........
--------------------------------
Recv: 1 3 1
---------- [Epoch: 2] ----------
..........
.🁢.⚉......
.....🁢....
.🁢........
..........
..........
..........
..........
..........
..........
--------------------------------
Recv: 1 3 1
```
- If you need to change maze configuration, modify `maps/ex_maps.toml` file.
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
```

## [Advanced] How to use
```
(step 1) modify a.cpp file to design your a star algorithm.
$ cd ./test/
$ vim a.cpp
(step 2) build your modified algorithm for simulation.
$ ./build.sh a.cpp
(step 3) simulation your algorithm.
$ python test_sim.py
(step 4) check your algorithm.
```