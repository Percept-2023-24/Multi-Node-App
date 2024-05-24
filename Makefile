CXX = g++
CXXFLAGS = -std=c++14 -Wall -Wextra -pedantic
LDFLAGS = -lfftw3f -pthread -lm `pkg-config --cflags --libs opencv4`

SRCS = test_mod.cpp
OBJS = $(SRCS:.cpp=.o)
EXEC = test_mod

.PHONY: all clean

all: $(EXEC)

$(EXEC): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -I../../src/ -o $@ $(LDFLAGS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -I../../src/ -c $< -o $@ $(LDFLAGS)

clean:
	rm -f $(OBJS) $(EXEC)
