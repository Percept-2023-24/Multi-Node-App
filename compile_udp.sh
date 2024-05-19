#! /bin/bash

g++ -o tcp_server tcp_server.cpp
g++ -o visualizer visualizer.cpp `pkg-config --cflags --libs opencv4`