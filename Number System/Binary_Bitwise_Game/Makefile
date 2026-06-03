CXX      := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -O2 -Isrc
SRC      := $(wildcard src/*.cpp)
OBJ      := $(SRC:.cpp=.o)
TARGET   := bitrealm

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(TARGET) $(TARGET).exe scores.txt

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run
