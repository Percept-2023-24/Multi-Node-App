#! /bin/bash

g++ -o tcp_server tcp_server.cpp
g++ -o visualizer visualizer.cpp `pkg-config --cflags --libs opencv4` -I /usr/local/include/opencv4
g++ -o cv_test cv_test.cpp `pkg-config --cflags --libs opencv4` -I /usr/local/include/opencv4